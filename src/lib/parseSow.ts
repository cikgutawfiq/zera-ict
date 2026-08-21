import readXlsxFile from "read-excel-file/browser";
import seedData from "@/data/seed.json";
import { assignMoralContent } from "@/data/values";
import type { Lesson, Term, TermWeek } from "./types";

/**
 * Browser-side mirror of scripts/extract_sow.py + scripts/build_seed.py,
 * for the Admin "upload workbook" flow. Re-parses the two SOW workbooks,
 * keeping the same shape scripts/build_seed.py writes to seed.json, so the
 * result can be handed straight to useData().seed(...).
 *
 * The two workbooks only ever contain Term 1 — Term 2 and Term 3 have no
 * source file, so this only ever touches term-1 lessons.
 */

const HEADER_ROW_INDEX = 8; // 0-indexed row of the header ("Week | Date | Topic | ...")
const ICT_YEARS = [1, 2, 3, 4, 5, 6, 7, 8, 9] as const;
const YEAR_TO_FILE: Record<number, "ks1ks2" | "ks3"> = {
  1: "ks1ks2",
  2: "ks1ks2",
  3: "ks1ks2",
  4: "ks1ks2",
  5: "ks1ks2",
  6: "ks1ks2",
  7: "ks3",
  8: "ks3",
  9: "ks3",
};

const DATE_RANGE = /(\d{1,2})\.(\d{1,2})\.(\d{4})\s*[-–]\s*(\d{1,2})\.(\d{1,2})\.(\d{4})/;

type RawRow = {
  weekLabel: string;
  weekNo: number | null;
  dateText: string;
  dateStart: string | null;
  dateEnd: string | null;
  topic: string;
  subtopic: string;
  outline: string;
  sowResources: string;
  remark: string;
  isBreak: boolean;
  isExam: boolean;
};

function clean(value: unknown): string {
  if (value === null || value === undefined) return "";
  return String(value)
    .replace(/ /g, " ")
    .replace(/→/g, "->")
    .replace(/[ \t]+/g, " ")
    .trim();
}

function pad(n: number): string {
  return String(n).padStart(2, "0");
}

function parseDates(text: string): { start: string | null; end: string | null } {
  const m = DATE_RANGE.exec(text);
  if (!m) return { start: null, end: null };
  const [, d1, mo1, y1, d2, mo2, y2] = m;
  return {
    start: `${y1}-${pad(Number(mo1))}-${pad(Number(d1))}`,
    end: `${y2}-${pad(Number(mo2))}-${pad(Number(d2))}`,
  };
}

function weekNumber(label: string): number | null {
  const m = /(\d+)/.exec(label);
  return m ? Number(m[1]) : null;
}

function readYearSheet(rows: unknown[][]): RawRow[] {
  const out: RawRow[] = [];
  for (let i = HEADER_ROW_INDEX + 1; i < rows.length; i++) {
    const row = rows[i] ?? [];
    const [weekLabelRaw, dateText, topic, subtopic, outline, sowResources, remark] = [
      clean(row[0]),
      clean(row[1]),
      clean(row[2]),
      clean(row[3]),
      clean(row[4]),
      clean(row[5]),
      clean(row[6]),
    ];
    if (![weekLabelRaw, dateText, topic, subtopic, outline].some(Boolean)) continue;
    const { start, end } = parseDates(dateText);
    const isBreak = topic.toLowerCase().includes("break") || !weekLabelRaw;
    out.push({
      weekLabel: weekLabelRaw || "Break",
      weekNo: weekNumber(weekLabelRaw),
      dateText,
      dateStart: start,
      dateEnd: end,
      topic,
      subtopic,
      outline,
      sowResources,
      remark,
      isBreak,
      isExam: topic.toLowerCase().includes("exam"),
    });
  }
  return out;
}

export type ParsedWorkbooks = { ks1ks2: File; ks3: File };

