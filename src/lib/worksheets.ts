"use client";

import { jsPDF } from "jspdf";
import autoTable from "jspdf-autotable";
import type { ClassInfo, Lesson } from "./types";

const MARGIN = 14;
const PAGE_W = 210; // A4 portrait, mm
const PAGE_BOTTOM = 283;

function header(
  doc: jsPDF,
  info: ClassInfo | undefined,
  lesson: Lesson,
  kicker: string,
  title: string,
  difficulty: string,
) {
  doc.setFont("helvetica", "bold");
  doc.setFontSize(9);
  doc.setTextColor(120);
  doc.text("ZERA ICT GUY :)", MARGIN, 14);
  doc.text(kicker, PAGE_W - MARGIN, 14, { align: "right" });

  doc.setTextColor(20);
  doc.setFontSize(18);
  doc.text(title, MARGIN, 24);

  doc.setFont("helvetica", "bold");
  doc.setFontSize(9);
  doc.setTextColor(37, 99, 235);
  doc.text(`Difficulty: ${difficulty}`, MARGIN, 29.5);

  doc.setFont("helvetica", "normal");
  doc.setFontSize(10);
  doc.setTextColor(90);
  const subject = `${info?.label ?? lesson.classId} · ${lesson.weekLabel}`;
  const topic = [lesson.topic, lesson.subtopic].filter(Boolean).join(" — ");
  doc.text(subject, MARGIN, 35.5);
  if (topic) doc.text(topic, MARGIN, 41);

  doc.setFontSize(10);
  doc.setTextColor(60);
  doc.text("Name: ______________________________", MARGIN, 48.5);
  doc.text("Date: ____________", PAGE_W - MARGIN - 45, 48.5);

  return 55;
}

function teacherNote(doc: jsPDF, y: number, text: string): number {
  const maxWidth = PAGE_W - MARGIN * 2 - 10;
  const wrapped = doc.splitTextToSize(text, maxWidth);
  const boxH = wrapped.length * 4.4 + 9;
  doc.setFillColor(234, 240, 250);
  doc.roundedRect(MARGIN, y, PAGE_W - MARGIN * 2, boxH, 2, 2, "F");
  doc.setFont("helvetica", "bold");
  doc.setFontSize(8);
  doc.setTextColor(37, 99, 235);
  doc.text("HOW TO RUN THIS", MARGIN + 4, y + 5.5);
  doc.setFont("helvetica", "normal");
  doc.setFontSize(8.5);
  doc.setTextColor(70);
  doc.text(wrapped, MARGIN + 4, y + 10);
  return y + boxH + 7;
}

function ensureSpace(doc: jsPDF, y: number, needed: number): number {
  if (y + needed > PAGE_BOTTOM) {
    doc.addPage();
    return 20;
  }
  return y;
}

function qaBlock(doc: jsPDF, y: number, n: number, prompt: string, lines: number): number {
  const maxWidth = PAGE_W - MARGIN * 2 - 8;
  doc.setFont("helvetica", "bold");
  doc.setFontSize(11);
  doc.setTextColor(20);
  const wrapped = doc.splitTextToSize(`${n}. ${prompt}`, maxWidth);
  y = ensureSpace(doc, y, wrapped.length * 5.5 + lines * 8);
  doc.text(wrapped, MARGIN, y);
  y += wrapped.length * 5.5 + 3;

  doc.setDrawColor(200);
  for (let i = 0; i < lines; i++) {
    doc.line(MARGIN + 6, y, PAGE_W - MARGIN, y);
    y += 8;
  }
  return y + 3;
}

function pickKeyword(lesson: Lesson): string {
  const source = `${lesson.subtopic} ${lesson.topic}`.replace(/[^a-zA-Z ]/g, "");
  const words = source
    .split(" ")
    .map((w) => w.trim())
    .filter((w) => w.length >= 4)
    .sort((a, b) => b.length - a.length);
  return (words[0] ?? "TOPIC").toUpperCase();
}

function scramble(word: string): string {
  if (word.length < 2) return word;
  const letters = word.split("");
  let out = word;
  for (let attempt = 0; attempt < 12 && out === word; attempt++) {
    for (let i = letters.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [letters[i], letters[j]] = [letters[j], letters[i]];
    }
    out = letters.join("");
  }
  return out;
}

