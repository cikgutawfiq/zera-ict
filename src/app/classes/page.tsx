"use client";

import Link from "next/link";
import { useData } from "@/lib/store";
import { CLASSES, slotsForClass } from "@/data/timetable";
import { prettyTime } from "@/lib/dates";
import { PageHeader, ClassDot } from "@/components/ui";

const DAY_SHORT = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

export default function ClassesPage() {
  const { lessonsForClass } = useData();

  return (
    <>
      <PageHeader title="Classes" subtitle="27 periods a week across 11 classes" />
      <main className="mx-auto max-w-3xl space-y-3 p-4">
        {CLASSES.map((c) => {
          const lessons = lessonsForClass(c.id);
          const done = lessons.filter((l) => l.status === "done").length;
          const planned = lessons.filter((l) => l.topic).length;
          return (
            <Link key={c.id} href={`/class/${c.id}`} className="card block px-4 py-3.5">
              <p className="flex items-center gap-2 text-base font-bold">
                <ClassDot classId={c.id} />
                {c.label}
              </p>
              <p className="mt-1 text-sm text-[color:var(--muted)]">
                {c.subject} · {c.keyStage} · {c.periodsPerWeek} periods/week
              </p>
              <div className="mt-2 flex flex-wrap gap-1.5">
                {slotsForClass(c.id).map((s, i) => (
                  <span key={i} className="chip">
                    {DAY_SHORT[s.day]} {prettyTime(s.start)}
                  </span>
                ))}
                <span className="chip">
                  {planned}/{lessons.length} planned
                </span>
                {done > 0 && <span className="chip">{done} done</span>}
              </div>
            </Link>
          );
        })}
      </main>
    </>
  );
}
