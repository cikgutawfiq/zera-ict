"""Generate the Term 2 and Term 3 week calendars.

Term 2 and Term 3 have no source workbook (unlike Term 1) — Zera's curriculum
hub (cikgutawfiq.com/zera-ict-sow1) only publishes a start date and an 8-topic
outline per term. This script turns those start dates into real week-by-week
calendars:

  Term 2: 6 Jan 2027 -> 24 Mar 2027 is exactly 11 weeks (confirmed: both dates
  fall on a Wednesday, same as every Zera term start). That leaves no room for
  a 15-week term shaped like Term 1 — Term 3's start date is fixed and known,
  so Term 2 is compressed to fit: 8 topic weeks + Consolidation + Revision +
  Examination Week, no mid-term break, no post-exam project block.

  Term 3: starts 24 Mar 2027 with no published end date. Given the full
  15-week treatment (8 topic weeks + Consolidation + Revision + Examination
  Week + a mid-term break + 3 End-of-Term-Project weeks + Portfolio Showcase),
  matching Term 1's shape, running to ~9 Jul 2027. This end date is an
  ESTIMATE — correct it in Admin once the real calendar is published.

Run:  python scripts/build_terms23.py
Writes src/data/terms23.json — consumed by scripts/build_seed.py.
"""
import json
import os
from datetime import date, timedelta

OUT = os.path.join(os.path.dirname(__file__), "..", "src", "data", "terms23.json")


def week(no, start, end, label=None, is_break=False, is_exam=False, remark=""):
    return {
        "no": no,
        "label": label or (f"Week {no}" if no else "Break"),
        "start": start.isoformat(),
        "end": end.isoformat(),
        "isBreak": is_break,
        "isExam": is_exam,
        "remark": remark,
    }


def monday_friday(monday: date):
    return monday, monday + timedelta(days=4)


def build_term2():
    weeks = []
    # Week 1: Wed 6 Jan - Fri 8 Jan 2027 (mid-week start, matches Term 1's pattern)
    weeks.append(week(1, date(2027, 1, 6), date(2027, 1, 8)))
    monday = date(2027, 1, 11)
    for no in range(2, 9):  # Weeks 2-8: the 8 topic weeks
        start, end = monday_friday(monday)
        weeks.append(week(no, start, end))
        monday += timedelta(days=7)
    # Week 9 Consolidation, 10 Revision, 11 Examination Week
    start, end = monday_friday(monday)
    weeks.append(week(9, start, end))
    monday += timedelta(days=7)
    start, end = monday_friday(monday)
    weeks.append(week(10, start, end))
    monday += timedelta(days=7)
    start, end = monday_friday(monday)
    weeks.append(week(11, start, end, is_exam=True, remark="Term 2 Examination Week"))
    return {"id": "term-2", "name": "Term 2", "order": 2, "weeks": weeks}


def build_term3():
    weeks = []
    weeks.append(week(1, date(2027, 3, 24), date(2027, 3, 26)))
    monday = date(2027, 3, 29)
    for no in range(2, 9):  # Weeks 2-8: the 8 topic weeks
        start, end = monday_friday(monday)
        weeks.append(week(no, start, end))
        monday += timedelta(days=7)
    start, end = monday_friday(monday)  # Week 9 Consolidation
    weeks.append(week(9, start, end))
    monday += timedelta(days=7)
    start, end = monday_friday(monday)  # Week 10 Revision
    weeks.append(week(10, start, end))
    monday += timedelta(days=7)
    start, end = monday_friday(monday)  # Week 11 Examination Week
    weeks.append(week(11, start, end, is_exam=True, remark="Term 3 Examination Week"))
    monday += timedelta(days=7)
    start, end = monday_friday(monday)  # Mid-term break
    weeks.append(week(None, start, end, label="Break", is_break=True))
    monday += timedelta(days=7)
    for no in range(12, 15):  # Weeks 12-14: End of Term Project
        start, end = monday_friday(monday)
        weeks.append(week(no, start, end))
        monday += timedelta(days=7)
    start, end = monday_friday(monday)  # Week 15 Portfolio Showcase
    weeks.append(
        week(
            15,
            start,
            end,
            remark="Estimated end of Term 3 — no official calendar published yet; confirm and adjust in Admin.",
        )
    )
    return {"id": "term-3", "name": "Term 3", "order": 3, "weeks": weeks}


def main():
    payload = {"term2": build_term2(), "term3": build_term3()}
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1, ensure_ascii=False)
    t2, t3 = payload["term2"], payload["term3"]
    print(f"Term 2: {len(t2['weeks'])} weeks, {t2['weeks'][0]['start']} -> {t2['weeks'][-1]['end']}")
    print(f"Term 3: {len(t3['weeks'])} weeks, {t3['weeks'][0]['start']} -> {t3['weeks'][-1]['end']}")
    print(f"wrote {os.path.abspath(OUT)}")


if __name__ == "__main__":
    main()
