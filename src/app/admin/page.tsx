"use client";

import { useState } from "react";
import { useAuth } from "@/lib/auth";
import { useData } from "@/lib/store";
import { PageHeader } from "@/components/ui";
import { addDays, formatRange, mondayOf, todayISO } from "@/lib/dates";
import seed from "@/data/seed.json";
import { parseSowWorkbooks } from "@/lib/parseSow";
import type { Lesson, Term, TermWeek } from "@/lib/types";

const SEED = seed as unknown as { terms: Term[]; lessons: Lesson[] };

export default function AdminPage() {
  const { user, signOut } = useAuth();
  const { lessons, terms, seed: runSeed, saveTerm, deleteTerm } = useData();
  const [busy, setBusy] = useState(false);
  const [message, setMessage] = useState<string | null>(null);
  const [overwrite, setOverwrite] = useState(false);
  const [ks1ks2File, setKs1ks2File] = useState<File | null>(null);
  const [ks3File, setKs3File] = useState<File | null>(null);
  const [uploadMessage, setUploadMessage] = useState<string | null>(null);
  const [openTermId, setOpenTermId] = useState<string | null>(null);

  const edited = lessons.filter((l) => l.updatedAt).length;

  const doUpload = async () => {
    if (!ks1ks2File || !ks3File) return;
    const warning = overwrite
      ? "Re-parse both workbooks and overwrite ALL Term 1 lessons, including any you've edited?"
      : "Re-parse both workbooks and update Term 1, skipping any lessons you've already edited?";
    if (!confirm(warning)) return;
    setBusy(true);
    setUploadMessage(null);
    try {
      const parsed = await parseSowWorkbooks({ ks1ks2: ks1ks2File, ks3: ks3File });
      const written = await runSeed(parsed, overwrite);
      setUploadMessage(`Upload complete — ${written} Term 1 lesson(s) written from the workbooks.`);
    } catch (e) {
      setUploadMessage(`Upload failed: ${(e as Error).message}`);
    } finally {
      setBusy(false);
    }
  };

  const doSeed = async () => {
    const warning = overwrite
      ? `Overwrite ALL ${SEED.lessons.length} lessons from the scheme of work, including the ${edited} you have edited?`
      : `Write ${SEED.lessons.length} lessons from the scheme of work, skipping any you have already edited?`;
    if (!confirm(warning)) return;
    setBusy(true);
    setMessage(null);
    try {
      const written = await runSeed(SEED, overwrite);
      setMessage(`Seed complete — ${written} lesson(s) written, ${SEED.lessons.length - written} skipped.`);
    } catch (e) {
      setMessage(`Seed failed: ${(e as Error).message}`);
    } finally {
      setBusy(false);
    }
  };

  const addTerm = async () => {
    const order = terms.length + 1;
    const name = prompt("Term name", `Term ${order}`);
    if (!name) return;
    const id = name.toLowerCase().replace(/[^a-z0-9]+/g, "-");
    setBusy(true);
    try {
      await saveTerm({ id, name, order, weeks: [] });
      setMessage(`Created ${name}. Add weeks below, then add lessons from each class page.`);
    } finally {
      setBusy(false);
    }
  };

  const addWeek = async (term: Term) => {
    const noRaw = prompt("Week number", String((term.weeks.at(-1)?.no ?? 0) + 1));
    if (!noRaw) return;
    const startRaw = prompt("Week starting (YYYY-MM-DD, Monday)", mondayOf(todayISO()));
    if (!startRaw) return;
    const start = mondayOf(startRaw);
    const no = Number.parseInt(noRaw, 10);
    const week: TermWeek = {
      no,
      label: `Week ${no}`,
      start,
      end: addDays(start, 4),
      isBreak: false,
      isExam: false,
      remark: "",
    };
    setBusy(true);
    try {
      await saveTerm({ ...term, weeks: [...term.weeks, week].sort((a, b) => a.start.localeCompare(b.start)) });
    } finally {
      setBusy(false);
    }
  };

  const removeWeek = async (term: Term, index: number) => {
    if (!confirm(`Remove ${term.weeks[index].label} from ${term.name}? Lessons are not deleted.`)) return;
    setBusy(true);
    try {
      await saveTerm({ ...term, weeks: term.weeks.filter((_, i) => i !== index) });
    } finally {
      setBusy(false);
    }
  };

  const removeTerm = async (term: Term) => {
    if (!confirm(`Delete ${term.name}? Its lessons stay in the database but will be unfiled.`)) return;
    setBusy(true);
    try {
      await deleteTerm(term.id);
    } finally {
      setBusy(false);
    }
  };

  return (
    <>
      <PageHeader title="Admin" subtitle={user?.email ?? undefined} />

      <main className="mx-auto max-w-6xl space-y-3 p-4 lg:p-6">
        <div className="grid grid-cols-1 gap-3 lg:grid-cols-2">
        <section className="card p-4">
          <h2 className="text-sm font-bold">Update Term 1 from Excel</h2>
          <p className="mt-1 text-xs text-[color:var(--muted)]">
            Upload a revised SOW workbook to update Term 1's dates, topics and remarks — right from your
            phone, no computer needed. Your lesson plans stay put; only the scheme-of-work fields refresh.
          </p>
          <div className="mt-3 space-y-2">
            <label className="block text-xs font-semibold text-[color:var(--muted)]">
              KS1–KS2 workbook (Y1–Y6)
              <input
                type="file"
                accept=".xlsx"
                className="field mt-1"
                onChange={(e) => setKs1ks2File(e.target.files?.[0] ?? null)}
              />
            </label>
            <label className="block text-xs font-semibold text-[color:var(--muted)]">
              KS3 workbook (Y7–Y9)
              <input
                type="file"
                accept=".xlsx"
                className="field mt-1"
                onChange={(e) => setKs3File(e.target.files?.[0] ?? null)}
              />
            </label>
          </div>
          <button
            className="btn btn-primary mt-3 w-full"
            onClick={doUpload}
            disabled={busy || !ks1ks2File || !ks3File}
          >
            {busy ? "Working…" : "Re-parse and update Term 1"}
          </button>
          {uploadMessage && <p className="mt-3 text-xs text-[color:var(--accent)]">{uploadMessage}</p>}
        </section>

        <section className="card p-4">
          <h2 className="text-sm font-bold">Database</h2>
          <p className="mt-1 text-xs text-[color:var(--muted)]">
            {lessons.length} lesson(s) live · {edited} edited by you · {terms.length} term(s).
          </p>
          <label className="mt-3 flex items-start gap-2 text-xs">
            <input
              type="checkbox"
              className="mt-0.5"
              checked={overwrite}
              onChange={(e) => setOverwrite(e.target.checked)}
            />
            <span>
              Overwrite lessons I have edited. Leave this off to keep your own changes and only fill in
              what is missing.
            </span>
          </label>
          <button className="btn btn-primary mt-3 w-full" onClick={doSeed} disabled={busy}>
            {busy ? "Working…" : `Seed / re-sync ${SEED.lessons.length} lessons from the SOW`}
          </button>
          {message && <p className="mt-3 text-xs text-[color:var(--accent)]">{message}</p>}
        </section>
        </div>

        <section className="card p-4">
          <div className="flex items-center gap-2">
            <h2 className="flex-1 text-sm font-bold">Terms</h2>
            <button className="btn btn-sm" onClick={addTerm} disabled={busy}>
              + Term
            </button>
          </div>
          {terms.length === 0 && (
            <p className="mt-2 text-xs text-[color:var(--muted)]">No terms yet — seed the database first.</p>
          )}
          <div className="mt-3 space-y-2">
            {terms.map((term) => {
              const open = openTermId === term.id;
              return (
                <div key={term.id} className="overflow-hidden rounded-lg border border-[color:var(--border)]">
                  <button
                    className="flex w-full items-center gap-2 px-3 py-2.5 text-left"
                    onClick={() => setOpenTermId(open ? null : term.id)}
                    aria-expanded={open}
                  >
                    <span
                      aria-hidden
                      className="text-sm text-[color:var(--muted)] transition-transform"
                      style={{
                        transform: open ? "rotate(90deg)" : "rotate(0deg)",
                        transitionDuration: "var(--dur-fast)",
                        transitionTimingFunction: "var(--ease)",
                      }}
                    >
                      ▸
                    </span>
                    <span className="flex-1 text-sm font-semibold">{term.name}</span>
                    <span className="chip">{term.weeks.length} weeks</span>
                  </button>
                  {open && (
                    <div className="border-t border-[color:var(--border)] p-3">
                      <div className="flex items-center gap-2">
                        <span className="flex-1" />
                        <button className="btn btn-sm" onClick={() => addWeek(term)} disabled={busy}>
                          + Week
                        </button>
                        <button
                          className="btn btn-sm"
                          style={{ color: "var(--warn)" }}
                          onClick={() => removeTerm(term)}
                          disabled={busy}
                        >
                          Delete term
                        </button>
                      </div>
                      <ul className="mt-2 space-y-1">
                        {term.weeks.map((w, i) => (
                          <li key={`${w.start}-${i}`} className="flex items-center gap-2 text-xs">
                            <span className="w-20 shrink-0 font-semibold">{w.label}</span>
                            <span className="flex-1 text-[color:var(--muted)]">{formatRange(w.start, w.end)}</span>
                            {w.isBreak && <span className="chip">break</span>}
                            {w.isExam && <span className="chip">exam</span>}
                            <button
                              className="btn btn-sm"
                              onClick={() => removeWeek(term, i)}
                              disabled={busy}
                              aria-label={`Remove ${w.label}`}
                            >
                              ✕
                            </button>
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </section>

        <section className="card p-4">
          <h2 className="text-sm font-bold">Account</h2>
          <p className="mt-1 text-xs text-[color:var(--muted)]">
            Signed in as {user?.email}. Only this account can read or write the dashboard.
          </p>
          <button className="btn mt-3 w-full" onClick={signOut}>
            Sign out
          </button>
        </section>
      </main>
    </>
  );
}
