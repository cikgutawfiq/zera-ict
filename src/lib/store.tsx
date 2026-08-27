"use client";

import { createContext, useContext, useEffect, useMemo, useState, type ReactNode } from "react";
import {
  collection,
  deleteDoc,
  doc,
  onSnapshot,
  setDoc,
  updateDoc,
  writeBatch,
  type DocumentData,
} from "firebase/firestore";
import { getDb } from "./firebase";
import { useAuth } from "./auth";
import { DEV_PREVIEW } from "./devPreview";
import seedData from "@/data/seed.json";
import { fromISO } from "./dates";
import type { Lesson, Term } from "./types";

type Store = {
  lessons: Lesson[];
  terms: Term[];
  loading: boolean;
  error: string | null;
  lessonById: (id: string) => Lesson | undefined;
  lessonFor: (classId: string, dateISO: string) => Lesson | undefined;
  lessonsForClass: (classId: string) => Lesson[];
  saveLesson: (id: string, patch: Partial<Lesson>) => Promise<void>;
  createLesson: (lesson: Lesson) => Promise<void>;
  deleteLesson: (id: string) => Promise<void>;
  saveTerm: (term: Term) => Promise<void>;
  deleteTerm: (id: string) => Promise<void>;
  seed: (payload: { terms: Term[]; lessons: Lesson[] }, overwriteEdited: boolean) => Promise<number>;
};

const Ctx = createContext<Store | null>(null);

export function DataProvider({ children }: { children: ReactNode }) {
  const { isOwner } = useAuth();
  const [lessons, setLessons] = useState<Lesson[]>([]);
  const [terms, setTerms] = useState<Term[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (DEV_PREVIEW) {
      const seeded = seedData as unknown as { terms: Term[]; lessons: Lesson[] };
      setLessons(seeded.lessons);
      setTerms(seeded.terms);
      setLoading(false);
      return;
    }
    if (!isOwner) {
      setLessons([]);
      setTerms([]);
      setLoading(false);
      return;
    }
    setLoading(true);
    const db = getDb();
    const unsubLessons = onSnapshot(
      collection(db, "lessons"),
      (snap) => {
        setLessons(snap.docs.map((d) => ({ ...(d.data() as DocumentData), id: d.id }) as Lesson));
        setLoading(false);
      },
      (e) => {
        setError(e.message);
        setLoading(false);
      },
    );
    const unsubTerms = onSnapshot(
      collection(db, "terms"),
      (snap) => setTerms(snap.docs.map((d) => ({ ...(d.data() as DocumentData), id: d.id }) as Term)),
      (e) => setError(e.message),
    );
    return () => {
      unsubLessons();
      unsubTerms();
    };
  }, [isOwner]);

  const value = useMemo<Store>(() => {
    const sortedTerms = [...terms].sort((a, b) => a.order - b.order);
    const sortedLessons = [...lessons].sort(
      (a, b) =>
        a.dateStart.localeCompare(b.dateStart) ||
        (a.day ?? 0) - (b.day ?? 0) ||
        a.classId.localeCompare(b.classId),
    );
    const db = () => getDb();

    return {
      lessons: sortedLessons,
      terms: sortedTerms,
      loading,
      error,
      lessonById: (id) => sortedLessons.find((l) => l.id === id),
      lessonFor: (classId, dateISO) => {
        const classLessons = sortedLessons.filter((l) => l.classId === classId);
        const dow = fromISO(dateISO).getDay();
        const inRange = (l: Lesson) => dateISO >= l.dateStart && dateISO <= l.dateEnd;
        // Prefer an exact day match (multi-session classes) over a day-less lesson that
        // spans the whole week — otherwise a stray pre-migration doc with no `day` field
        // would win the sort order and get shown (and marked Done) for every session.
        let idx = classLessons.findIndex((l) => inRange(l) && l.day === dow);
        if (idx === -1) idx = classLessons.findIndex((l) => inRange(l) && l.day === undefined);
        if (idx === -1) return undefined;
        const natural = classLessons[idx];
        const prev = classLessons[idx - 1];
        // A lesson that didn't get finished stays front-and-centre on the next scheduled
        // slot for this class, instead of quietly falling behind the calendar.
        if (prev && prev.status === "carried-over") {
          return { ...prev, carriedIntoWeekLabel: natural.weekLabel };
        }
        return natural;
      },
      lessonsForClass: (classId) => sortedLessons.filter((l) => l.classId === classId),
      saveLesson: async (id, patch) => {
        await updateDoc(doc(db(), "lessons", id), { ...patch, updatedAt: Date.now() });
      },
      createLesson: async (lesson) => {
        const { id, ...rest } = lesson;
        await setDoc(doc(db(), "lessons", id), { ...rest, updatedAt: Date.now() });
      },
      deleteLesson: async (id) => {
        await deleteDoc(doc(db(), "lessons", id));
      },
      saveTerm: async (term) => {
        const { id, ...rest } = term;
        await setDoc(doc(db(), "terms", id), rest, { merge: true });
      },
      deleteTerm: async (id) => {
        await deleteDoc(doc(db(), "terms", id));
      },
      seed: async (payload, overwriteEdited) => {
        const edited = new Set(lessons.filter((l) => l.updatedAt).map((l) => l.id));
        const targets = payload.lessons.filter((l) => overwriteEdited || !edited.has(l.id));

        // Multi-session classes (Maths Y1, Malay Enrichment Y8) migrated from one lesson
        // per week to one lesson per session (id "..._d{day}"). Any doc still sitting on
        // the old id with no `day` field is a pre-migration leftover — clear it out so it
        // can't shadow the new per-session lessons (see lessonFor in this file).
        const MULTI_SESSION_CLASS_IDS = new Set(["maths-y1", "me-y8"]);
        const legacyIds = lessons
          .filter((l) => MULTI_SESSION_CLASS_IDS.has(l.classId) && l.day === undefined)
          .filter((l) => overwriteEdited || !l.updatedAt)
          .map((l) => l.id);

        let batch = writeBatch(db());
        let ops = 0;
        let written = 0;
        for (const term of payload.terms) {
          const { id, ...rest } = term;
          batch.set(doc(db(), "terms", id), rest, { merge: true });
          ops++;
        }
        for (const lesson of targets) {
          const { id, ...rest } = lesson;
          batch.set(doc(db(), "lessons", id), rest, { merge: true });
          written++;
          if (++ops >= 400) {
            await batch.commit();
            batch = writeBatch(db());
            ops = 0;
          }
        }
        for (const id of legacyIds) {
          batch.delete(doc(db(), "lessons", id));
          if (++ops >= 400) {
            await batch.commit();
            batch = writeBatch(db());
            ops = 0;
          }
        }
        if (ops > 0) await batch.commit();
        return written;
      },
    };
  }, [lessons, terms, loading, error]);

  return <Ctx.Provider value={value}>{children}</Ctx.Provider>;
}

export function useData(): Store {
  const v = useContext(Ctx);
  if (!v) throw new Error("useData must be used inside <DataProvider>");
  return v;
}
