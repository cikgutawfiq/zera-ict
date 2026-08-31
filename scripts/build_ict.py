"""Expands ict_content.py's week specs into full Lesson dicts: one lesson
per class per week (ICT classes meet once/week), across all 3 terms.

Each content week gets a single-session plan (Starter / Teach & model /
Main task / Plenary) whose wording adapts to that week's equipmentMode, so
"unplugged" weeks read as genuinely device-free and "shared-laptops" weeks
read as genuinely group-rotation, rather than one generic template pasted
41 times with the topic swapped in.
"""

from ict_content import build_class_weeks, CLASS_KEY_STAGE, PROJECTS

CLASS_ID = None  # set by caller loop
SUBJECT = "ICT"

DEVICE_NOTE = {
    "unplugged": "No devices needed this session — everything happens on paper, through discussion, or moving around the room.",
    "shared-laptops": "Laptops are shared: put pupils in groups of 4-5 around one laptop, rotating who is 'hands on the keyboard' every few minutes so everyone gets a turn.",
    "1-1-devices": "Each pupil (or pair, if devices are limited) works on their own device for this session.",
}

STARTER_TEMPLATE = {
    "unplugged": "Gather in a circle, away from any devices. Quick recap or hook question related to '{topic}'.",
    "shared-laptops": "Gather pupils away from the laptops first. Quick recap or hook question related to '{topic}', then explain today's groups and roles.",
    "1-1-devices": "Pupils log in and sit ready. Quick recap or hook question related to '{topic}' before opening today's tool.",
}

MODEL_TEMPLATE = {
    "unplugged": "Model today's focus step by step using the unplugged materials (cards, diagrams, movement), thinking aloud.",
    "shared-laptops": "Model today's focus step by step on the board or a demo device, thinking aloud.",
    "1-1-devices": "Model today's focus step by step on the board, thinking aloud, then let pupils try the first step alongside you.",
}

MAIN_TEMPLATE = {
    "unplugged": "In pairs or small groups, work through a hands-on paper-and-movement task on today's focus — no screens involved.",
    "shared-laptops": "In groups of 4-5 around one laptop, work through today's focus, rotating who is hands-on every few minutes so everyone contributes.",
    "1-1-devices": "Individually (or in pairs if devices are shared), work through today's focus, applying what was modelled.",
}

MAIN_STUDENT_TEMPLATE = {
    "unplugged": "Work through the unplugged task with a partner or small group, explaining their thinking out loud.",
    "shared-laptops": "Take turns being 'hands on the keyboard', and help teammates when it's not their turn.",
    "1-1-devices": "Work through the task, asking for help if stuck, and check their work against the model.",
}


def session_plan(topic: str, subtopic: str, mode: str) -> list:
    return [
        {
            "mins": 10,
            "title": "Starter",
            "detail": STARTER_TEMPLATE[mode].format(topic=topic),
            "studentActivity": "Join in the recap/hook and share ideas.",
            "assessment": "Cold-call 2-3 pupils to gauge starting confidence.",
        },
        {
            "mins": 15,
            "title": f"Teach & model: {subtopic}",
            "detail": MODEL_TEMPLATE[mode].format(subtopic=subtopic),
            "studentActivity": "Watch, and repeat back key vocabulary when prompted.",
            "assessment": "Thumbs up/down check before releasing to the main task.",
        },
        {
            "mins": 30,
            "title": "Main task",
            "detail": MAIN_TEMPLATE[mode].format(subtopic=subtopic),
            "studentActivity": MAIN_STUDENT_TEMPLATE[mode],
            "assessment": "Circulate and support; note 2-3 pupils/groups to check in on first next session.",
        },
        {
            "mins": 10,
            "title": "Plenary",
            "detail": "Bring the class/groups back together. 2-3 pupils or groups share what they made or found.",
            "studentActivity": "Share one thing they made, tried or found tricky.",
            "assessment": "Quick show of hands on confidence with today's focus.",
        },
    ]


def build_week_lesson(class_id, term_id, week_no, cal, week_spec, order):
    topic, subtopic, mode = week_spec["topic"], week_spec["subtopic"], week_spec["equipmentMode"]
    key_stage = CLASS_KEY_STAGE[class_id]
    return {
        "id": f"{class_id}_{term_id}_w{week_no}",
        "classId": class_id,
        "subject": SUBJECT,
        "termId": term_id,
        "weekNo": week_no,
        "weekLabel": cal["label"],
        "dateStart": cal["start"],
        "dateEnd": cal["end"],
        "equipmentMode": mode,
        "topic": topic,
        "subtopic": subtopic,
        "outline": week_spec.get("source", ""),
        "sowResources": "",
        "remark": cal.get("remark", ""),
        "objectives": [
            f"Understand what '{topic}' involves and why it matters.",
            f"Practise '{subtopic}' with the right level of support for {key_stage}.",
            "Talk about their work using the correct vocabulary.",
        ],
        "plan": session_plan(topic, subtopic, mode),
        "activities": [
            f"Main task: {subtopic}",
            {
                "unplugged": f"Unplugged partner/group task on {topic.lower()}",
                "shared-laptops": f"Shared-laptop group task on {topic.lower()}",
                "1-1-devices": f"Independent device task on {topic.lower()}",
            }[mode],
            "Plenary share-back",
        ],
        "successCriteria": [
            f"I can talk about {topic.lower()}.",
            f"I had a go at {subtopic.lower()}.",
            "I shared what I made or found with the class.",
        ],
        "resources": [{"label": DEVICE_NOTE[mode]}],
        "status": "planned",
        "note": "",
        "order": order,
    }


