"use client";

import { useState } from "react";
import type { PlanStep, ResourceLink } from "@/lib/types";

function Section({
  title,
  hint,
  editing,
  onEdit,
  onCancel,
  onSave,
  children,
  saving,
}: {
  title: string;
  hint?: string;
  editing: boolean;
  onEdit: () => void;
  onCancel: () => void;
  onSave: () => void;
  children: React.ReactNode;
  saving: boolean;
}) {
  return (
    <section className="card p-4">
      <div className="mb-2 flex items-center gap-2">
        <h2 className="flex-1 text-sm font-bold uppercase tracking-wide text-[color:var(--muted)]">{title}</h2>
        {editing ? (
          <>
            <button className="btn btn-sm" onClick={onCancel} disabled={saving}>
              Cancel
            </button>
            <button className="btn btn-sm btn-primary" onClick={onSave} disabled={saving}>
              {saving ? "Saving…" : "Save"}
            </button>
          </>
        ) : (
          <button className="btn btn-sm no-print" onClick={onEdit}>
            Edit
          </button>
        )}
      </div>
      {editing && hint && <p className="mb-2 text-xs text-[color:var(--muted)]">{hint}</p>}
      {children}
    </section>
  );
}

export function TextSection({
  title,
  value,
  onSave,
  multiline = true,
  placeholder = "Nothing here yet.",
}: {
  title: string;
  value: string;
  onSave: (next: string) => Promise<void>;
  multiline?: boolean;
  placeholder?: string;
}) {
  const [editing, setEditing] = useState(false);
  const [draft, setDraft] = useState(value);
  const [saving, setSaving] = useState(false);

  const save = async () => {
    setSaving(true);
    try {
      await onSave(draft);
      setEditing(false);
    } finally {
      setSaving(false);
    }
  };

  return (
    <Section
      title={title}
      editing={editing}
      saving={saving}
      onEdit={() => {
        setDraft(value);
        setEditing(true);
      }}
      onCancel={() => setEditing(false)}
      onSave={save}
    >
      {editing ? (
        multiline ? (
          <textarea className="field min-h-28" value={draft} onChange={(e) => setDraft(e.target.value)} />
        ) : (
          <input className="field" value={draft} onChange={(e) => setDraft(e.target.value)} />
        )
      ) : value ? (
        <p className="whitespace-pre-line text-[15px] leading-relaxed">{value}</p>
      ) : (
        <p className="text-sm text-[color:var(--muted)]">{placeholder}</p>
      )}
    </Section>
  );
}

export function ListSection({
  title,
  items,
  onSave,
  ordered = false,
}: {
  title: string;
  items: string[];
  onSave: (next: string[]) => Promise<void>;
  ordered?: boolean;
}) {
  const [editing, setEditing] = useState(false);
  const [draft, setDraft] = useState(items.join("\n"));
  const [saving, setSaving] = useState(false);

  const save = async () => {
    setSaving(true);
    try {
      await onSave(
        draft
          .split("\n")
          .map((s) => s.trim())
          .filter(Boolean),
      );
      setEditing(false);
    } finally {
      setSaving(false);
    }
  };

  const List = ordered ? "ol" : "ul";

  return (
    <Section
      title={title}
      hint="One item per line."
      editing={editing}
      saving={saving}
      onEdit={() => {
        setDraft(items.join("\n"));
        setEditing(true);
      }}
      onCancel={() => setEditing(false)}
      onSave={save}
    >
      {editing ? (
        <textarea className="field min-h-32" value={draft} onChange={(e) => setDraft(e.target.value)} />
      ) : items.length ? (
        <List className={`space-y-1.5 pl-5 text-[15px] leading-relaxed ${ordered ? "list-decimal" : "list-disc"}`}>
          {items.map((item, i) => (
            <li key={i}>{item}</li>
          ))}
        </List>
      ) : (
        <p className="text-sm text-[color:var(--muted)]">Nothing here yet — tap Edit to add.</p>
      )}
    </Section>
  );
}

const planToText = (steps: PlanStep[]) =>
  steps.map((s) => `${s.mins} | ${s.title} | ${s.detail}`).join("\n");

