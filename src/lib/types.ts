export type Status = "planned" | "done" | "carried-over";

export type ResourceLink = { label: string; url?: string };

export type Lesson = {
  id: string;
  classId: string;
  subject: string;
  termId: string;
  weekNo: number;
  weekLabel: string;
  dateStart: string; // ISO yyyy-mm-dd (Monday of the week)
  dateEnd: string;
  topic: string;
  subtopic: string;
  outline: string;
  sowResources: string;
  remark: string;
  objectives: string[];
  plan: PlanStep[];
  activities: string[];
  successCriteria: string[];
  resources: ResourceLink[];
  status: Status;
  note: string;
  order: number;
  updatedAt?: number;
};

export type PlanStep = { mins: number; title: string; detail: string };

export type TermWeek = {
  no: number | null;
  label: string;
  start: string;
  end: string;
  isBreak: boolean;
  isExam: boolean;
  remark: string;
};

export type Term = {
  id: string;
  name: string;
  order: number;
  weeks: TermWeek[];
};

export type ClassInfo = {
  id: string;
  code: string; // Y1..Y9
  subject: string; // ICT | Mathematics | Malay Enrichment
  label: string;
  keyStage: string;
  periodsPerWeek: number;
  color: string;
};
