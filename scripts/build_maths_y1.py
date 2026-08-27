"""Turns scripts/maths_y1_content.py's weekly topics into 3 per-session Lesson
dicts each (Tue/Thu/Fri), so Maths Y1's 3 weekly sessions are independently
plannable and markable Done instead of sharing one lesson doc for the week.
"""

from maths_y1_content import TERMS

CLASS_ID = "maths-y1"
SUBJECT = "Mathematics"

# JS Date.getDay() convention: Mon=1 .. Fri=5, matching Slot.day in timetable.ts.
SESSION_DAYS = [2, 4, 5]  # Tue, Thu, Fri
DAY_SHORT = {1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri"}


def day_variant(day: int, topic: str, subtopic: str) -> dict:
    if day == 2:  # Tue — explore
        return {
            "plan": [
                {
                    "mins": 10,
                    "title": "Warm-up: number chat",
                    "detail": f"Quick counting rhyme or chant related to '{topic}'. Cold-call 3-4 pupils to check confidence coming in.",
                    "studentActivity": "Join in the rhyme/chant and answer when called on.",
                    "assessment": "Listen for pupils who hesitate or get lost — note names to support in the guided activity.",
                },
                {
                    "mins": 15,
                    "title": f"Introduce: {subtopic}",
                    "detail": f"Model '{subtopic}' on the board/carpet using manipulatives. Think aloud each step.",
                    "studentActivity": "Watch and repeat back key vocabulary when prompted.",
                    "assessment": "Thumbs up/down check: 'does that make sense so far?'",
                },
                {
                    "mins": 20,
                    "title": "Hands-on exploration",
                    "detail": f"In small groups, pupils explore '{topic}' hands-on with manipulatives, teacher circulates.",
                    "studentActivity": "Explore the resources in pairs or small groups, trying the idea out themselves.",
                    "assessment": "Circulate and listen to pupil talk; jot down 2-3 names who need more support next session.",
                },
                {
                    "mins": 10,
                    "title": "Plenary: what did we notice?",
                    "detail": "Bring the class back together. Ask 2-3 pupils to share what they noticed.",
                    "studentActivity": "Share one thing they noticed or found tricky.",
                    "assessment": "Show of hands: who feels ready to practise this on their own next session?",
                },
            ],
            "activities": [
                f"Hands-on exploration of {topic.lower()} with manipulatives",
                f"Whole-class modelling of {subtopic.lower()}",
                "Turn-and-talk: explain what we noticed to a partner",
            ],
            "successCriteria": [
                f"I am starting to understand {topic.lower()}.",
                f"I can join in exploring {subtopic.lower()} with support.",
                "I can talk about what I noticed.",
            ],
        }
    if day == 4:  # Thu — practise
        return {
            "plan": [
                {
                    "mins": 10,
                    "title": "Recap",
                    "detail": f"Quick recap of '{topic}' from Tuesday — 2-3 quick-fire questions.",
                    "studentActivity": "Answer quick-fire questions on mini-whiteboards.",
                    "assessment": "Scan whiteboards for common misconceptions before moving on.",
                },
                {
                    "mins": 15,
                    "title": "Worked example",
                    "detail": f"Model 1-2 worked examples of '{subtopic}', narrating each step.",
                    "studentActivity": "Copy the worked example and try one alongside the teacher.",
                    "assessment": "Check the copied example matches before releasing to independent work.",
                },
                {
                    "mins": 20,
                    "title": "Practice task",
                    "detail": f"Pupils work through a practice task on '{topic}'; teacher supports lower-confidence pupils in a small group.",
                    "studentActivity": "Complete the practice task independently or in pairs, using resources as needed.",
                    "assessment": "Check 2-3 completed examples per pupil while circulating; note who needs Friday's small group.",
                },
                {
                    "mins": 10,
                    "title": "Mini plenary",
                    "detail": "Share 1-2 pupil examples on the board and discuss.",
                    "studentActivity": "Explain their answer to the class or a partner.",
                    "assessment": "Quick thumbs up/down: 'did you get this right?'",
                },
            ],
            "activities": [
                f"Practice task: {subtopic.lower()}",
                "Paired check: swap books and check a partner's work",
                "Small-group support table for pupils needing extra help",
            ],
            "successCriteria": [
                f"I can {subtopic.lower()} with a little help.",
                f"I can explain how I solved a {topic.lower()} problem.",
                "I can check my own or a partner's work.",
            ],
        }
    # Fri — consolidate
    return {
        "plan": [
            {
                "mins": 10,
                "title": "Recap game",
                "detail": f"Fast-paced recap game (quiz, bingo or 'show me') covering '{topic}' from the week.",
                "studentActivity": "Play the recap game, showing answers on whiteboards or with actions.",
                "assessment": "Note any pupil still unsure of the core idea for next week's starter.",
            },
            {
                "mins": 20,
                "title": "Show what you know",
                "detail": f"Pupils complete a short independent task pulling together '{topic}' and '{subtopic}' from the week.",
                "studentActivity": "Complete the task independently, using resources only if needed.",
                "assessment": "Check books — this is the week's main evidence of progress.",
            },
            {
                "mins": 15,
                "title": "Challenge extension",
                "detail": "Early finishers try a harder version, or explain their thinking to a partner still working.",
                "studentActivity": "Attempt the challenge version, or teach a partner who is still working.",
                "assessment": "Listen in on pupil explanations — a good sign of secure understanding.",
            },
            {
                "mins": 10,
                "title": "Reflect and celebrate",
                "detail": "Celebrate what the class achieved this week; preview next week's topic in one sentence.",
                "studentActivity": "Share one thing they are proud of from this week.",
                "assessment": "Quick temperature check (thumbs) on confidence with this week's topic.",
            },
        ],
        "activities": [
            f"Independent show-what-you-know task on {topic.lower()}",
            "Challenge extension for early finishers",
            "Reflect and share: one thing I'm proud of",
        ],
        "successCriteria": [
            f"I can {subtopic.lower()} independently.",
            f"I can show what I know about {topic.lower()} without help.",
            "I can talk about what I'm proud of this week.",
        ],
    }


def build_maths_y1_lessons(term_id: str, weeks_by_week_no: dict) -> list:
    """weeks_by_week_no: {weekNo: TermWeek dict} for teaching weeks only."""
    topics = TERMS[term_id]
    ordered_weeks = sorted(weeks_by_week_no.items(), key=lambda kv: kv[0])
    if len(ordered_weeks) != len(topics):
        raise SystemExit(
            f"{term_id}: {len(ordered_weeks)} calendar weeks but {len(topics)} maths_y1_content topics"
        )
    out = []
    order = 0
    for (week_no, cal), week_topic in zip(ordered_weeks, topics):
        for day in SESSION_DAYS:
            variant = day_variant(day, week_topic["topic"], week_topic["subtopic"])
            out.append(
                {
                    "id": f"{CLASS_ID}_{term_id}_w{week_no}_d{day}",
                    "classId": CLASS_ID,
                    "subject": SUBJECT,
                    "termId": term_id,
                    "weekNo": week_no,
                    "weekLabel": f"{cal['label']} ({DAY_SHORT[day]})",
                    "dateStart": cal["start"],
                    "dateEnd": cal["end"],
                    "day": day,
                    "topic": week_topic["topic"],
                    "subtopic": week_topic["subtopic"],
                    "outline": "",
                    "sowResources": "",
                    "remark": cal.get("remark", ""),
                    "objectives": week_topic["objectives"],
                    "plan": variant["plan"],
                    "activities": variant["activities"],
                    "successCriteria": variant["successCriteria"],
                    "resources": [{"label": r} for r in week_topic["resources"]],
                    "status": "planned",
                    "note": "",
                    "order": order,
                }
            )
            order += 1
    return out
