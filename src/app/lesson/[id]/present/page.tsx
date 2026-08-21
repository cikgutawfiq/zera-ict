"use client";

import { useRouter, useParams } from "next/navigation";
import { useCallback, useEffect, useMemo, useState } from "react";
import { useData } from "@/lib/store";
import { CLASS_BY_ID } from "@/data/timetable";
import type { Lesson } from "@/lib/types";

type Card = { heading: string; bullets: string[]; steps?: Lesson["plan"]; moral?: Lesson; iceBreaker?: Lesson };

function buildCards(lesson: Lesson): Card[] {
  const cards: Card[] = [];
  if (lesson.moralValue) cards.push({ heading: "Value of the day", bullets: [], moral: lesson });
  if (lesson.iceBreakerTitle)
    cards.push({ heading: `Ice breaker · ${lesson.iceBreakerMinutes} min`, bullets: [], iceBreaker: lesson });
  if (lesson.objectives.length) cards.push({ heading: "Learning objectives", bullets: lesson.objectives });
  if (lesson.plan.length) cards.push({ heading: "Lesson plan", bullets: [], steps: lesson.plan });
  if (lesson.activities.length) cards.push({ heading: "Activities", bullets: lesson.activities });
  if (lesson.successCriteria.length) cards.push({ heading: "Success criteria", bullets: lesson.successCriteria });
  if (lesson.resources.length)
    cards.push({ heading: "Resources", bullets: lesson.resources.map((r) => r.label) });
  if (!cards.length) cards.push({ heading: "No content yet", bullets: ["Add objectives and a plan first."] });
  return cards;
}

export default function PresentPage() {
  const { id } = useParams<{ id: string }>();
  const router = useRouter();
  const { lessonById, loading } = useData();
  const lesson = lessonById(id);
  const [index, setIndex] = useState(0);

  const cards = useMemo(() => (lesson ? buildCards(lesson) : []), [lesson]);
  const next = useCallback(() => setIndex((i) => Math.min(i + 1, cards.length - 1)), [cards.length]);
  const prev = useCallback(() => setIndex((i) => Math.max(i - 1, 0)), []);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "ArrowRight" || e.key === " ") next();
      if (e.key === "ArrowLeft") prev();
      if (e.key === "Escape") router.push(`/lesson/${id}`);
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [next, prev, router, id]);

  useEffect(() => {
    let sentinel: { release: () => Promise<void> } | null = null;
    const nav = navigator as Navigator & {
      wakeLock?: { request: (type: "screen") => Promise<{ release: () => Promise<void> }> };
    };
    nav.wakeLock?.request("screen").then((s) => (sentinel = s)).catch(() => {});
    return () => {
      sentinel?.release().catch(() => {});
    };
  }, []);

  if (loading) return <p className="p-6 text-sm">Loading…</p>;
  if (!lesson) return <p className="p-6 text-sm">Lesson not found.</p>;

  const info = CLASS_BY_ID[lesson.classId];
  const card = cards[index];

  return (
    <div className="flex min-h-screen flex-col bg-[color:var(--bg)]">
      <header className="flex items-center gap-3 border-b border-[color:var(--border)] px-4 py-3">
        <div className="min-w-0 flex-1">
          <p className="truncate text-sm font-bold">
            {info?.label} · {lesson.weekLabel}
          </p>
          <p className="truncate text-xs text-[color:var(--muted)]">
            {lesson.topic}
            {lesson.subtopic ? ` — ${lesson.subtopic}` : ""}
          </p>
        </div>
        <button className="btn btn-sm" onClick={() => router.push(`/lesson/${lesson.id}`)}>
          Exit
        </button>
      </header>

      <main className="flex-1 px-5 py-6">
        <h2 className="text-xs font-bold uppercase tracking-widest text-[color:var(--accent)]">{card.heading}</h2>
        {card.moral ? (
          <div className="mt-6 space-y-6">
            <p className="text-3xl font-extrabold">{card.moral.moralValue}</p>
            <p className="text-lg text-[color:var(--muted)]">{card.moral.moralDescription}</p>
            <blockquote className="text-2xl italic leading-snug">
              <span className="text-4xl not-italic text-[color:var(--accent)] leading-none align-top">&ldquo;</span>
              {card.moral.quote}
              <span className="text-4xl not-italic text-[color:var(--accent)] leading-none align-bottom">&rdquo;</span>
              <footer className="mt-2 text-base not-italic text-[color:var(--muted)]">— {card.moral.quoteAuthor}</footer>
            </blockquote>
            <p className="text-lg font-medium">
              <span className="text-[color:var(--accent)]">Food for thought: </span>
              {card.moral.foodForThought}
            </p>
          </div>
        ) : card.iceBreaker ? (
          <div className="mt-6 space-y-4">
            <p className="text-3xl font-extrabold">🧊 {card.iceBreaker.iceBreakerTitle}</p>
            <p className="text-xl leading-relaxed text-[color:var(--muted)]">
              {card.iceBreaker.iceBreakerDescription}
            </p>
          </div>
        ) : card.steps ? (
          <ol className="mt-5 space-y-5">
            {card.steps.map((step, i) => (
              <li key={i}>
                <p className="text-xl font-bold leading-snug">
                  <span className="text-[color:var(--accent)]">{step.mins} min</span> · {step.title}
                </p>
                <p className="mt-1 text-lg leading-relaxed text-[color:var(--muted)]">{step.detail}</p>
              </li>
            ))}
          </ol>
        ) : (
          <ul className="mt-5 space-y-4">
            {card.bullets.map((b, i) => (
              <li key={i} className="flex gap-3 text-xl font-medium leading-snug">
                <span className="text-[color:var(--accent)]">•</span>
                <span>{b}</span>
              </li>
            ))}
          </ul>
        )}
      </main>

      <footer className="sticky bottom-0 flex items-center gap-3 border-t border-[color:var(--border)] bg-[color:var(--surface)] px-4 py-3">
        <button className="btn flex-1" onClick={prev} disabled={index === 0}>
          ‹ Back
        </button>
        <span className="text-xs font-semibold text-[color:var(--muted)]">
          {index + 1} / {cards.length}
        </span>
        <button className="btn btn-primary flex-1" onClick={next} disabled={index === cards.length - 1}>
          Next ›
        </button>
      </footer>
    </div>
  );
}