function wordPuzzleBlock(doc: jsPDF, y: number, n: number, lesson: Lesson): number {
  const word = pickKeyword(lesson);
  const scrambled = scramble(word);
  const hintSource = lesson.subtopic || lesson.topic || "today's lesson";

  const maxWidth = PAGE_W - MARGIN * 2 - 8;
  doc.setFont("helvetica", "bold");
  doc.setFontSize(11);
  doc.setTextColor(20);
  const wrapped = doc.splitTextToSize(`${n}. WORD PUZZLE — unscramble the letters below.`, maxWidth);
  y = ensureSpace(doc, y, wrapped.length * 5.5 + 34);
  doc.text(wrapped, MARGIN, y);
  y += wrapped.length * 5.5 + 5;

  doc.setFont("courier", "bold");
  doc.setFontSize(20);
  doc.setTextColor(37, 99, 235);
  doc.text(scrambled.split("").join("  "), MARGIN + 6, y + 6);
  y += 14;

  doc.setFont("helvetica", "italic");
  doc.setFontSize(9);
  doc.setTextColor(110);
  const hintWrapped = doc.splitTextToSize(`Hint: it's something to do with "${hintSource}".`, maxWidth - 6);
  doc.text(hintWrapped, MARGIN + 6, y);
  y += hintWrapped.length * 4.5 + 4;

  doc.setFont("helvetica", "normal");
  doc.setFontSize(10);
  doc.setTextColor(60);
  doc.text("Answer: ______________________________", MARGIN + 6, y);
  return y + 10;
}

function timedBlock(doc: jsPDF, y: number, n: number, task: string, minutes: number): number {
  const maxWidth = PAGE_W - MARGIN * 2 - 8;
  doc.setFont("helvetica", "bold");
  doc.setFontSize(11);
  doc.setTextColor(20);
  const wrapped = doc.splitTextToSize(`${n}. BEAT THE CLOCK (${minutes} minutes) — ${task}`, maxWidth);
  y = ensureSpace(doc, y, wrapped.length * 5.5 + 28);
  doc.text(wrapped, MARGIN, y);
  y += wrapped.length * 5.5 + 4;

  doc.setDrawColor(217, 119, 6);
  doc.setLineWidth(0.6);
  doc.rect(MARGIN + 6, y, PAGE_W - MARGIN * 2 - 6, 22);
  doc.setLineWidth(0.2);
  return y + 27;
}

function checkInBlock(doc: jsPDF, y: number, n: number): number {
  const maxWidth = PAGE_W - MARGIN * 2 - 8;
  doc.setFont("helvetica", "bold");
  doc.setFontSize(11);
  doc.setTextColor(20);
  const wrapped = doc.splitTextToSize(`${n}. QUICK CHECK-IN — circle one, then tell us why in a sentence.`, maxWidth);
  y = ensureSpace(doc, y, wrapped.length * 5.5 + 24);
  doc.text(wrapped, MARGIN, y);
  y += wrapped.length * 5.5 + 5;

  doc.setFont("helvetica", "normal");
  doc.setFontSize(11);
  doc.setTextColor(60);
  doc.text("Nailed it          Getting there          Still stuck", MARGIN + 6, y);
  y += 9;

  doc.setDrawColor(200);
  doc.line(MARGIN + 6, y, PAGE_W - MARGIN, y);
  return y + 9;
}

function bonusBlock(doc: jsPDF, y: number, n: number, prompt: string): number {
  const maxWidth = PAGE_W - MARGIN * 2 - 14;
  doc.setFont("helvetica", "bolditalic");
  doc.setFontSize(11);
  doc.setTextColor(124, 58, 237);
  const wrapped = doc.splitTextToSize(`${n}. BONUS CHALLENGE — ${prompt}`, maxWidth);
  const boxH = wrapped.length * 5.5 + 33;
  y = ensureSpace(doc, y, boxH + 6);
  doc.setDrawColor(124, 58, 237);
  doc.setLineWidth(0.6);
  doc.roundedRect(MARGIN, y - 4, PAGE_W - MARGIN * 2, boxH, 3, 3);
  doc.setLineWidth(0.2);
  doc.text(wrapped, MARGIN + 5, y + 3);
  let ly = y + wrapped.length * 5.5 + 8;
  doc.setDrawColor(210);
  for (let i = 0; i < 3; i++) {
    doc.line(MARGIN + 8, ly, PAGE_W - MARGIN - 5, ly);
    ly += 7;
  }
  return y - 4 + boxH + 8;
}