META_PLAN_NOTE = {
    "unplugged": "No devices needed — this is a review/discussion session.",
    "shared-laptops": "Shared laptops, groups of 4-5, rotating roles.",
    "1-1-devices": "Each pupil on their own device.",
}


def meta_lesson(class_id, term_id, week_no, cal, topic, subtopic, order, mode="shared-laptops"):
    is_project = topic.startswith("End of Term Project") or topic == "Portfolio Showcase"
    if is_project:
        objectives = [
            f"Make progress on the term's project: {subtopic if not subtopic.startswith('Present') else topic}.",
            "Apply skills learned this term to a real, finished piece of work.",
            "Give and receive feedback from a partner or group.",
        ]
    else:
        objectives = [
            "Revisit and strengthen this term's skills.",
            "Identify what feels secure and what still needs practice.",
            "Support a partner with a skill they find secure.",
        ]
    return {
        "id": f"{class_id}_{term_id}_w{week_no}",
        "classId": class_id,
        "subject": SUBJECT,
        "termId": term_id,
        "weekNo": week_no,
        "weekLabel": cal["label"],
        "dateStart": cal["start"],
        "dateEnd": cal["end"],
        "equipmentMode": mode,
        "topic": topic,
        "subtopic": subtopic,
        "outline": "",
        "sowResources": "",
        "remark": cal.get("remark", ""),
        "objectives": objectives,
        "plan": [
            {
                "mins": 10,
                "title": "Recap",
                "detail": (
                    f"Quick recap of progress so far on '{topic}'."
                    if is_project
                    else f"Quick recap of the term's work on {subtopic.lower()}."
                ),
                "studentActivity": "Share what they remember.",
                "assessment": "Note common gaps to target in the main task.",
            },
            {
                "mins": 35,
                "title": "Main task",
                "detail": (
                    f"{topic} — {subtopic} stage. {META_PLAN_NOTE[mode]}"
                    if is_project
                    else f"{subtopic} — {META_PLAN_NOTE[mode]}"
                ),
                "studentActivity": "Work through the task, choosing an area to focus on.",
                "assessment": "Circulate and support; identify pupils needing extra help before the practical check.",
            },
            {
                "mins": 20,
                "title": "Share and reflect",
                "detail": "Pupils or groups share progress; class discusses what's ready and what needs more time.",
                "studentActivity": "Share progress and one thing they're proud of.",
                "assessment": "Quick self-assessment (thumbs) on readiness.",
            },
        ],
        "activities": [subtopic, "Peer support", "Share and reflect"],
        "successCriteria": [
            "I know which skills from this term I'm confident with.",
            "I know which skills I still need to practise.",
            "I helped or was helped by a partner.",
        ],
        "resources": [{"label": META_PLAN_NOTE[mode]}],
        "status": "planned",
        "note": "",
        "order": order,
    }


def build_class_term_lessons(class_id, term_id, weeks_by_week_no, content_weeks, term_index):
    """weeks_by_week_no: {weekNo: TermWeek dict}, all weeks (incl. meta) for this term.
    content_weeks: this term's slice (8) of the 24 class content weeks.
    term_index: 1, 2 or 3."""
    ordered = sorted(weeks_by_week_no.items(), key=lambda kv: kv[0])
    out = []
    order = 0

    n_content = len(content_weeks)
    for i in range(n_content):
        week_no, cal = ordered[i]
        out.append(build_week_lesson(class_id, term_id, week_no, cal, content_weeks[i], order))
        order += 1

    meta = [(t, s) for t, s in _meta_sequence(term_index, class_id)]
    for j, (topic, subtopic) in enumerate(meta):
        week_no, cal = ordered[n_content + j]
        mode = "unplugged" if topic in ("Consolidation", "Revision") else "shared-laptops"
        out.append(meta_lesson(class_id, term_id, week_no, cal, topic, subtopic, order, mode))
        order += 1

    assert len(ordered) == n_content + len(meta), (
        f"{class_id} {term_id}: {len(ordered)} calendar weeks, "
        f"{n_content} content + {len(meta)} meta = {n_content + len(meta)}"
    )
    return out


def _meta_sequence(term_index, class_id):
    seq = [
        ("Consolidation", "Whole-unit skills rotation"),
        ("Revision", "Ready for the practical check"),
        ("Examination Week", f"Term {term_index} Practical Assessment"),
    ]
    if term_index in (1, 3):
        project = PROJECTS[class_id][term_index]
        seq += [
            (f"End of Term Project — {project}", "Plan"),
            (f"End of Term Project — {project}", "Build"),
            (f"End of Term Project — {project}", "Refine and prepare to present"),
            ("Portfolio Showcase", f"Present: {project}"),
        ]
    return seq


def build_all_ict_lessons(term1_cal, term2_cal, term3_cal):
    out = []
    for class_id in CLASS_KEY_STAGE:
        weeks = build_class_weeks(class_id)
        t1, t2, t3 = weeks[0:8], weeks[8:16], weeks[16:24]
        out += build_class_term_lessons(class_id, "term-1", term1_cal, t1, 1)
        out += build_class_term_lessons(class_id, "term-2", term2_cal, t2, 2)
        out += build_class_term_lessons(class_id, "term-3", term3_cal, t3, 3)
    return out
