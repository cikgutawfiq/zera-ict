"""Merges the term calendars, the ICT curriculum (build_ict.py), the Maths Y1
curriculum (build_maths_y1.py) and blank Malay Enrichment Y8 rows into
src/data/seed.json.

Run, in order:
  python scripts/extract_sow.py       # Term 1 calendar from the workbook
  python scripts/build_terms23.py     # Term 2/3 week calendars
  python scripts/build_seed.py        # merge everything + assign moral content

Output shape:
  { "terms": [Term, Term, Term], "lessons": [Lesson] }  -- what /admin writes
  to Firestore. (The browser Excel-upload path, src/lib/parseSow.ts, is a
  separate, independent way to re-import Term 1 dates/topics from a
  workbook and does not go through this script.)
"""
import json
import os

from values import assign_ice_breaker, assign_moral_content
from build_maths_y1 import build_maths_y1_lessons
from build_ict import build_all_ict_lessons

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "src", "data")
RAW = os.path.join(DATA, "sow.raw.json")
TERMS23 = os.path.join(DATA, "terms23.json")
OUT = os.path.join(DATA, "seed.json")

# classId -> weekly session days (JS Date.getDay() convention, Mon=1..Fri=5),
# for classes that meet more than once a week and need one lesson per session
# instead of one shared lesson for the whole week. Matches SLOTS in
# src/data/timetable.ts.
BLANK_CLASSES = [
    {"classId": "me-y8", "subject": "Malay Enrichment", "days": [1, 2]},
]
DAY_SHORT = {1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri"}
EMPTY = {"objectives": [], "plan": [], "activities": [], "successCriteria": [], "resources": []}


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

    term1_cal = {w["no"]: w for w in raw["term"]["weeks"] if not w["isBreak"]}
    term2_cal = {w["no"]: w for w in terms23["term2"]["weeks"] if not w["isBreak"]}
    term3_cal = {w["no"]: w for w in terms23["term3"]["weeks"] if not w["isBreak"]}

    ict_lessons = build_all_ict_lessons(term1_cal, term2_cal, term3_cal)

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

    lessons = ict_lessons + blanks + maths_y1_lessons
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
