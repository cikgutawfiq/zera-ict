"use client";

import { useMemo, useState } from "react";
import { useData } from "@/lib/store";
import { CLASSES } from "@/data/timetable";
import { PageHeader } from "@/components/ui";
import { buildOverviewRows, generateAllClassesOverviewPdf, generateClassOverviewPdf } from "@/lib/overview";

const ICT_CLASSES = CLASSES.filter((c) => c.subject === "ICT");

export default function OverviewPage() {
  const { lessons, terms, loading } = useData();
  const [classId, setClassId] = useState(CLASSES[0].id);
  const [exporting, setExporting] = useState<"one" | "all" | null>(null);

  const info = CLASSES.find((c) => c.id === classId) ?? CLASSES[0];
  const rows = useMemo(() => buildOverviewRows(lessons, terms, classId), [lessons, terms, classId]);

  const exportOne = async () => {
    setExporting("one");
    try {
      generateClassOverviewPdf(info, rows);
    } finally {
      setExporting(null);
    }
  };

  const exportAll = async () => {
    setExporting("all");
    try {
      const packs = ICT_CLASSES.map((c) => ({ info: c, rows: buildOverviewRows(lessons, terms, c.id) }));
      generateAllClassesOverviewPdf(packs);
    } finally {
      setExporting(null);
    }
  };

  return (
    <>
      <PageHeader title="Overview" subtitle="Whole-year topic list, by class — all 3 terms at a glance" />

      <main className="mx-auto max-w-5xl space-y-4 p-4 lg:p-6">
        <section className="card flex flex-wrap items-end gap-4 p-4">
          <label className="flex flex-col gap-1 text-sm font-semibold text-[color:var(--muted)]">
            Year / class
            <select className="field" value={classId} onChange={(e) => setClassId(e.target.value)}>
              {CLASSES.map((c) => (
                <option key={c.id} value={c.id}>
                  {c.label}
                </option>
              ))}
            </select>
          </label>

          <p className="text-sm text-[color:var(--muted)]">
            {rows.length} lesson{rows.length === 1 ? "" : "s"} across the year
          </p>

          <div className="no-print ml-auto flex flex-wrap gap-2">
            <button
              className="btn btn-sm btn-primary"
              disabled={exporting !== null || rows.length === 0}
              onClick={exportOne}
            >
              {exporting === "one" ? "Exporting…" : `📥 Save ${info.label} (PDF)`}
            </button>
            <button className="btn btn-sm" disabled={exporting !== null} onClick={exportAll}>
              {exporting === "all" ? "Exporting…" : "📚 Export Y1–Y9 pack (PDF)"}
            </button>
          </div>
        </section>

        {loading ? (
          <p className="p-6 text-sm text-[color:var(--muted)]">Loading…</p>
        ) : rows.length === 0 ? (
          <div className="card p-8 text-center text-sm text-[color:var(--muted)]">
            No topics set for this class yet.
          </div>
        ) : (
          <div className="card overflow-x-auto p-0">
            <table className="w-full min-w-[640px] border-collapse text-sm">
              <thead>
                <tr className="border-b border-[color:var(--border)] bg-[color:var(--surface-2)] text-left text-xs font-bold uppercase tracking-wide text-[color:var(--muted)]">
                  <th className="px-3 py-2.5">Term</th>
                  <th className="px-3 py-2.5">Week</th>
                  <th className="px-3 py-2.5">Topic</th>
                  <th className="px-3 py-2.5">What students will learn</th>
                </tr>
              </thead>
              <tbody>
                {rows.map((r, i) => (
                  <tr key={i} className="border-b border-[color:var(--border)] align-top last:border-0">
                    <td className="whitespace-nowrap px-3 py-2.5 text-[color:var(--muted)]">{r.termName}</td>
                    <td className="whitespace-nowrap px-3 py-2.5 font-semibold">{r.weekLabel}</td>
                    <td className="px-3 py-2.5 font-semibold">{r.topic}</td>
                    <td className="px-3 py-2.5 text-[color:var(--muted)]">{r.explanation || "—"}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </main>
    </>
  );
}
