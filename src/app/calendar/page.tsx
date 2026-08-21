"use client";

import { useState } from "react";
import { useData } from "@/lib/store";
import { slotsForDay, DAY_NAMES } from "@/data/timetable";
import { addDays, formatRange, formatShort, mondayOf, todayISO } from "@/lib/dates";
import { PageHeader, SlotCard } from "@/components/ui";

const DAYS = [1, 2, 3, 4, 5] as const;

export default function ThisWeekPage() {
  const { lessonFor, terms } = useData();
  const [monday, setMonday] = useState(mondayOf(todayISO()));

  const termWeek = terms
    .flatMap((t) => t.weeks.map((w) => ({ term: t, week: w })))
    .find((x) => monday >= x.week.start && monday <= x.week.end);

  return (
    <>
      <PageHeader
        title={termWeek ? `${termWeek.term.name} · ${termWeek.week.label}` : "This week"}
        subtitle={formatRange(monday, addDays(monday, 4))}
        right={
          <div className="flex items-center gap-1">
            <button className="btn btn-icon btn-sm" onClick={() => setMonday(addDays(monday, -7))} aria-label="Previous week">
              ‹
            </button>
            <button className="btn btn-sm" onClick={() => setMonday(mondayOf(todayISO()))}>
              Today
            </button>
            <button className="btn btn-icon btn-sm" onClick={() => setMonday(addDays(monday, 7))} aria-label="Next week">
              ›
            </button>
          </div>
        }
      />

      <main className="mx-auto max-w-7xl space-y-5 p-4 lg:p-6">
        {termWeek?.week.remark && (
          <p className="card whitespace-pre-line p-3 text-sm text-[color:var(--warn)]">{termWeek.week.remark}</p>
        )}
        <div className="grid grid-cols-1 gap-5 lg:grid-cols-5 lg:items-start lg:gap-4">
          {DAYS.map((day) => {
            const date = addDays(monday, day - 1);
            const slots = slotsForDay(day);
            const isToday = date === todayISO();
            return (
              <section key={day} className="space-y-2">
                <h2
                  className="px-1 text-base font-bold lg:sticky lg:top-16 lg:z-[1] lg:rounded-lg lg:px-2 lg:py-1.5"
                  style={isToday ? { background: "var(--accent-soft)", color: "var(--accent)" } : undefined}
                >
                  {DAY_NAMES[day]}
                  <span className="ml-2 text-sm font-normal text-[color:var(--muted)]">{formatShort(date)}</span>
                </h2>
                {slots.length === 0 ? (
                  <p className="px-1 text-sm text-[color:var(--muted)]">No classes.</p>
                ) : (
                  <div className="space-y-2">
                    {slots.map((slot, i) => (
                      <SlotCard key={i} slot={slot} lesson={lessonFor(slot.classId, date)} />
                    ))}
                  </div>
                )}
              </section>
            );
          })}
        </div>
      </main>
    </>
  );
}