type Level = "Foundation" | "Core" | "Challenge";

const DIFFICULTY_LABEL: Record<Level, string> = {
  Foundation: "Easy — recall & understand",
  Core: "Medium — apply & explain",
  Challenge: "Hard — design & extend",
};

const NOTES: Record<Level, string> = {
  Foundation:
    "Best as a starter, cover-lesson task, or independent catch-up. Allow about 15 minutes; students may use their notes.",
  Core: "Best run in pairs or small groups as the main task. Allow 20-25 minutes. The timed round works well read aloud.",
  Challenge:
    "For fast finishers, homework, or an extension group. No time pressure - depth and creativity over speed.",
};

function renderFoundation(doc: jsPDF, lesson: Lesson, y: number): void {
  y = teacherNote(doc, y, NOTES.Foundation);
  let n = 1;
  if (lesson.topic) y = qaBlock(doc, y, n++, `In your own words, what is "${lesson.topic}"? Write 1-2 sentences.`, 2);
  y = wordPuzzleBlock(doc, y, n++, lesson);
  for (const obj of lesson.objectives.slice(0, 2)) {
    y = qaBlock(doc, y, n++, `This lesson's goal is: "${obj}". Give one example of this.`, 2);
  }
  y = checkInBlock(doc, y, n++);
}

function renderCore(doc: jsPDF, lesson: Lesson, y: number): void {
  y = teacherNote(doc, y, NOTES.Core);
  let n = 1;
  for (const act of lesson.activities.slice(0, 2)) {
    y = qaBlock(doc, y, n++, `Task: ${act} — describe what you did and what happened.`, 3);
  }
  if (lesson.topic) y = qaBlock(doc, y, n++, `Explain why "${lesson.topic}" is useful. Give one real-life example.`, 3);
  const timedTask = lesson.activities[0] || lesson.topic || "today's skill";
  y = timedBlock(doc, y, n++, `Go as far as you can with: ${timedTask}. Ready, set, go!`, 5);
  for (const sc of lesson.successCriteria.slice(0, 1)) {
    y = qaBlock(doc, y, n++, `Show that you can do this: "${sc}". Describe or demonstrate it below.`, 3);
  }
}

function renderChallenge(doc: jsPDF, lesson: Lesson, y: number): void {
  y = teacherNote(doc, y, NOTES.Challenge);
  let n = 1;
  if (lesson.topic)
    y = qaBlock(doc, y, n++, `Design your own example that shows "${lesson.topic}" in action. Describe it in detail.`, 4);
  if (lesson.subtopic)
    y = qaBlock(
      doc,
      y,
      n++,
      `What could go wrong if someone did not understand "${lesson.subtopic}"? How would you fix it?`,
      4,
    );
  y = bonusBlock(
    doc,
    y,
    n++,
    `Connect what you learned today to something you already knew from another lesson or subject. Explain the link, then write 3 quiz questions (with answers) you'd use to check a partner really understood it.`,
  );
}

const RENDERERS: Record<Level, (doc: jsPDF, lesson: Lesson, y: number) => void> = {
  Foundation: renderFoundation,
  Core: renderCore,
  Challenge: renderChallenge,
};

const LEVELS: { key: Level; kicker: string }[] = [
  { key: "Foundation", kicker: "Worksheet A - Foundation" },
  { key: "Core", kicker: "Worksheet B - Core" },
  { key: "Challenge", kicker: "Worksheet C - Challenge" },
];

export function generateWorksheetsPdf(lesson: Lesson, info: ClassInfo | undefined) {
  const doc = new jsPDF({ unit: "mm", format: "a4" });

  LEVELS.forEach(({ key, kicker }, idx) => {
    if (idx > 0) doc.addPage();
    const y = header(doc, info, lesson, kicker, `${key} worksheet`, DIFFICULTY_LABEL[key]);
    RENDERERS[key](doc, lesson, y);
  });

  const filename = `${(info?.label ?? lesson.classId).replace(/\s+/g, "-")}_${lesson.weekLabel.replace(/\s+/g, "-")}_worksheets.pdf`;
  doc.save(filename);
}

