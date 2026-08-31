"""Merges the term calendars, the ICT curriculum (build_ict.py), the Maths Y1
curriculum (build_maths_y1.py) and the Malay Enrichment Y8 curriculum
(build_malay_y8.py) into src/data/seed.json.

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
from build_malay_y8 import build_malay_y8_lessons
from build_ict import build_all_ict_lessons

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "src", "data")
RAW = os.path.join(DATA, "sow.raw.json")
TERMS23 = os.path.join(DATA, "terms23.json")
OUT = os.path.join(DATA, "seed.json")


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

    maths_y1_lessons = (
        build_maths_y1_lessons("term-1", term1_cal)
        + build_maths_y1_lessons("term-2", term2_cal)
        + build_maths_y1_lessons("term-3", term3_cal)
    )

    malay_y8_lessons = (
        build_malay_y8_lessons("term-1", term1_cal)
        + build_malay_y8_lessons("term-2", term2_cal)
        + build_malay_y8_lessons("term-3", term3_cal)
    )

    lessons = ict_lessons + maths_y1_lessons + malay_y8_lessons
    attach_moral_content(lessons)

    terms = [raw["term"], terms23["term2"], terms23["term3"]]
    payload = {"terms": terms, "lessons": lessons}

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1, ensure_ascii=False)

    ict = sum(1 for x in lessons if x["subject"] == "ICT")
    maths = sum(1 for x in lessons if x["subject"] == "Mathematics")
    malay = sum(1 for x in lessons if x["subject"] == "Malay Enrichment")
    print(f"lessons: {len(lessons)} total ({ict} ICT, {maths} Maths Y1, {malay} Malay Enrichment Y8)")
    for t in terms:
        print(f"  {t['name']}: {len(t['weeks'])} weeks")
    print(f"wrote {os.path.abspath(OUT)}")


if __name__ == "__main__":
    main()