const AUTHORED_TERM1: Record<string, Lesson> = Object.fromEntries(
  (seedData as unknown as { lessons: Lesson[] }).lessons
    .filter((l) => l.termId === "term-1" && l.classId.startsWith("ict-y"))
    .map((l) => [l.id, l]),
);

const BLANK_CLASSES: { classId: string; subject: string }[] = [
  { classId: "maths-y1", subject: "Mathematics" },
  { classId: "me-y8", subject: "Malay Enrichment" },
];

export async function parseSowWorkbooks(
  files: ParsedWorkbooks,
): Promise<{ terms: [Term]; lessons: Lesson[] }> {
  const sheetsByFile: Record<"ks1ks2" | "ks3", { sheet: string; data: unknown[][] }[]> = {
    ks1ks2: (await readXlsxFile(files.ks1ks2)) as unknown as { sheet: string; data: unknown[][] }[],
    ks3: (await readXlsxFile(files.ks3)) as unknown as { sheet: string; data: unknown[][] }[],
  };

  const rowsByYear = new Map<number, RawRow[]>();
  for (const year of ICT_YEARS) {
    const source = sheetsByFile[YEAR_TO_FILE[year]];
    const sheet = source.find((s) => s.sheet.trim().toUpperCase() === `YEAR ${year}`);
    if (!sheet) throw new Error(`Sheet "YEAR ${year}" not found in the uploaded workbook.`);
    rowsByYear.set(year, readYearSheet(sheet.data));
  }

  const year1Rows = rowsByYear.get(1)!;
  const weeks: TermWeek[] = year1Rows.map((r) => ({
    no: r.weekNo,
    label: r.weekLabel,
    start: r.dateStart ?? "",
    end: r.dateEnd ?? "",
    isBreak: r.isBreak,
    isExam: r.isExam,
    remark: r.remark,
  }));
  const term: Term = { id: "term-1", name: "Term 1", order: 1, weeks };

  const lessons: Lesson[] = [];
  for (const year of ICT_YEARS) {
    const classId = `ict-y${year}`;
    const rows = rowsByYear.get(year)!.filter((r) => !r.isBreak);
    rows.forEach((row, order) => {
      if (row.weekNo == null || !row.dateStart || !row.dateEnd) return;
      const id = `${classId}_term-1_w${row.weekNo}`;
      const authored = AUTHORED_TERM1[id];
      lessons.push({
        id,
        classId,
        subject: "ICT",
        termId: "term-1",
        weekNo: row.weekNo,
        weekLabel: row.weekLabel,
        dateStart: row.dateStart,
        dateEnd: row.dateEnd,
        topic: row.topic,
        subtopic: row.subtopic,
        outline: row.outline,
        sowResources: row.sowResources,
        remark: row.remark,
        objectives: authored?.objectives ?? [],
        plan: authored?.plan ?? [],
        activities: authored?.activities ?? [],
        successCriteria: authored?.successCriteria ?? [],
        resources: authored?.resources ?? [],
        ...assignMoralContent(classId, order),
        status: "planned",
        note: "",
        order,
      });
    });
  }

  const teachingWeeks = weeks.filter((w) => !w.isBreak);
  for (const spec of BLANK_CLASSES) {
    teachingWeeks.forEach((week, order) => {
      const id = `${spec.classId}_term-1_w${week.no}`;
      lessons.push({
        id,
        classId: spec.classId,
        subject: spec.subject,
        termId: "term-1",
        weekNo: week.no ?? order + 1,
        weekLabel: week.label,
        dateStart: week.start,
        dateEnd: week.end,
        topic: "",
        subtopic: "",
        outline: "",
        sowResources: "",
        remark: week.remark,
        objectives: [],
        plan: [],
        activities: [],
        successCriteria: [],
        resources: [],
        ...assignMoralContent(spec.classId, order),
        status: "planned",
        note: "",
        order,
      });
    });
  }

  return { terms: [term], lessons };
}
