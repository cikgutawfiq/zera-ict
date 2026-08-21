import type { ClassInfo } from "@/lib/types";

/**
 * Mr Tawfiq bin Rahmat — teacher timetable, v2 (26.8.2026).
 * Period grid (school-wide):
 *   reg 0815-0830 | 1 0830-0910 | 2 0910-0945 | 3/Break 0945-1020 | 3/Break 1020-1055
 *   4 1055-1130 | 5 1130-1205 | 6 1205-1240 | Lunch/7 1240-1315 | 7/Lunch 1315-1350
 *   8 1350-1430 | 9 1430-1500
 * Total taught periods: 27.
 */

export type Slot = {
  day: 1 | 2 | 3 | 4 | 5; // Mon..Fri
  start: string; // HH:mm
  end: string;
  periods: string; // human label, e.g. "P1-2"
  classId: string;
  duty?: boolean; // non-lesson duty (assembly, support) — not backed by a lesson
  room?: string;
};

export const CLASSES: ClassInfo[] = [
  { id: "ict-y1", code: "Y1", subject: "ICT", label: "ICT Y1", keyStage: "KS1", periodsPerWeek: 2, color: "#f97316" },
  { id: "ict-y2", code: "Y2", subject: "ICT", label: "ICT Y2", keyStage: "KS1", periodsPerWeek: 2, color: "#f59e0b" },
  { id: "ict-y3", code: "Y3", subject: "ICT", label: "ICT Y3", keyStage: "KS2", periodsPerWeek: 2, color: "#84cc16" },
  { id: "ict-y4", code: "Y4", subject: "ICT", label: "ICT Y4", keyStage: "KS2", periodsPerWeek: 2, color: "#10b981" },
  { id: "ict-y5", code: "Y5", subject: "ICT", label: "ICT Y5", keyStage: "KS2", periodsPerWeek: 2, color: "#06b6d4" },
  { id: "ict-y6", code: "Y6", subject: "ICT", label: "ICT Y6", keyStage: "KS2", periodsPerWeek: 2, color: "#3b82f6" },
  { id: "ict-y7", code: "Y7", subject: "ICT", label: "ICT Y7", keyStage: "KS3", periodsPerWeek: 2, color: "#6366f1" },
  { id: "ict-y8", code: "Y8", subject: "ICT", label: "ICT Y8", keyStage: "KS3", periodsPerWeek: 2, color: "#8b5cf6" },
  { id: "ict-y9", code: "Y9", subject: "ICT", label: "ICT Y9", keyStage: "KS3", periodsPerWeek: 2, color: "#a855f7" },
  { id: "maths-y1", code: "Y1", subject: "Mathematics", label: "Maths Y1", keyStage: "KS1", periodsPerWeek: 6, color: "#ec4899" },
  { id: "me-y8", code: "Y8", subject: "Malay Enrichment", label: "Malay Enrichment Y8", keyStage: "KS3", periodsPerWeek: 3, color: "#14b8a6" },
];

export const CLASS_BY_ID = Object.fromEntries(CLASSES.map((c) => [c.id, c]));

export const SLOTS: Slot[] = [
  // Monday
  { day: 1, start: "08:30", end: "09:45", periods: "P1-2", classId: "me-y8", room: "C3-1" },
  { day: 1, start: "10:20", end: "10:55", periods: "P3", classId: "assembly", duty: true },
  { day: 1, start: "11:30", end: "12:40", periods: "P5-6", classId: "pe-y4", duty: true },
  { day: 1, start: "13:15", end: "14:30", periods: "P7-8", classId: "ict-y8", room: "Y8" },
  // Tuesday
  { day: 2, start: "08:30", end: "09:45", periods: "P1-2", classId: "maths-y1", room: "Y1" },
  { day: 2, start: "09:45", end: "10:20", periods: "P3", classId: "me-y8", room: "C3-1" },
  { day: 2, start: "10:20", end: "11:30", periods: "P3-4", classId: "ict-y5", room: "Y5" },
  { day: 2, start: "11:30", end: "12:40", periods: "P5-6", classId: "ict-y3", room: "Y3" },
  // Wednesday
  { day: 3, start: "08:30", end: "09:45", periods: "P1-2", classId: "ict-y7", room: "Y7" },
  { day: 3, start: "10:20", end: "11:30", periods: "P3-4", classId: "ict-y6", room: "Y6" },
  { day: 3, start: "12:05", end: "13:15", periods: "P6-7", classId: "ict-y9", room: "Y9" },
  // Thursday
  { day: 4, start: "10:20", end: "11:30", periods: "P3-4", classId: "maths-y1", room: "Y1" },
  { day: 4, start: "11:30", end: "12:40", periods: "P5-6", classId: "ict-y2", room: "Y2" },
  { day: 4, start: "13:15", end: "14:30", periods: "P7-8", classId: "ict-y4", room: "Y4" },
  // Friday
  { day: 5, start: "08:30", end: "09:45", periods: "P1-2", classId: "maths-y1", room: "Y1" },
  { day: 5, start: "10:20", end: "11:30", periods: "P3-4", classId: "ict-y1", room: "Y1" },
];

export const DUTIES: Record<string, string> = {
  assembly: "Assembly (Primary)",
  "pe-y4": "PE Support Y4",
};

export const DAY_NAMES = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

export function slotsForDay(day: number): Slot[] {
  return SLOTS.filter((s) => s.day === day).sort((a, b) => a.start.localeCompare(b.start));
}

export function slotsForClass(classId: string): Slot[] {
  return SLOTS.filter((s) => s.classId === classId).sort((a, b) => a.day - b.day || a.start.localeCompare(b.start));
}
