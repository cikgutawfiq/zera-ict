"use client";

import { useState } from "react";
import { useData } from "@/lib/store";
import { slotsForDay, DAY_NAMES } from "@/data/timetable";
import { addDays, formatRange, formatShort, mondayOf, todayISO } from "@/lib/dates";
import { PageHeader, SlotCard } from "@/components/ui";

const DAYS = [1, 2, 3, 4, 5] as const;

export default function WeekPage() {
  const { lessonFor, terms } = useData();
  const [monday, setMonday] = useState(mondayOf(todayISO()));

  const termWeek = terms
    .flatMap((t) => t.weeks.map((w) => ({ term: t, week: w })))
    .find((x) => monday >= x.week.start && monday <= x.week.end);

  return (
    <>
      <PageHeader
        title={termWeek ? `${termWeek.term.name} · ${termWeek.week.label}` : "Week"}
        subtitle={formatRange(monday, addDays(monday, 4))}
        right={
          <div className="flex items-center gap-1">
            <button className="btn btn-sm" onClick={() => setMonday(addDays(monday, -7))} aria-label="Previous week">
              ‹
            </button>
            <button className="btn btn-sm" onClick={() => setMonday(mondayOf(todayISO()))}>
              This week
            </button>
            <button className="btn btn-sm" onClick={() => setMonday(addDays(monday, 7))} aria-label="Next week">
              ›
            </button>
          </div>
        }
      />

      <main className="mx-auto max-w-3xl space-y-5 p-4">
        {termWeek?.week.remark && (
          <p className="card whitespace-pre-line p-3 text-xs text-[color:var(--warn)]">{termWeek.week.remark}</p>
        )}
        {DAYS.map((day) => {
          const date = addDays(monday, day - 1);
          const slots = slotsForDay(day);
          return (
            <section key={day} className="space-y-2">
              <h2 className="px-1 text-sm font-bold">
                {DAY_NAMES[day]}
                <span className="ml-2 text-xs font-normal text-[color:var(--muted)]">{formatShort(date)}</span>
              </h2>
              {slots.length === 0 ? (
                <p className="px-1 text-xs text-[color:var(--muted)]">No classes.</p>
              ) : (
                slots.map((slot, i) => (
                  <SlotCard key={i} slot={slot} lesson={lessonFor(slot.classId, date)} />
                ))
              )}
            </section>
          );
        })}
      </main>
    </>
  );
}
