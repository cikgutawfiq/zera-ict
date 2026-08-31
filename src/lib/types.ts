export type Status = "planned" | "done" | "carried-over";

export type EquipmentMode = "unplugged" | "shared-laptops" | "1-1-devices";

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
  /** Which weekday session (Mon=1..Fri=5) this lesson is for, matching Slot.day in
   *  timetable.ts. Only set for classes that meet more than once a week (each session
   *  gets its own lesson doc); undefined for classes with a single weekly session, where
   *  the whole dateStart-dateEnd week range is unambiguous. */
  day?: number;
  /** What kind of device access this lesson assumes. Unset/"1-1-devices" means one device
   *  per pupil as normal; "shared-laptops" means small groups rotate around a shared device;
   *  "unplugged" means no devices at all — paper, discussion or movement-based. */
  equipmentMode?: EquipmentMode;
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
  moralValue: string;
  moralDescription: string;
  quote: string;
  quoteAuthor: string;
  foodForThought: string;
  iceBreakerTitle: string;
  iceBreakerDescription: string;
  iceBreakerMinutes: number;
  status: Status;
  note: string;
  order: number;
  updatedAt?: number;
  /** Transient: set by `lessonFor` when a carried-over lesson is being shown in place of
   *  the lesson naturally scheduled for this slot. Never persisted. */
  carriedIntoWeekLabel?: string;
};

export type PlanStep = {
  mins: number;
  title: string;
  detail: string; // instructions — what the teacher says/sets up
  studentActivity?: string; // what students actually do during this step
  assessment?: string; // how to check understanding during/after this step
};

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
