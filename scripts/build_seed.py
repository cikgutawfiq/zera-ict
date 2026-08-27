"""Merge the SOW (Term 1) and authored Term 2/3 content into src/data/seed.json.

Run, in order:
  python scripts/extract_sow.py       # Term 1 from the two workbooks
  python scripts/build_terms23.py     # Term 2/3 week calendars
  python scripts/build_seed.py        # merge everything + assign moral content

Output shape:
  { "terms": [Term, Term, Term], "lessons": [Lesson] }  -- what /admin writes
  to Firestore, and what the browser Excel-upload path (src/lib/parseSow.ts)
  produces for Term 1 re-uploads.
"""
import json
import os

from values import assign_ice_breaker, assign_moral_content
from build_maths_y1 import build_maths_y1_lessons

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "src", "data")
RAW = os.path.join(DATA, "sow.raw.json")
TERMS23 = os.path.join(DATA, "terms23.json")
AUTHORED = os.path.join(DATA, "authored")
OUT = os.path.join(DATA, "seed.json")

ICT_YEARS = list(range(1, 10))
# classId -> weekly session days (JS Date.getDay() convention, Mon=1..Fri=5),
# for classes that meet more than once a week and need one lesson per session
# instead of one shared lesson for the whole week. Matches SLOTS in
# src/data/timetable.ts.
BLANK_CLASSES = [
    {"classId": "me-y8", "subject": "Malay Enrichment", "days": [1, 2]},
]
DAY_SHORT = {1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri"}
EMPTY = {"objectives": [], "plan": [], "activities": [], "successCriteria": [], "resources": []}


def lesson_id(class_id: str, term_id: str, week_no) -> str:
    return f"{class_id}_{term_id}_w{week_no}"


def build_ict_lessons(term_id: str, weeks_by_week_no: dict, ict_source: dict) -> list:
    """weeks_by_week_no: {weekNo: TermWeek dict}. ict_source: {"1": {...weekNo: content}}."""
    out = []
    for year in ICT_YEARS:
        class_id = f"ict-y{year}"
        authored = ict_source[str(year)]
        order = 0
        for week_no_str, content in sorted(authored.items(), key=lambda kv: int(kv[0])):
            week_no = int(week_no_str)
            cal = weeks_by_week_no.get(week_no)
            if cal is None:
                raise SystemExit(f"{term_id} year {year} week {week_no}: no matching calendar week")
            out.append(
                {
                    "id": lesson_id(class_id, term_id, week_no),
                    "classId": class_id,
                    "subject": "ICT",
                    "termId": term_id,
                    "weekNo": week_no,
                    "weekLabel": cal["label"],
                    "dateStart": cal["start"],
                    "dateEnd": cal["end"],
                    "topic": content["topic"],
                    "subtopic": content["subtopic"],
                    "outline": content["outline"],
                    "sowResources": content["sowResources"],
                    "remark": cal.get("remark", ""),
                    "objectives": content["objectives"],
                    "plan": content["plan"],
                    "activities": content["activities"],
                    "successCriteria": content["successCriteria"],
                    "resources": content["resources"],
                    "status": "planned",
                    "note": "",
                    "order": order,
                }
            )
            order += 1
    return out


def build_term1_lessons(raw: dict) -> tuple[list, dict]:
    out = []
    calendar_weeks = {w["no"]: w for w in raw["term"]["weeks"] if not w["isBreak"]}
    for year in ICT_YEARS:
        class_id = f"ict-y{year}"
        authored = json.load(open(os.path.join(AUTHORED, f"y{year}.json"), encoding="utf-8"))
        rows = [r for r in raw["years"][str(year)] if not r["isBreak"]]
        order = 0
        for row in rows:
            week = row["weekNo"]
            extra = authored.get(str(week))
            if extra is None:
                raise SystemExit(f"term-1 year {year} week {week}: missing authored content")
            out.append(
                {
                    "id": lesson_id(class_id, "term-1", week),
                    "classId": class_id,
                    "subject": "ICT",
                    "termId": "term-1",
                    "weekNo": week,
                    "weekLabel": row["weekLabel"],
                    "dateStart": row["dateStart"],
                    "dateEnd": row["dateEnd"],
                    "topic": row["topic"],
                    "subtopic": row["subtopic"],
                    "outline": row["outline"],
                    "sowResources": row["sowResources"],
                    "remark": row["remark"],
                    "objectives": extra["objectives"],
                    "plan": extra["plan"],
                    "activities": extra["activities"],
                    "successCriteria": extra["successCriteria"],
                    "resources": extra["resources"],
                    "status": "planned",
                    "note": "",
                    "order": order,
                }
            )
            order += 1
    return out, calendar_weeks


def build_blank_rows(term_id: str, weeks: list) -> list:
    out = []
    teaching_weeks = [w for w in weeks if not w["isBreak"]]
    for spec in BLANK_CLASSES:
        order = 0
        for week in teaching_weeks:
            for day in spec["days"]:
                out.append(
                    {
                        "id": f"{spec['classId']}_{term_id}_w{week['no']}_d{day}",
                        "classId": spec["classId"],
                        "subject": spec["subject"],
                        "termId": term_id,
                        "weekNo": week["no"],
                        "weekLabel": f"{week['label']} ({DAY_SHORT[day]})",
                        "dateStart": week["start"],
                        "dateEnd": week["end"],
                        "day": day,
                        "topic": "",
                        "subtopic": "",
                        "outline": "",
                        "sowResources": "",
                        "remark": week["remark"],
                        "status": "planned",
                        "note": "",
                        "order": order,
                        **EMPTY,
                    }
                )
                order += 1
    return out


def attach_moral_content(lessons: list) -> None:
    """Assign moralValue/quote/foodForThought/iceBreaker* in-place, chronologically per class."""
    by_class: dict = {}
    for lesson in lessons:
        by_class.setdefault(lesson["classId"], []).append(lesson)
    for class_id, group in by_class.items():
        group.sort(key=lambda l: (l["termId"], l["weekNo"] if l["weekNo"] is not None else 0))
        for i, lesson in enumerate(group):
            lesson.update(assign_moral_content(class_id, i))
            lesson.update(assign_ice_breaker(class_id, i))


def main():
    raw = json.load(open(RAW, encoding="utf-8"))
    terms23 = json.load(open(TERMS23, encoding="utf-8"))

    term1_lessons, term1_cal = build_term1_lessons(raw)

    term2_cal = {w["no"]: w for w in terms23["term2"]["weeks"] if not w["isBreak"]}
    term3_cal = {w["no"]: w for w in terms23["term3"]["weeks"] if not w["isBreak"]}

    term2_source = {
        str(y): json.load(open(os.path.join(AUTHORED, "term2", f"y{y}.json"), encoding="utf-8"))
        for y in ICT_YEARS
    }
    term3_source = {
        str(y): json.load(open(os.path.join(AUTHORED, "term3", f"y{y}.json"), encoding="utf-8"))
        for y in ICT_YEARS
    }
    term2_lessons = build_ict_lessons("term-2", term2_cal, term2_source)
    term3_lessons = build_ict_lessons("term-3", term3_cal, term3_source)

    blanks = (
        build_blank_rows("term-1", raw["term"]["weeks"])
        + build_blank_rows("term-2", terms23["term2"]["weeks"])
        + build_blank_rows("term-3", terms23["term3"]["weeks"])
    )

    maths_y1_lessons = (
        build_maths_y1_lessons("term-1", term1_cal)
        + build_maths_y1_lessons("term-2", term2_cal)
        + build_maths_y1_lessons("term-3", term3_cal)
    )

    lessons = term1_lessons + term2_lessons + term3_lessons + blanks + maths_y1_lessons
    attach_moral_content(lessons)

    terms = [raw["term"], terms23["term2"], terms23["term3"]]
    payload = {"terms": terms, "lessons": lessons}

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1, ensure_ascii=False)

    ict = sum(1 for x in lessons if x["subject"] == "ICT")
    maths = sum(1 for x in lessons if x["subject"] == "Mathematics")
    blank = len(lessons) - ict - maths
    print(f"lessons: {len(lessons)} total ({ict} ICT, {maths} Maths Y1, {blank} blank)")
    for t in terms:
        print(f"  {t['name']}: {len(t['weeks'])} weeks")
    print(f"wrote {os.path.abspath(OUT)}")


if __name__ == "__main__":
    main()
