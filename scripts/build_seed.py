"""Merge the extracted SOW with the authored lesson content into src/data/seed.json.

Run:  python scripts/extract_sow.py && python scripts/build_seed.py

Output shape:
  { "terms": [Term], "lessons": [Lesson] }   -- exactly what /admin writes to Firestore.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "src", "data")
RAW = os.path.join(DATA, "sow.raw.json")
AUTHORED = os.path.join(DATA, "authored")
OUT = os.path.join(DATA, "seed.json")

TERM_ID = "term-1"

# Classes seeded from the SOW workbooks.
ICT_YEARS = list(range(1, 10))
# Classes that appear on the timetable but have no SOW: seeded as blank week rows.
BLANK_CLASSES = [
    {"classId": "maths-y1", "subject": "Mathematics"},
    {"classId": "me-y8", "subject": "Malay Enrichment"},
]

EMPTY = {"objectives": [], "plan": [], "activities": [], "successCriteria": [], "resources": []}


def lesson_id(class_id: str, week_no: int) -> str:
    return f"{class_id}_{TERM_ID}_w{week_no}"


def main():
    raw = json.load(open(RAW, encoding="utf-8"))
    lessons = []

    for year in ICT_YEARS:
        class_id = f"ict-y{year}"
        authored_path = os.path.join(AUTHORED, f"y{year}.json")
        authored = json.load(open(authored_path, encoding="utf-8"))
        rows = [r for r in raw["years"][str(year)] if not r["isBreak"]]
        for order, row in enumerate(rows):
            week = row["weekNo"]
            extra = authored.get(str(week))
            if extra is None:
                raise SystemExit(f"missing authored content: year {year} week {week}")
            lessons.append(
                {
                    "id": lesson_id(class_id, week),
                    "classId": class_id,
                    "subject": "ICT",
                    "termId": TERM_ID,
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

    # Blank rows for the timetabled classes that have no scheme of work yet.
    calendar = [w for w in raw["term"]["weeks"] if not w["isBreak"]]
    for spec in BLANK_CLASSES:
        for order, week in enumerate(calendar):
            lessons.append(
                {
                    "id": lesson_id(spec["classId"], week["no"]),
                    "classId": spec["classId"],
                    "subject": spec["subject"],
                    "termId": TERM_ID,
                    "weekNo": week["no"],
                    "weekLabel": week["label"],
                    "dateStart": week["start"],
                    "dateEnd": week["end"],
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

    payload = {"terms": [raw["term"]], "lessons": lessons}
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1, ensure_ascii=False)

    ict = sum(1 for x in lessons if x["subject"] == "ICT")
    print(f"lessons: {len(lessons)} total ({ict} ICT, {len(lessons) - ict} blank)")
    print(f"term weeks: {len(raw['term']['weeks'])} ({len(calendar)} teaching)")
    print(f"wrote {os.path.abspath(OUT)}")


if __name__ == "__main__":
    main()
