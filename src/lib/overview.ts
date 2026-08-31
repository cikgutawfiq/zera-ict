"use client";

import { jsPDF } from "jspdf";
import autoTable from "jspdf-autotable";
import type { ClassInfo, Lesson, Term } from "./types";

export type OverviewRow = {
  id: string;
  termName: string;
  weekLabel: string;
  topic: string;
  explanation: string;
  detail: string;
};

/** The richest single piece of "what actually happens" text available on a lesson.
 *  Activities are preferred over plan-step detail — some plan templates (e.g. ICT's
 *  equipment-mode-driven steps) intentionally keep the step body generic across a
 *  whole class of weeks, while activities always name the actual topic/subtopic, so
 *  they stay genuinely distinct week to week. Used for the Overview's detail column
 *  and PDF export. */
function pickDetail(l: Lesson): string {
  if (l.activities.length) return l.activities.slice(0, 2).join("; ");
  if (l.objectives.length) return l.objectives.join(" ");
  const mainStep = l.plan.find((s) => /main|task|explore|practice|apply|show/i.test(s.title));
  return mainStep?.detail ?? "";
}

export function buildOverviewRows(lessons: Lesson[], terms: Term[], classId: string): OverviewRow[] {
  const termOrder = new Map(terms.map((t) => [t.id, t.order]));
  return lessons
    .filter((l) => l.classId === classId && l.topic.trim())
    .sort(
      (a, b) =>
        (termOrder.get(a.termId) ?? 0) - (termOrder.get(b.termId) ?? 0) || a.dateStart.localeCompare(b.dateStart),
    )
    .map((l) => {
      const term = terms.find((t) => t.id === l.termId);
      const explanation = l.subtopic || l.objectives[0] || l.activities[0] || "";
      return {
        id: l.id,
        termName: term?.name ?? l.termId,
        weekLabel: l.weekLabel,
        topic: l.topic,
        explanation,
        detail: pickDetail(l),
      };
    });
}

function addClassPage(doc: jsPDF, info: ClassInfo, rows: OverviewRow[], first: boolean) {
  if (!first) doc.addPage();

  doc.setFont("helvetica", "bold");
  doc.setFontSize(16);
  doc.setTextColor(20);
  doc.text(`${info.label} — Whole-year topic overview`, 14, 14);

  doc.setFont("helvetica", "normal");
  doc.setFontSize(9);
  doc.setTextColor(110);
  doc.text(`${rows.length} lessons across the year, all terms`, 14, 20);

  autoTable(doc, {
    startY: 25,
    head: [["Term", "Week", "Topic", "What students will learn", "Lesson detail"]],
    body: rows.map((r) => [r.termName, r.weekLabel, r.topic, r.explanation || "—", r.detail || "—"]),
    styles: { fontSize: 7, cellPadding: 1.6, valign: "top", overflow: "linebreak" },
    headStyles: { fillColor: [37, 99, 235], textColor: 255, fontStyle: "bold", fontSize: 8 },
    alternateRowStyles: { fillColor: [245, 247, 251] },
    columnStyles: {
      0: { cellWidth: 22 },
      1: { cellWidth: 18 },
      2: { cellWidth: 52, fontStyle: "bold" },
      3: { cellWidth: 68 },
      4: { cellWidth: "auto" },
    },
    margin: { left: 14, right: 14, top: 25, bottom: 12 },
    theme: "striped",
  });
}

export function generateClassOverviewPdf(info: ClassInfo, rows: OverviewRow[]) {
  const doc = new jsPDF({ unit: "mm", format: "a4", orientation: "landscape" });
  addClassPage(doc, info, rows, true);
  doc.save(`${info.label.replace(/\s+/g, "-")}_overview.pdf`);
}

export function generateAllClassesOverviewPdf(packs: { info: ClassInfo; rows: OverviewRow[] }[]) {
  const doc = new jsPDF({ unit: "mm", format: "a4", orientation: "landscape" });
  packs.forEach(({ info, rows }, i) => addClassPage(doc, info, rows, i === 0));
  doc.save("Zera-ICT_Y1-Y9_topic-overview.pdf");
}
