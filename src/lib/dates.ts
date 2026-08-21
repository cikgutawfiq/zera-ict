export const MS_DAY = 86400000;

export function toISO(d: Date): string {
  const tz = new Date(d.getTime() - d.getTimezoneOffset() * 60000);
  return tz.toISOString().slice(0, 10);
}

export function fromISO(iso: string): Date {
  const [y, m, d] = iso.split("-").map(Number);
  return new Date(y, m - 1, d);
}

export function addDays(iso: string, n: number): string {
  const d = fromISO(iso);
  d.setDate(d.getDate() + n);
  return toISO(d);
}

/** Monday of the week containing `iso`. */
export function mondayOf(iso: string): string {
  const d = fromISO(iso);
  const shift = (d.getDay() + 6) % 7;
  d.setDate(d.getDate() - shift);
  return toISO(d);
}

export function todayISO(): string {
  return toISO(new Date());
}

/** First of the month containing `iso`. */
export function startOfMonth(iso: string): string {
  const d = fromISO(iso);
  return toISO(new Date(d.getFullYear(), d.getMonth(), 1));
}

export function addMonths(iso: string, n: number): string {
  const d = fromISO(iso);
  return toISO(new Date(d.getFullYear(), d.getMonth() + n, 1));
}

export function daysInMonth(iso: string): number {
  const d = fromISO(iso);
  return new Date(d.getFullYear(), d.getMonth() + 1, 0).getDate();
}

const MONTH_YEAR = new Intl.DateTimeFormat("en-GB", { month: "long", year: "numeric" });

export function formatMonthYear(iso: string): string {
  return MONTH_YEAR.format(fromISO(iso));
}

const LONG = new Intl.DateTimeFormat("en-GB", { weekday: "long", day: "numeric", month: "long", year: "numeric" });
const SHORT = new Intl.DateTimeFormat("en-GB", { day: "numeric", month: "short" });

export function formatLong(iso: string): string {
  return LONG.format(fromISO(iso));
}

export function formatShort(iso: string): string {
  return SHORT.format(fromISO(iso));
}

export function formatRange(startISO: string, endISO: string): string {
  return `${formatShort(startISO)} – ${formatShort(endISO)}`;
}

export function isBetween(iso: string, startISO: string, endISO: string): boolean {
  return iso >= startISO && iso <= endISO;
}

/** "13:15" -> "1.15 pm" */
export function prettyTime(hhmm: string): string {
  const [h, m] = hhmm.split(":").map(Number);
  const suffix = h >= 12 ? "pm" : "am";
  const hour = h % 12 === 0 ? 12 : h % 12;
  return `${hour}.${String(m).padStart(2, "0")} ${suffix}`;
}
