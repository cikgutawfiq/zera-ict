"use client";

import { jsPDF } from "jspdf";
import autoTable from "jspdf-autotable";
import type { ClassInfo, Lesson } from "./types";

const MARGIN = 14;
const PAGE_W = 210; // A4 portrait, mm

function header(doc: jsPDF, info: ClassInfo | undefined, lesson: Lesson, kicker: string, title: string) {
  doc.setFont("helvetica", "bold");
  doc.setFontSize(9);
  doc.setTextColor(120);
  doc.text("ZERA ICT GUY :)", MARGIN, 14);
  doc.text(kicker, PAGE_W - MARGIN, 14, { align: "right" });

  doc.setTextColor(20);
  doc.setFontSize(18);
  doc.text(title, MARGIN, 24);

  doc.setFont("helvetica", "normal");
  doc.setFontSize(10);
  doc.setTextColor(90);
  const subject = `${info?.label ?? lesson.classId} · ${lesson.weekLabel}`;
  const topic = [lesson.topic, lesson.subtopic].filter(Boolean).join(" — ");
  doc.text(subject, MARGIN, 31);
  if (topic) doc.text(topic, MARGIN, 36.5);

  doc.setDrawColor(210);
  doc.line(MARGIN, 40, PAGE_W - MARGIN, 40);

  doc.setFontSize(10);
  doc.setTextColor(60);
  doc.text("Name: ______________________________", MARGIN, 47);
  doc.text("Date: ____________", PAGE_W - MARGIN - 45, 47);

  return 55;
}

function questionBlock(
  doc: jsPDF,
  y: number,
  n: number,
  prompt: string,
  lines: number,
): number {
  const maxWidth = PAGE_W - MARGIN * 2 - 8;
  doc.setFont("helvetica", "bold");
  doc.setFontSize(11);
  doc.setTextColor(20);
  const wrapped = doc.splitTextToSize(`${n}. ${prompt}`, maxWidth);
  if (y + wrapped.length * 5.5 + lines * 8 > 285) {
    doc.addPage();
    y = 20;
  }
  doc.text(wrapped, MARGIN, y);
  y += wrapped.length * 5.5 + 3;

  doc.setDrawColor(200);
  for (let i = 0; i < lines; i++) {
    doc.line(MARGIN + 6, y, PAGE_W - MARGIN, y);
    y += 8;
  }
  return y + 3;
}

type Difficulty = { label: string; kicker: string };

const DIFFICULTIES: Difficulty[] = [
  { label: "Foundation", kicker: "Worksheet A · Foundation" },
  { label: "Core", kicker: "Worksheet B · Core" },
  { label: "Challenge", kicker: "Worksheet C · Challenge" },
];

function foundationQuestions(lesson: Lesson): string[] {
  const qs: string[] = [];
  if (lesson.topic) qs.push(`In your own words, what is "${lesson.topic}"? Write 1–2 sentences.`);
  if (lesson.subtopic) qs.push(`Write down what "${lesson.subtopic}" means, in your own words.`);
  for (const obj of lesson.objectives.slice(0, 3)) {
    qs.push(`This lesson's goal is: "${obj}". Give one example of this.`);
  }
  if (qs.length < 3) qs.push(`List 3 things you learned about ${lesson.topic || "today's lesson"}.`);
  return qs.slice(0, 5);
}

function coreQuestions(lesson: Lesson): string[] {
  const qs: string[] = [];
  for (const act of lesson.activities.slice(0, 2)) {
    qs.push(`Task: ${act} — describe what you did and what happened.`);
  }
  if (lesson.topic) qs.push(`Explain why "${lesson.topic}" is useful. Give one real-life example.`);
  for (const sc of lesson.successCriteria.slice(0, 2)) {
    qs.push(`Show that you can do this: "${sc}". Describe or demonstrate it below.`);
  }
  if (qs.length < 3) qs.push(`Explain, step by step, how you would use ${lesson.topic || "what you learned today"}.`);
  return qs.slice(0, 5);
}

function challengeQuestions(lesson: Lesson): string[] {
  const qs: string[] = [];
  if (lesson.topic) qs.push(`Design your own example that shows "${lesson.topic}" in action. Describe it in detail.`);
  if (lesson.subtopic) qs.push(`What could go wrong if someone did not understand "${lesson.subtopic}"? How would you fix it?`);
  qs.push(`Extension: connect what you learned today to something you already knew. Explain the link.`);
  qs.push(`Write 3 questions you would ask a partner to check they understood today's lesson, and model answers.`);
  return qs.slice(0, 4);
}

const QUESTION_BUILDERS: Record<string, (lesson: Lesson) => string[]> = {
  Foundation: foundationQuestions,
  Core: coreQuestions,
  Challenge: challengeQuestions,
};

const LINES_PER_LEVEL: Record<string, number> = { Foundation: 2, Core: 3, Challenge: 4 };

export function generateWorksheetsPdf(lesson: Lesson, info: ClassInfo | undefined) {
  const doc = new jsPDF({ unit: "mm", format: "a4" });

  DIFFICULTIES.forEach((d, idx) => {
    if (idx > 0) doc.addPage();
    let y = header(doc, info, lesson, d.kicker, `${d.label} worksheet`);
    const questions = QUESTION_BUILDERS[d.label](lesson);
    const lines = LINES_PER_LEVEL[d.label];
    questions.forEach((q, i) => {
      y = questionBlock(doc, y, i + 1, q, lines);
    });
  });

  const filename = `${(info?.label ?? lesson.classId).replace(/\s+/g, "-")}_${lesson.weekLabel.replace(/\s+/g, "-")}_worksheets.pdf`;
  doc.save(filename);
}

const RUBRIC_LEVELS = [
  { label: "Excellent", score: 4, tone: "Consistently and independently demonstrates" },
  { label: "Good", score: 3, tone: "Usually demonstrates, with minor support" },
  { label: "Satisfactory", score: 2, tone: "Sometimes demonstrates, needs support" },
  { label: "Needs Improvement", score: 1, tone: "Rarely demonstrates, needs significant support" },
];

export function generateRubricPdf(lesson: Lesson, info: ClassInfo | undefined) {
  const doc = new jsPDF({ unit: "mm", format: "a4", orientation: "landscape" });
  const criteria = lesson.successCriteria.length ? lesson.successCriteria : lesson.objectives;

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

  doc.setFontSize(9);
  doc.text("Name: ______________________________", MARGIN, 34);
  doc.text("Total: _____ / " + criteria.length * 4, 297 - MARGIN - 35, 34);

  const head = [["Criteria", ...RUBRIC_LEVELS.map((l) => `${l.label} (${l.score})`)]];
  const body = (criteria.length ? criteria : ["Participation and effort in today's lesson"]).map((c) => [
    c,
    ...RUBRIC_LEVELS.map((l) => `${l.tone}:\n${c}`),
  ]);

  autoTable(doc, {
    startY: 39,
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
  });

  const filename = `${(info?.label ?? lesson.classId).replace(/\s+/g, "-")}_${lesson.weekLabel.replace(/\s+/g, "-")}_rubric.pdf`;
  doc.save(filename);
}
