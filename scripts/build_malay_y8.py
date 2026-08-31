"""Turns malay_y8_content.py's weekly themes into 2 per-session Lesson dicts
each (Mon/Tue), so Malay Enrichment Y8's 2 weekly sessions are independently
plannable and markable Done.
"""

from malay_y8_content import TERMS

CLASS_ID = "me-y8"
SUBJECT = "Malay Enrichment"

# JS Date.getDay() convention: Mon=1, Tue=2, matching Slot.day in timetable.ts.
SESSION_DAYS = [1, 2]
DAY_SHORT = {1: "Mon", 2: "Tue"}


def day_variant(day: int, topic: str, subtopic: str) -> dict:
    if day == 1:  # Mon — teach (75 min, all 4 skills introduced)
        return {
            "plan": [
                {
                    "mins": 10,
                    "title": "Warm-up: greetings and quick review",
                    "detail": f"Greet the class in Malay and do a 2-minute quick review of last session before introducing '{topic}'.",
                    "studentActivity": "Respond to the greeting in Malay and answer 1-2 quick review questions.",
                    "assessment": "Listen for confident, automatic responses to the greeting routine.",
                },
                {
                    "mins": 20,
                    "title": f"Listen and repeat: {subtopic}",
                    "detail": f"Model the new vocabulary/phrases for '{subtopic}' with clear pronunciation (audio if available), pupils listen and repeat chorally, then in pairs.",
                    "studentActivity": "Listen carefully and repeat each new word or phrase, first as a class, then with a partner.",
                    "assessment": "Listen for accurate pronunciation; note 2-3 pupils who need extra modelling.",
                },
                {
                    "mins": 25,
                    "title": "Speak and read",
                    "detail": f"In pairs, pupils practise saying the new '{subtopic}' phrases aloud, then read them from cards/the board.",
                    "studentActivity": "Take turns speaking the new phrases with a partner, then read them aloud together.",
                    "assessment": "Circulate and listen to pair talk; give quick pronunciation feedback.",
                },
                {
                    "mins": 15,
                    "title": "Write",
                    "detail": f"Pupils write 1-2 sentences using today's '{subtopic}' vocabulary, modelled first on the board.",
                    "studentActivity": "Write their own sentence(s), checking spelling against the board model.",
                    "assessment": "Check 2-3 pupils' sentences while circulating; note common spelling slips for Tuesday.",
                },
                {
                    "mins": 5,
                    "title": "Plenary",
                    "detail": "Cold-call 2-3 pupils to say one new word or phrase from today.",
                    "studentActivity": "Share one new word or phrase they learned today.",
                    "assessment": "Quick thumbs up/down on confidence with today's vocabulary.",
                },
            ],
            "activities": [
                f"Listen-and-repeat drill: {subtopic}",
                "Paired speaking practice",
                f"Short writing task using {topic.lower()} vocabulary",
            ],
            "successCriteria": [
                f"I can listen to and repeat new words/phrases about {topic.lower()}.",
                f"I can say a short phrase about {subtopic.lower()} with a partner.",
                "I can write 1-2 sentences using today's new vocabulary.",
            ],
        }
    # Tue — practise (35 min, shorter game-based consolidation)
    return {
        "plan": [
            {
                "mins": 5,
                "title": "Quick greeting and recap",
                "detail": f"Greet the class in Malay and recap Monday's key words for '{topic}' with a rapid-fire round.",
                "studentActivity": "Respond to the greeting and answer the rapid-fire recap questions.",
                "assessment": "Note which words/phrases from Monday still need reinforcing.",
            },
            {
                "mins": 20,
                "title": f"Game: {subtopic}",
                "detail": f"Run a short game (e.g. flashcard matching, Bingo, or a speaking chain) practising '{subtopic}' vocabulary from Monday.",
                "studentActivity": "Play the game in pairs or small groups, using the target vocabulary as much as possible.",
                "assessment": "Listen in on pupil talk during the game; note who is using vocabulary confidently and unprompted.",
            },
            {
                "mins": 8,
                "title": "Speaking challenge",
                "detail": f"In pairs, pupils have a very short conversation using at least 2 phrases from '{subtopic}'.",
                "studentActivity": "Have a short paired conversation using today's target phrases.",
                "assessment": "Listen to 2-3 pairs; note pronunciation or confidence to address next Monday.",
            },
            {
                "mins": 2,
                "title": "Plenary",
                "detail": "Quick class check: thumbs up if they feel confident with this week's vocabulary.",
                "studentActivity": "Give a thumbs up/down/sideways on their confidence this week.",
                "assessment": "Use the show of hands to plan who needs extra support next week.",
            },
        ],
        "activities": [
            f"Vocabulary game: {subtopic}",
            "Short paired speaking challenge",
            "Confidence check-in",
        ],
        "successCriteria": [
            f"I can use {topic.lower()} vocabulary in a game.",
            f"I can have a short conversation using {subtopic.lower()} phrases.",
            "I know how confident I feel with this week's Malay.",
        ],
    }


def build_malay_y8_lessons(term_id: str, weeks_by_week_no: dict) -> list:
    """weeks_by_week_no: {weekNo: TermWeek dict} for teaching weeks only."""
    topics = TERMS[term_id]
    ordered_weeks = sorted(weeks_by_week_no.items(), key=lambda kv: kv[0])
    if len(ordered_weeks) != len(topics):
        raise SystemExit(
            f"{term_id}: {len(ordered_weeks)} calendar weeks but {len(topics)} malay_y8_content topics"
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
