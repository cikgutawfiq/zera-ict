"use client";

import Link from "next/link";
import { useParams } from "next/navigation";
import { useState } from "react";
import { useData } from "@/lib/store";
import { CLASS_BY_ID, slotsForClass } from "@/data/timetable";
import { addDays, formatRange, mondayOf, todayISO } from "@/lib/dates";
import { PageHeader, StatusChip } from "@/components/ui";
import { assignMoralContent } from "@/data/values";
import type { Lesson } from "@/lib/types";

const DAY_SHORT = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

export default function ClassPage() {
  const { classId } = useParams<{ classId: string }>();
  const { lessonsForClass, terms, createLesson, loading } = useData();
  const [adding, setAdding] = useState(false);
  const [busy, setBusy] = useState(false);

  const info = CLASS_BY_ID[classId];
  const lessons = lessonsForClass(classId);

  const defaultTerm = terms[0]?.id ?? "term-1";
  const nextWeek = Math.max(0, ...lessons.filter((l) => l.termId === defaultTerm).map((l) => l.weekNo)) + 1;
  const [termId, setTermId] = useState(defaultTerm);
  const [weekNo, setWeekNo] = useState(String(nextWeek));
  const [start, setStart] = useState(mondayOf(todayISO()));
  const [topic, setTopic] = useState("");

  const add = async () => {
    const no = Number.parseInt(weekNo, 10);
    if (!no || !start) return;
    const id = `${classId}_${termId}_w${no}`;
    if (lessons.some((l) => l.id === id)) {
      alert(`Week ${no} already exists for this class in that term.`);
      return;
    }
    const moral = assignMoralContent(classId, lessons.length);
    const lesson: Lesson = {
      id,
      classId,
      subject: info?.subject ?? "",
      termId,
      weekNo: no,
      weekLabel: `Week ${no}`,
      dateStart: start,
      dateEnd: addDays(start, 4),
      topic,
      subtopic: "",
      outline: "",
      sowResources: "",
      remark: "",
      objectives: [],
      plan: [],
      activities: [],
      successCriteria: [],
      resources: [],
      ...moral,
      status: "planned",
      note: "",
      order: no,
    };
    setBusy(true);
    try {
      await createLesson(lesson);
      setAdding(false);
      setTopic("");
      setWeekNo(String(no + 1));
    } finally {
      setBusy(false);
    }
  };

  const byTerm = terms.length
    ? terms.map((t) => ({ term: t.name, id: t.id, items: lessons.filter((l) => l.termId === t.id) }))
    : [{ term: "Lessons", id: "all", items: lessons }];
  const orphans = lessons.filter((l) => !terms.some((t) => t.id === l.termId));

  return (
    <>
      <PageHeader
        title={info?.label ?? classId}
        subtitle={
          info
            ? `${info.subject} · ${slotsForClass(classId)
                .map((s) => DAY_SHORT[s.day])
                .join(", ")}`
            : undefined
        }
        right={
          <button className="btn btn-sm btn-primary" onClick={() => setAdding((v) => !v)}>
            {adding ? "Close" : "+ Week"}
          </button>
        }
      />

      <main className="mx-auto max-w-3xl space-y-3 p-4">
        {adding && (
          <div className="card space-y-3 p-4">
            <h2 className="text-sm font-bold">Add a week</h2>
            <label className="block text-xs font-semibold text-[color:var(--muted)]">
              Term
              <select className="field mt-1" value={termId} onChange={(e) => setTermId(e.target.value)}>
                {terms.map((t) => (
                  <option key={t.id} value={t.id}>
                    {t.name}
                  </option>
                ))}
                {terms.length === 0 && <option value="term-1">Term 1</option>}
              </select>
            </label>
            <div className="flex gap-3">
              <label className="flex-1 text-xs font-semibold text-[color:var(--muted)]">
                Week number
                <input
                  className="field mt-1"
                  inputMode="numeric"
                  value={weekNo}
                  onChange={(e) => setWeekNo(e.target.value)}
                />
              </label>
              <label className="flex-1 text-xs font-semibold text-[color:var(--muted)]">
                Week starting (Mon)
                <input
                  className="field mt-1"
                  type="date"
                  value={start}
                  onChange={(e) => setStart(mondayOf(e.target.value))}
                />
              </label>
            </div>
            <label className="block text-xs font-semibold text-[color:var(--muted)]">
              Topic (optional)
              <input className="field mt-1" value={topic} onChange={(e) => setTopic(e.target.value)} />
            </label>
            <button className="btn btn-primary w-full" onClick={add} disabled={busy}>
              {busy ? "Adding…" : "Add week"}
            </button>
          </div>
        )}

        {loading && <p className="text-sm text-[color:var(--muted)]">Loading…</p>}

        {byTerm.map((group) => (
          <section key={group.id} className="space-y-2">
            {terms.length > 0 && <h2 className="px-1 pt-2 text-sm font-bold">{group.term}</h2>}
            {group.items.length === 0 && (
              <p className="px-1 text-xs text-[color:var(--muted)]">No lessons in this term yet.</p>
            )}
            {group.items.map((lesson) => (
              <Link key={lesson.id} href={`/lesson/${lesson.id}`} className="card block px-4 py-3">
                <div className="flex items-start gap-3">
                  <div className="w-16 shrink-0">
                    <p className="text-xs font-bold">{lesson.weekLabel}</p>
                    <p className="text-[11px] text-[color:var(--muted)]">
                      {formatRange(lesson.dateStart, lesson.dateEnd)}
                    </p>
                  </div>
                  <div className="min-w-0 flex-1">
                    <p className="truncate text-sm font-semibold">{lesson.topic || "Not planned yet"}</p>
                    {lesson.subtopic && (
                      <p className="truncate text-xs text-[color:var(--muted)]">{lesson.subtopic}</p>
                    )}
                    <div className="mt-1.5 flex flex-wrap gap-1.5">
                      <StatusChip status={lesson.status} />
                      {lesson.objectives.length > 0 && (
                        <span className="chip">{lesson.objectives.length} objectives</span>
                      )}
                      {lesson.note && <span className="chip">note</span>}
                    </div>
                  </div>
                </div>
              </Link>
            ))}
          </section>
        ))}

        {terms.length > 0 && orphans.length > 0 && (
          <p className="px-1 text-xs text-[color:var(--muted)]">
            {orphans.length} lesson(s) belong to a term that no longer exists.
          </p>
        )}
      </main>
    </>
  );
}
