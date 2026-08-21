"use client";

import Link from "next/link";
import type { Lesson, Status } from "@/lib/types";
import { CLASS_BY_ID, DUTIES, type Slot } from "@/data/timetable";
import { prettyTime } from "@/lib/dates";

export const STATUS_LABEL: Record<Status, string> = {
  planned: "Planned",
  done: "Done",
  "carried-over": "Carried over",
};

export function StatusChip({ status }: { status: Status }) {
  const color =
    status === "done" ? "var(--good)" : status === "carried-over" ? "var(--warn)" : "var(--muted)";
  return (
    <span className="chip" style={{ color, borderColor: color }}>
      {STATUS_LABEL[status]}
    </span>
  );
}

export function ClassDot({ classId }: { classId: string }) {
  const color = CLASS_BY_ID[classId]?.color ?? "var(--muted)";
  return <span className="inline-block h-2.5 w-2.5 rounded-full" style={{ background: color }} />;
}

export function PageHeader({
  title,
  subtitle,
  right,
}: {
  title: string;
  subtitle?: string;
  right?: React.ReactNode;
}) {
  return (
    <header className="blur-bar sticky top-0 z-10 border-b border-[color:var(--border)] px-4 py-3">
      <div className="mx-auto flex max-w-3xl items-center gap-3">
        <div className="min-w-0 flex-1">
          <h1 className="truncate text-base font-bold">{title}</h1>
          {subtitle && <p className="truncate text-xs text-[color:var(--muted)]">{subtitle}</p>}
        </div>
        {right}
      </div>
    </header>
  );
}

export function SlotCard({ slot, lesson }: { slot: Slot; lesson?: Lesson }) {
  const info = CLASS_BY_ID[slot.classId];
  const time = `${prettyTime(slot.start)} – ${prettyTime(slot.end)}`;

  if (slot.duty) {
    return (
      <div className="card flex items-center gap-3 px-4 py-3 opacity-80">
        <div className="w-[86px] shrink-0 text-xs font-semibold text-[color:var(--muted)]">{time}</div>
        <div className="min-w-0 flex-1">
          <p className="truncate text-sm font-semibold">{DUTIES[slot.classId] ?? slot.classId}</p>
          <p className="text-xs text-[color:var(--muted)]">Duty · {slot.periods}</p>
        </div>
      </div>
    );
  }

  const body = (
    <div className="card block px-4 py-3">
      <div className="flex items-start gap-3">
        <div className="w-[86px] shrink-0">
          <p className="text-xs font-semibold">{prettyTime(slot.start)}</p>
          <p className="text-[11px] text-[color:var(--muted)]">{prettyTime(slot.end)}</p>
        </div>
        <div className="min-w-0 flex-1">
          <p className="flex items-center gap-2 text-sm font-bold">
            <ClassDot classId={slot.classId} />
            <span className="truncate">{info?.label ?? slot.classId}</span>
          </p>
          {lesson ? (
            <>
              <p className="mt-0.5 truncate text-sm">{lesson.topic || "No topic set"}</p>
              {lesson.subtopic && (
                <p className="truncate text-xs text-[color:var(--muted)]">{lesson.subtopic}</p>
              )}
            </>
          ) : (
            <p className="mt-0.5 text-xs text-[color:var(--muted)]">No lesson for this week yet</p>
          )}
          <div className="mt-2 flex flex-wrap items-center gap-1.5">
            <span className="chip">{slot.periods}</span>
            {slot.room && <span className="chip">Room {slot.room}</span>}
            {lesson && <span className="chip">{lesson.weekLabel}</span>}
            {lesson && <StatusChip status={lesson.status} />}
          </div>
        </div>
      </div>
    </div>
  );

  return lesson ? (
    <Link href={`/lesson/${lesson.id}`} className="block">
      {body}
    </Link>
  ) : (
    body
  );
}
