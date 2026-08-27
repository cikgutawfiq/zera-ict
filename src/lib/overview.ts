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
};

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
      return { id: l.id, termName: term?.name ?? l.termId, weekLabel: l.weekLabel, topic: l.topic, explanation };
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
    head: [["Term", "Week", "Topic", "What students will learn"]],
    body: rows.map((r) => [r.termName, r.weekLabel, r.topic, r.explanation || "—"]),
    styles: { fontSize: 7.5, cellPadding: 1.6, valign: "top", overflow: "linebreak" },
    headStyles: { fillColor: [37, 99, 235], textColor: 255, fontStyle: "bold", fontSize: 8 },
    alternateRowStyles: { fillColor: [245, 247, 251] },
    columnStyles: {
      0: { cellWidth: 26 },
      1: { cellWidth: 20 },
      2: { cellWidth: 68, fontStyle: "bold" },
      3: { cellWidth: "auto" },
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
