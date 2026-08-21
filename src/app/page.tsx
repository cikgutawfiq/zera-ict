"use client";

import { useEffect, useMemo, useState } from "react";
import { useData } from "@/lib/store";
import { slotsForDay, DAY_NAMES } from "@/data/timetable";
import { addDays, formatLong, mondayOf, todayISO } from "@/lib/dates";
import { PageHeader, SlotCard } from "@/components/ui";

export default function TodayPage() {
  const { lessonFor, terms, loading } = useData();
  const [date, setDate] = useState(todayISO());

  // Deep link support: /?date=2026-09-01 opens that day directly.
  useEffect(() => {
    const wanted = new URLSearchParams(window.location.search).get("date");
    if (wanted && /^\d{4}-\d{2}-\d{2}$/.test(wanted)) setDate(wanted);
  }, []);

  const day = new Date(date + "T00:00:00").getDay();
  const slots = useMemo(() => slotsForDay(day), [day]);

  const week = useMemo(() => {
    for (const term of terms) {
      const hit = term.weeks.find((w) => date >= w.start && date <= w.end);
      if (hit) return { term, week: hit };
    }
    return null;
  }, [terms, date]);

  const isToday = date === todayISO();

  return (
    <>
      <PageHeader
        title={isToday ? "Today" : DAY_NAMES[day]}
        subtitle={formatLong(date)}
        right={
          <div className="flex items-center gap-1">
            <button className="btn btn-sm" onClick={() => setDate(addDays(date, -1))} aria-label="Previous day">
              ‹
            </button>
            <button className="btn btn-sm" onClick={() => setDate(todayISO())}>
              Today
            </button>
            <button className="btn btn-sm" onClick={() => setDate(addDays(date, 1))} aria-label="Next day">
              ›
            </button>
          </div>
        }
      />

      <main className="mx-auto max-w-3xl space-y-3 p-4">
        {week && (
          <div className="card px-4 py-3">
            <p className="text-sm font-semibold">
              {week.term.name} · {week.week.label}
              {week.week.isExam && " · Examination Week"}
            </p>
            <p className="text-xs text-[color:var(--muted)]">
              Week of {formatLong(mondayOf(date))}
              {week.week.isBreak && " · Mid-term break"}
            </p>
            {week.week.remark && (
              <p className="mt-2 whitespace-pre-line text-xs text-[color:var(--warn)]">{week.week.remark}</p>
            )}
          </div>
        )}

        {loading && <p className="p-4 text-sm text-[color:var(--muted)]">Loading lessons…</p>}

        {!loading && slots.length === 0 && (
          <div className="card p-6 text-center">
            <p className="text-sm font-semibold">No classes on {DAY_NAMES[day]}.</p>
            <p className="mt-1 text-xs text-[color:var(--muted)]">Enjoy the day off.</p>
          </div>
        )}

        {slots.map((slot, i) => (
          <SlotCard key={`${slot.day}-${slot.start}-${i}`} slot={slot} lesson={lessonFor(slot.classId, date)} />
        ))}

        {!loading && week?.week.isBreak && slots.length > 0 && (
          <p className="px-1 text-xs text-[color:var(--muted)]">
            This week is a scheduled break — lessons above are shown for reference only.
          </p>
        )}
      </main>
    </>
  );
}
