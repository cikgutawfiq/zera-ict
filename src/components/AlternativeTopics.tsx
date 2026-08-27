"use client";

import { useState } from "react";
import { pickAlternativeTopics, type AltTopic } from "@/data/altTopics";

export function AlternativeTopicsSection({
  subject,
  keyStage,
  currentTopic,
  onSwap,
}: {
  subject: string;
  keyStage: string;
  currentTopic: string;
  onSwap: (next: { topic: string; subtopic: string }) => Promise<void>;
}) {
  const [suggestions, setSuggestions] = useState<AltTopic[]>(() =>
    pickAlternativeTopics(subject, keyStage, currentTopic, 3),
  );
  const [busyIdx, setBusyIdx] = useState<number | null>(null);

  const reroll = () => setSuggestions(pickAlternativeTopics(subject, keyStage, currentTopic, 3));

  const swap = async (idx: number) => {
    const s = suggestions[idx];
    setBusyIdx(idx);
    try {
      await onSwap({ topic: s.title, subtopic: s.description });
    } finally {
      setBusyIdx(null);
    }
  };

  if (suggestions.length === 0) return null;

  return (
    <section className="card no-print p-4">
      <div className="mb-1 flex items-center gap-2">
        <h2 className="flex-1 text-[15px] font-bold uppercase tracking-wide text-[color:var(--muted)]">
          Not feeling this topic?
        </h2>
        <button className="btn btn-sm" onClick={reroll}>
          🔀 Show different ones
        </button>
      </div>
      <p className="mb-3 text-sm text-[color:var(--muted)]">
        3 alternative {subject} ideas for this level. Swapping updates the topic &amp; subtopic — you&rsquo;ll still
        want to adjust the objectives, plan and activities below to match.
      </p>
      <div className="grid gap-3 sm:grid-cols-3">
        {suggestions.map((s, i) => (
          <div key={s.title} className="rounded-lg border border-[color:var(--border)] p-3">
            <p className="text-base font-bold">{s.title}</p>
            <p className="mt-1 text-sm text-[color:var(--muted)]">{s.description}</p>
            <button
              className="btn btn-sm btn-primary mt-3 w-full"
              disabled={busyIdx !== null}
              onClick={() => swap(i)}
            >
              {busyIdx === i ? "Swapping…" : "Use this topic"}
            </button>
          </div>
        ))}
      </div>
    </section>
  );
}
