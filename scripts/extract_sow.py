"""Extract the ICT Scheme of Work workbooks into src/data/sow.raw.json.

Run:  python scripts/extract_sow.py
Source workbooks live in ~/Downloads (override with SOW_DIR env var).
"""
import json
import os
import re
from datetime import date

import openpyxl

SOW_DIR = os.environ.get("SOW_DIR", os.path.expanduser("~/Downloads"))
FILES = [
    ("KS1_KS2", "SOW_ICT_KS1_KS2_Y1-6_2026-2027.xlsx", [1, 2, 3, 4, 5, 6]),
    ("KS3", "SOW_ICT_KS3_Y7-9_2026-2027.xlsx", [7, 8, 9]),
]
HEADER_ROW = 8
OUT = os.path.join(os.path.dirname(__file__), "..", "src", "data", "sow.raw.json")

DATE_RANGE = re.compile(r"(\d{1,2})\.(\d{1,2})\.(\d{4})\s*[-–]\s*(\d{1,2})\.(\d{1,2})\.(\d{4})")


def clean(value):
    if value is None:
        return ""
    text = str(value).replace("\xa0", " ").replace("\u2192", "->")
    return re.sub(r"[ \t]+", " ", text).strip()


def parse_dates(text):
    m = DATE_RANGE.search(text or "")
    if not m:
        return None, None
    d1, m1, y1, d2, m2, y2 = (int(x) for x in m.groups())
    return date(y1, m1, d1).isoformat(), date(y2, m2, d2).isoformat()


def week_number(label):
    m = re.search(r"(\d+)", label or "")
    return int(m.group(1)) if m else None


def read_year(ws):
    rows = []
    for row in ws.iter_rows(min_row=HEADER_ROW + 1, values_only=True):
        cells = [clean(c) for c in row]
        while len(cells) < 7:
            cells.append("")
        week_label, dates, topic, subtopic, outline, resources, remark = cells[:7]
        if not any([week_label, dates, topic, subtopic, outline]):
            continue
        start, end = parse_dates(dates)
        is_break = "break" in topic.lower() or not week_label
        rows.append(
            {
                "weekLabel": week_label or "Break",
                "weekNo": week_number(week_label),
                "dateText": dates,
                "dateStart": start,
                "dateEnd": end,
                "topic": topic,
                "subtopic": subtopic,
                "outline": outline,
                "sowResources": resources,
                "remark": remark,
                "isBreak": is_break,
                "isExam": "exam" in topic.lower(),
            }
        )
    return rows


def main():
    out = {"term": {"id": "term-1", "name": "Term 1", "order": 1, "weeks": []}, "years": {}}
    for _key, filename, years in FILES:
        path = os.path.join(SOW_DIR, filename)
        wb = openpyxl.load_workbook(path, data_only=True)
        for year in years:
            sheet = f"YEAR {year}"
            rows = read_year(wb[sheet])
            out["years"][str(year)] = rows
            print(f"{sheet}: {len(rows)} rows ({sum(1 for r in rows if not r['isBreak'])} teaching weeks)")

    # Canonical term calendar, taken from Year 1 (identical across every year sheet).
    for row in out["years"]["1"]:
        out["term"]["weeks"].append(
            {
                "no": row["weekNo"],
                "label": row["weekLabel"],
                "start": row["dateStart"],
                "end": row["dateEnd"],
                "isBreak": row["isBreak"],
                "isExam": row["isExam"],
                "remark": row["remark"],
            }
        )

    # Sanity: every year must share the same week dates.
    base = [(w["start"], w["end"]) for w in out["term"]["weeks"]]
    for year, rows in out["years"].items():
        got = [(r["dateStart"], r["dateEnd"]) for r in rows]
        if got != base:
            print(f"WARNING: Year {year} week dates differ from Year 1")

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False)
    print(f"wrote {os.path.abspath(OUT)}")


if __name__ == "__main__":
    main()
