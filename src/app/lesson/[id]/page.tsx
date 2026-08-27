"use client";

import Link from "next/link";
import { useParams, useRouter } from "next/navigation";
import { useState } from "react";
import { useData } from "@/lib/store";
import { CLASS_BY_ID, slotsForClass } from "@/data/timetable";
import { formatRange, prettyTime } from "@/lib/dates";
import { PageHeader, StatusChip, ClassDot } from "@/components/ui";
import {
  IceBreakerSection,
  ListSection,
  MoralSection,
  PlanSection,
  ResourceSection,
  TextSection,
} from "@/components/Editable";
import type { Lesson, Status } from "@/lib/types";
import { generateRubricPdf, generateWorksheetsPdf } from "@/lib/worksheets";
import { AlternativeTopicsSection } from "@/components/AlternativeTopics";

const DAY_SHORT = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

export default function LessonPage() {
  const { id } = useParams<{ id: string }>();
  const router = useRouter();
  const { lessonById, saveLesson, deleteLesson, loading } = useData();
  const [busy, setBusy] = useState(false);
  const [pdfBusy, setPdfBusy] = useState<"worksheets" | "rubric" | null>(null);
  const lesson = lessonById(id);

  if (loading) return <p className="p-6 text-sm text-[color:var(--muted)]">Loading…</p>;

  if (!lesson) {
    return (
      <main className="p-6">
        <p className="text-sm">Lesson not found.</p>
        <Link href="/" className="btn mt-4">
          Back to Today
        </Link>
      </main>
    );
  }

  const info = CLASS_BY_ID[lesson.classId];
  const slots = slotsForClass(lesson.classId);
  const patch = (p: Partial<Lesson>) => saveLesson(lesson.id, p);

  const downloadWorksheets = async () => {
    setPdfBusy("worksheets");
    try {
      generateWorksheetsPdf(lesson, info);
    } finally {
      setPdfBusy(null);
    }
  };

  const downloadRubric = async () => {
    setPdfBusy("rubric");
    try {
      generateRubricPdf(lesson, info);
    } finally {
      setPdfBusy(null);
    }
  };

  const setStatus = async (status: Status) => {
    setBusy(true);
    try {
      await patch({ status });
    } finally {
      setBusy(false);
    }
  };

  const remove = async () => {
    if (!confirm(`Delete ${info?.label} ${lesson.weekLabel}? This cannot be undone.`)) return;
    setBusy(true);
    try {
      await deleteLesson(lesson.id);
      router.push(`/class/${lesson.classId}`);
    } finally {
      setBusy(false);
    }
  };

  return (
    <>
      <PageHeader
        back
        backHref={`/class/${lesson.classId}`}
        title={`${info?.label ?? lesson.classId} · ${lesson.weekLabel}`}
        subtitle={`${formatRange(lesson.dateStart, lesson.dateEnd)} · ${lesson.topic || "No topic"}`}
        right={
          <Link href={`/lesson/${lesson.id}/present`} className="btn btn-sm btn-primary">
            Present
          </Link>
        }
      />

      <main className="mx-auto flex max-w-6xl flex-col gap-4 p-4 lg:grid lg:grid-cols-[1fr_20rem] lg:items-start lg:p-6">
        <div className="order-2 space-y-3 lg:order-1">
          <div className="grid grid-cols-2 gap-3">
            <TextSection title="Topic" value={lesson.topic} multiline={false} onSave={(topic) => patch({ topic })} />
            <TextSection
              title="Subtopic"
              value={lesson.subtopic}
              multiline={false}
              onSave={(subtopic) => patch({ subtopic })}
            />
          </div>

          <AlternativeTopicsSection
            subject={info?.subject ?? lesson.subject}
            keyStage={info?.keyStage ?? "KS2"}
            currentTopic={lesson.topic}
            onSwap={(next) => patch(next)}
          />

          <ListSection
            title="Learning objectives"
            items={lesson.objectives}
            onSave={(objectives) => patch({ objectives })}
          />
          <PlanSection steps={lesson.plan} onSave={(plan) => patch({ plan })} />
          <ListSection
            title="Recommended activities"
            items={lesson.activities}
            onSave={(activities) => patch({ activities })}
          />
          <ListSection
            title="Success criteria"
            items={lesson.successCriteria}
            onSave={(successCriteria) => patch({ successCriteria })}
          />
          <ResourceSection items={lesson.resources} onSave={(resources) => patch({ resources })} />

          <section className="card p-4">
            <h2 className="mb-1 text-[15px] font-bold uppercase tracking-wide text-[color:var(--muted)]">
              Worksheets &amp; assessment
            </h2>
            <p className="mb-3 text-sm text-[color:var(--muted)]">
              Printable PDFs built from this lesson&rsquo;s topic, objectives, activities and success
              criteria — for cover lessons or independent work.
            </p>
            <div className="no-print flex flex-wrap gap-2">
              <button className="btn btn-sm btn-primary" disabled={pdfBusy !== null} onClick={downloadWorksheets}>
                {pdfBusy === "worksheets" ? "Generating…" : "📄 3 worksheets (Foundation / Core / Challenge)"}
              </button>
              <button className="btn btn-sm" disabled={pdfBusy !== null} onClick={downloadRubric}>
                {pdfBusy === "rubric" ? "Generating…" : "📊 Assessment rubric"}
              </button>
            </div>
          </section>

          <TextSection
            title="Reflection"
            value={lesson.note}
            placeholder="How did it go? Where did you stop? What to pick up next week?"
            onSave={(note) => patch({ note })}
          />

          <div className="no-print pt-2 pb-4">
            <button className="btn btn-sm w-full" style={{ color: "var(--warn)" }} disabled={busy} onClick={remove}>
              Delete this lesson
            </button>
          </div>
        </div>

        <div className="order-1 space-y-3 lg:sticky lg:top-20 lg:order-2">
          <div className="card p-4">
            <div className="flex flex-wrap items-center gap-1.5">
              <span className="chip">
                <ClassDot classId={lesson.classId} /> {info?.subject ?? lesson.subject}
              </span>
              {slots.map((s, i) => (
                <span key={i} className="chip">
                  {DAY_SHORT[s.day]} {prettyTime(s.start)}–{prettyTime(s.end)} · {s.periods}
                </span>
              ))}
              <StatusChip status={lesson.status} />
            </div>

            <div className="mt-3 flex flex-wrap gap-2">
              <button
                className={`btn btn-sm ${lesson.status === "done" ? "btn-primary" : ""}`}
                disabled={busy}
                onClick={() => setStatus(lesson.status === "done" ? "planned" : "done")}
              >
                ✓ Done
              </button>
              <button
                className={`btn btn-sm ${lesson.status === "carried-over" ? "btn-primary" : ""}`}
                disabled={busy}
                onClick={() => setStatus(lesson.status === "carried-over" ? "planned" : "carried-over")}
              >
                → Carried over
              </button>
              <Link href={`/class/${lesson.classId}`} className="btn btn-sm">
                All {info?.label} weeks
              </Link>
            </div>

            {lesson.remark && (
              <p className="mt-3 whitespace-pre-line rounded-lg bg-[color:var(--surface-2)] p-3 text-sm text-[color:var(--warn)]">
                {lesson.remark}
              </p>
            )}
          </div>

          <MoralSection
            moralValue={lesson.moralValue}
            moralDescription={lesson.moralDescription}
            quote={lesson.quote}
            quoteAuthor={lesson.quoteAuthor}
            foodForThought={lesson.foodForThought}
            onSave={(next) => patch(next)}
          />

          <IceBreakerSection
            title={lesson.iceBreakerTitle}
            description={lesson.iceBreakerDescription}
            minutes={lesson.iceBreakerMinutes}
            keyStage={info?.keyStage ?? "KS2"}
            onSave={(next) => patch(next)}
          />
        </div>
      </main>
    </>
  );
}
