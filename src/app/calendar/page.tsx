"use client";

import { Suspense, useEffect, useMemo, useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { useData } from "@/lib/store";
import { slotsForDay, CLASS_BY_ID, DAY_NAMES } from "@/data/timetable";
import {
  addDays,
  addMonths,
  daysInMonth,
  formatLong,
  formatMonthYear,
  formatRange,
  formatShort,
  fromISO,
  mondayOf,
  startOfMonth,
  todayISO,
} from "@/lib/dates";
import { PageHeader, SlotCard } from "@/components/ui";

type Mode = "day" | "week" | "month";
const MODES: { id: Mode; label: string }[] = [
  { id: "day", label: "Day" },
  { id: "week", label: "Week" },
  { id: "month", label: "Month" },
];
const WEEKDAY_LETTERS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

function SegmentedControl({ mode, onChange }: { mode: Mode; onChange: (m: Mode) => void }) {
  return (
    <div className="flex rounded-xl bg-[color:var(--surface-2)] p-1">
      {MODES.map((m) => (
        <button
          key={m.id}
          className="flex-1 rounded-lg py-1.5 text-sm font-semibold transition-all"
          style={{
            background: mode === m.id ? "var(--surface)" : "transparent",
            color: mode === m.id ? "var(--text)" : "var(--muted)",
            boxShadow: mode === m.id ? "var(--shadow)" : "none",
            transitionDuration: "var(--dur-fast)",
            transitionTimingFunction: "var(--ease)",
          }}
          onClick={() => onChange(m.id)}
        >
          {m.label}
        </button>
      ))}
    </div>
  );
}

export default function CalendarPage() {
  return (
    <Suspense fallback={null}>
      <CalendarPageInner />
    </Suspense>
  );
}

function CalendarPageInner() {
  const { lessonFor, terms } = useData();
  const router = useRouter();
  const params = useSearchParams();

  const [mode, setMode] = useState<Mode>("week");
  const [anchor, setAnchor] = useState(todayISO());

  useEffect(() => {
    const d = params.get("date");
    const m = params.get("mode") as Mode | null;
    if (d && /^\d{4}-\d{2}-\d{2}$/.test(d)) setAnchor(d);
    if (m && MODES.some((x) => x.id === m)) setMode(m);
  }, [params]);

  const findTermWeek = (dateIso: string) =>
    terms.flatMap((t) => t.weeks.map((w) => ({ term: t, week: w }))).find(
      (x) => dateIso >= x.week.start && dateIso <= x.week.end,
    );

  const goToday = () => setAnchor(todayISO());
  const step = (dir: 1 | -1) => {
    if (mode === "day") setAnchor((a) => addDays(a, dir));
    else if (mode === "week") setAnchor((a) => addDays(a, dir * 7));
    else setAnchor((a) => addMonths(a, dir));
  };
  const openDay = (iso: string) => {
    setAnchor(iso);
    setMode("day");
  };

  const title = useMemo(() => {
    if (mode === "day") return formatLong(anchor);
    if (mode === "month") return formatMonthYear(anchor);
    const tw = findTermWeek(mondayOf(anchor));
    return tw ? `${tw.term.name} · ${tw.week.label}` : "Week";
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [mode, anchor, terms]);

  const subtitle = useMemo(() => {
    if (mode === "day") return undefined;
    if (mode === "month") return undefined;
    const monday = mondayOf(anchor);
    return formatRange(monday, addDays(monday, 4));
  }, [mode, anchor]);

  return (
    <>
      <PageHeader
        title={title}
        subtitle={subtitle}
        right={
          <div className="flex items-center gap-1">
            <button className="btn btn-icon btn-sm" onClick={() => step(-1)} aria-label="Previous">
              ‹
            </button>
            <button className="btn btn-sm" onClick={goToday}>
              Today
            </button>
            <button className="btn btn-icon btn-sm" onClick={() => step(1)} aria-label="Next">
              ›
            </button>
          </div>
        }
      />

      <main className="mx-auto max-w-3xl space-y-4 p-4">
        <SegmentedControl
          mode={mode}
          onChange={(m) => {
            setMode(m);
            router.replace(`/calendar?date=${anchor}&mode=${m}`);
          }}
        />

        {mode === "day" && <DayView date={anchor} lessonFor={lessonFor} findTermWeek={findTermWeek} />}
        {mode === "week" && <WeekView monday={mondayOf(anchor)} lessonFor={lessonFor} findTermWeek={findTermWeek} />}
        {mode === "month" && <MonthView anchor={anchor} lessonFor={lessonFor} onPickDay={openDay} />}
      </main>
    </>
  );
}

function DayView({
  date,
  lessonFor,
  findTermWeek,
}: {
  date: string;
  lessonFor: ReturnType<typeof useData>["lessonFor"];
  findTermWeek: (iso: string) => { term: { name: string }; week: { label: string; remark: string; isBreak: boolean } } | undefined;
}) {
  const day = fromISO(date).getDay();
  const slots = slotsForDay(day);
  const tw = findTermWeek(date);

  return (
    <div className="space-y-3">
      {tw?.week.remark && (
        <p className="card whitespace-pre-line p-3 text-sm text-[color:var(--warn)]">{tw.week.remark}</p>
      )}
      {slots.length === 0 ? (
        <div className="card p-6 text-center">
          <p className="text-base font-semibold">No classes on {DAY_NAMES[day]}.</p>
          <p className="mt-1 text-sm text-[color:var(--muted)]">Enjoy the day off.</p>
        </div>
      ) : (
        slots.map((slot, i) => <SlotCard key={i} slot={slot} lesson={lessonFor(slot.classId, date)} />)
      )}
    </div>
  );
}

function WeekView({
  monday,
  lessonFor,
  findTermWeek,
}: {
  monday: string;
  lessonFor: ReturnType<typeof useData>["lessonFor"];
  findTermWeek: (iso: string) => { term: { name: string }; week: { label: string; remark: string; isBreak: boolean } } | undefined;
}) {
  const tw = findTermWeek(monday);
  return (
    <div className="space-y-5">
      {tw?.week.remark && (
        <p className="card whitespace-pre-line p-3 text-sm text-[color:var(--warn)]">{tw.week.remark}</p>
      )}
      {[1, 2, 3, 4, 5].map((day) => {
        const date = addDays(monday, day - 1);
        const slots = slotsForDay(day);
        return (
          <section key={day} className="space-y-2">
            <h2 className="px-1 text-base font-bold">
              {DAY_NAMES[day]}
              <span className="ml-2 text-sm font-normal text-[color:var(--muted)]">{formatShort(date)}</span>
            </h2>
            {slots.length === 0 ? (
              <p className="px-1 text-sm text-[color:var(--muted)]">No classes.</p>
            ) : (
              slots.map((slot, i) => <SlotCard key={i} slot={slot} lesson={lessonFor(slot.classId, date)} />)
            )}
          </section>
        );
      })}
    </div>
  );
}

function MonthView({
  anchor,
  lessonFor,
  onPickDay,
}: {
  anchor: string;
  lessonFor: ReturnType<typeof useData>["lessonFor"];
  onPickDay: (iso: string) => void;
}) {
  const first = startOfMonth(anchor);
  const total = daysInMonth(anchor);
  const firstWeekday = (fromISO(first).getDay() + 6) % 7; // 0=Mon
  const today = todayISO();

  const cells: (string | null)[] = [
    ...Array(firstWeekday).fill(null),
    ...Array.from({ length: total }, (_, i) => addDays(first, i)),
  ];
  while (cells.length % 7 !== 0) cells.push(null);

  return (
    <div className="card p-3">
      <div className="grid grid-cols-7 gap-1 text-center text-xs font-semibold text-[color:var(--muted)]">
        {WEEKDAY_LETTERS.map((d) => (
          <div key={d} className="py-1">
            {d}
          </div>
        ))}
      </div>
      <div className="mt-1 grid grid-cols-7 gap-1">
        {cells.map((iso, i) => {
          if (!iso) return <div key={i} />;
          const day = fromISO(iso).getDay();
          const slots = slotsForDay(day).filter((s) => !s.duty);
          const classIds = Array.from(new Set(slots.map((s) => s.classId))).slice(0, 4);
          const isToday = iso === today;
          return (
            <button
              key={i}
              onClick={() => onPickDay(iso)}
              className="flex aspect-square flex-col items-center justify-start gap-1 rounded-lg pt-1.5 transition-transform active:scale-95"
              style={{
                background: isToday ? "var(--accent-soft)" : "transparent",
                transitionDuration: "var(--dur-fast)",
                transitionTimingFunction: "var(--ease)",
              }}
            >
              <span
                className="text-sm font-semibold"
                style={{ color: isToday ? "var(--accent)" : "var(--text)" }}
              >
                {fromISO(iso).getDate()}
              </span>
              <span className="flex flex-wrap justify-center gap-0.5 px-0.5">
                {classIds.map((cid) => {
                  const has = lessonFor(cid, iso);
                  return (
                    <span
                      key={cid}
                      className="h-1.5 w-1.5 rounded-full"
                      style={{
                        background: CLASS_BY_ID[cid]?.color ?? "var(--muted)",
                        opacity: has ? 1 : 0.35,
                      }}
                    />
                  );
                })}
              </span>
            </button>
          );
        })}
      </div>
    </div>
  );
}
