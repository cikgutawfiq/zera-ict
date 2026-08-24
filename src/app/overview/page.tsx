"use client";

import { useEffect, useMemo, useState } from "react";
import { useData } from "@/lib/store";
import { CLASSES } from "@/data/timetable";
import { PageHeader } from "@/components/ui";
import { MindMap, type MindMapNode } from "@/components/MindMap";

export default function OverviewPage() {
  const { lessons, terms, loading } = useData();
  const [classId, setClassId] = useState(CLASSES[0].id);
  const [termId, setTermId] = useState<string>("");

  useEffect(() => {
    if (!termId && terms.length) setTermId(terms[0].id);
  }, [terms, termId]);

  const info = CLASSES.find((c) => c.id === classId);
  const term = terms.find((t) => t.id === termId);

  const nodes: MindMapNode[] = useMemo(() => {
    return lessons
      .filter((l) => l.classId === classId && l.termId === termId && l.topic.trim())
      .sort((a, b) => a.dateStart.localeCompare(b.dateStart))
      .map((l) => ({
        id: l.id,
        title: `${l.weekLabel} · ${l.topic}`,
        subtitle: l.subtopic || undefined,
      }));
  }, [lessons, classId, termId]);

  return (
    <>
      <PageHeader title="Overview" subtitle="Whole-term topic map, by class" />

      <main className="mx-auto max-w-6xl space-y-4 p-4 lg:p-6">
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

          <label className="flex flex-col gap-1 text-sm font-semibold text-[color:var(--muted)]">
            Term
            <select className="field" value={termId} onChange={(e) => setTermId(e.target.value)}>
              {terms.map((t) => (
                <option key={t.id} value={t.id}>
                  {t.name}
                </option>
              ))}
            </select>
          </label>

          <p className="text-sm text-[color:var(--muted)]">
            {nodes.length} topic{nodes.length === 1 ? "" : "s"} mapped
          </p>
        </section>

        {loading ? (
          <p className="p-6 text-sm text-[color:var(--muted)]">Loading…</p>
        ) : (
          <MindMap
            centerTitle={info?.label ?? classId}
            centerSubtitle={term?.name}
            nodes={nodes}
            filename={`${(info?.label ?? classId).replace(/\s+/g, "-")}_${(term?.name ?? termId).replace(/\s+/g, "-")}_overview.pdf`}
          />
        )}
      </main>
    </>
  );
}