const RUBRIC_LEVELS = [
  { label: "Superstar", score: 4, tone: "Consistently and independently demonstrates" },
  { label: "Solid", score: 3, tone: "Usually demonstrates, with minor support" },
  { label: "Growing", score: 2, tone: "Sometimes demonstrates, needs support" },
  { label: "Just Starting", score: 1, tone: "Rarely demonstrates, needs significant support" },
];

export function generateRubricPdf(lesson: Lesson, info: ClassInfo | undefined) {
  const doc = new jsPDF({ unit: "mm", format: "a4", orientation: "landscape" });
  const criteria = lesson.successCriteria.length ? lesson.successCriteria : lesson.objectives;
  const criteriaCount = criteria.length || 1;

  doc.setFont("helvetica", "bold");
  doc.setFontSize(9);
  doc.setTextColor(120);
  doc.text("ZERA ICT GUY :)", MARGIN, 12);
  doc.text("Assessment rubric", 297 - MARGIN, 12, { align: "right" });

  doc.setTextColor(20);
  doc.setFontSize(16);
  doc.text(`${info?.label ?? lesson.classId} · ${lesson.weekLabel}`, MARGIN, 21);

  doc.setFont("helvetica", "normal");
  doc.setFontSize(10);
  doc.setTextColor(90);
  const topic = [lesson.topic, lesson.subtopic].filter(Boolean).join(" — ");
  if (topic) doc.text(topic, MARGIN, 27);

  doc.setFont("helvetica", "italic");
  doc.setFontSize(8.5);
  doc.setTextColor(110);
  doc.text(
    "How to use: score each row 1-4 as the lesson goes, or hand this to students to self-assess first, then compare.",
    MARGIN,
    32.5,
  );

  doc.setFont("helvetica", "normal");
  doc.setFontSize(9);
  doc.setTextColor(60);
  doc.text("Name: ______________________________", MARGIN, 38.5);
  doc.text(`Total: _____ / ${criteriaCount * 4}`, 297 - MARGIN - 35, 38.5);

  const head = [["Criteria", ...RUBRIC_LEVELS.map((l) => `${l.label} (${l.score})`)]];
  const body = (criteria.length ? criteria : ["Participation and effort in today's lesson"]).map((c) => [
    c,
    ...RUBRIC_LEVELS.map((l) => `${l.tone}:\n${c}`),
  ]);

  autoTable(doc, {
    startY: 43,
    head,
    body,
    styles: { fontSize: 8, cellPadding: 2.5, valign: "top", overflow: "linebreak" },
    headStyles: { fillColor: [37, 99, 235], textColor: 255, fontStyle: "bold" },
    columnStyles: {
      0: { cellWidth: 55, fontStyle: "bold" },
      1: { cellWidth: 55 },
      2: { cellWidth: 55 },
      3: { cellWidth: 55 },
      4: { cellWidth: 55 },
    },
    margin: { left: MARGIN, right: MARGIN },
    didDrawPage: (data) => {
      const pageH = doc.internal.pageSize.getHeight();
      const finalY = data.cursor?.y ?? pageH - 20;
      if (finalY < pageH - 22) {
        doc.setFont("helvetica", "normal");
        doc.setFontSize(8);
        doc.setTextColor(120);
        doc.text(
          `Grade bands: ${criteriaCount * 4}-${Math.ceil(criteriaCount * 3.6)} Superstar · ${Math.ceil(criteriaCount * 3.5)}-${Math.ceil(criteriaCount * 2.6)} Solid · ${Math.ceil(criteriaCount * 2.5)}-${Math.ceil(criteriaCount * 1.6)} Growing · below that, Just Starting.`,
          MARGIN,
          finalY + 8,
        );
      }
    },
  });

  const filename = `${(info?.label ?? lesson.classId).replace(/\s+/g, "-")}_${lesson.weekLabel.replace(/\s+/g, "-")}_rubric.pdf`;
  doc.save(filename);
}