const textToPlan = (text: string): PlanStep[] =>
  text
    .split("\n")
    .map((line) => line.trim())
    .filter(Boolean)
    .map((line) => {
      const [mins, title, ...rest] = line.split("|");
      return {
        mins: Number.parseInt(mins?.trim() ?? "", 10) || 0,
        title: (title ?? "").trim(),
        detail: rest.join("|").trim(),
      };
    });

export function PlanSection({
  steps,
  onSave,
}: {
  steps: PlanStep[];
  onSave: (next: PlanStep[]) => Promise<void>;
}) {
  const [editing, setEditing] = useState(false);
  const [draft, setDraft] = useState(planToText(steps));
  const [saving, setSaving] = useState(false);
  const total = steps.reduce((sum, s) => sum + s.mins, 0);

  const save = async () => {
    setSaving(true);
    try {
      await onSave(textToPlan(draft));
      setEditing(false);
    } finally {
      setSaving(false);
    }
  };

  return (
    <Section
      title={`Lesson plan${total ? ` · ${total} min` : ""}`}
      hint="One step per line, as: minutes | title | what happens"
      editing={editing}
      saving={saving}
      onEdit={() => {
        setDraft(planToText(steps));
        setEditing(true);
      }}
      onCancel={() => setEditing(false)}
      onSave={save}
    >
      {editing ? (
        <textarea className="field min-h-48" value={draft} onChange={(e) => setDraft(e.target.value)} />
      ) : steps.length ? (
        <ol className="space-y-3">
          {steps.map((step, i) => (
            <li key={i} className="flex gap-3">
              <span className="mt-0.5 w-14 shrink-0 rounded-md bg-[color:var(--accent-soft)] px-2 py-1 text-center text-xs font-bold text-[color:var(--accent)]">
                {step.mins} min
              </span>
              <div className="min-w-0">
                <p className="text-[15px] font-semibold">{step.title}</p>
                <p className="text-[15px] leading-relaxed text-[color:var(--muted)]">{step.detail}</p>
              </div>
            </li>
          ))}
        </ol>
      ) : (
        <p className="text-sm text-[color:var(--muted)]">No plan yet — tap Edit to add steps.</p>
      )}
    </Section>
  );
}

const resToText = (items: ResourceLink[]) =>
  items.map((r) => (r.url ? `${r.label} | ${r.url}` : r.label)).join("\n");

const textToRes = (text: string): ResourceLink[] =>
  text
    .split("\n")
    .map((line) => line.trim())
    .filter(Boolean)
    .map((line) => {
      const [label, url] = line.split("|");
      const trimmed = (url ?? "").trim();
      return trimmed ? { label: label.trim(), url: trimmed } : { label: label.trim() };
    });

export function ResourceSection({
  items,
  onSave,
}: {
  items: ResourceLink[];
  onSave: (next: ResourceLink[]) => Promise<void>;
}) {
  const [editing, setEditing] = useState(false);
  const [draft, setDraft] = useState(resToText(items));
  const [saving, setSaving] = useState(false);

  const save = async () => {
    setSaving(true);
    try {
      await onSave(textToRes(draft));
      setEditing(false);
    } finally {
      setSaving(false);
    }
  };

  return (
    <Section
      title="Resources"
      hint="One per line, as: name | https://link (link optional)"
      editing={editing}
      saving={saving}
      onEdit={() => {
        setDraft(resToText(items));
        setEditing(true);
      }}
      onCancel={() => setEditing(false)}
      onSave={save}
    >
      {editing ? (
        <textarea className="field min-h-32" value={draft} onChange={(e) => setDraft(e.target.value)} />
      ) : items.length ? (
        <ul className="space-y-2">
          {items.map((r, i) => (
            <li key={i}>
              {r.url ? (
                <a
                  href={r.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-[15px] font-medium text-[color:var(--accent)] underline underline-offset-2"
                >
                  {r.label}
                </a>
              ) : (
                <span className="text-[15px]">{r.label}</span>
              )}
            </li>
          ))}
        </ul>
      ) : (
        <p className="text-sm text-[color:var(--muted)]">No resources yet — tap Edit to add.</p>
      )}
    </Section>
  );
}
