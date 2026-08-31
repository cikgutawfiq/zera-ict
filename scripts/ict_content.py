"""ICT Y1-Y9 curriculum spine.

Y1-Y6 unit titles come from Oak National Academy's Computing (Primary)
programme (https://www.thenational.academy/teachers/programmes/computing-
primary/units) -- real unit names/order, not verbatim Oak lesson content.
Each Oak unit (6 Oak lessons) is expanded into 2 of our weekly sessions
("Explore & learn" then "Create & share"), since our classes get a full
weekly double period rather than Oak's more occasional slot.

Y7-Y9 have no Oak *primary* units to draw on, so these are original KS3
Computing units, written for more depth and explicit groupwork.

Every class also gets, in this order:
  1. 8 "settling in" weeks at the very start of Term 1 (equipmentMode
     unplugged/shared-laptops) -- for the first ~2 months, while laptop
     access may be limited (as few as 4 shared machines in rotating groups).
  2. The Oak-unit (Y1-6) or original KS3-unit (Y7-9) weeks.
  3. Flexible custom slots (Typing Club, Microsoft 365, Google Workspace,
     independent project time) filling out the rest of the 24-content-week
     year -- swap, reorder or edit any of these in the app; every field
     stays editable per lesson.

24 content weeks + the existing 17 consolidation/revision/exam/project/
showcase weeks = 41, split 8/8/8 across Term 1/2/3 (content) same as before.
"""

UNPLUGGED_WEEKS = {
    "KS1": [
        ("Meet the Computer", "Labelling a Computer Poster"),
        ("ICT Room Rules", "Agreeing How We Look After Equipment"),
        ("Keyboard and Mouse Match-Up", "Matching Keys and Mouse Actions to Pictures"),
        ("Being Safe Online", "Telling a Trusted Adult"),
        ("Being Kind Online", "Kind and Unkind Messages, Role-Played"),
        ("Giving Instructions", "The Unplugged 'Robot' Game"),
        ("Sorting and Patterns", "Sorting Objects and Spotting Patterns"),
        ("First Look at a Shared Laptop", "Switching On and Logging In, in Groups of 4"),
    ],
    "KS2": [
        ("What Is a Computer System?", "Labelling the Parts of a Computer System"),
        ("ICT Room Routines and Digital Citizenship", "Agreeing Expectations for Equipment and Online Behaviour"),
        ("Algorithms Unplugged", "Giving and Following Step-by-Step Instructions"),
        ("Sequencing and Debugging Unplugged", "Spotting and Fixing the 'Bug' in Written Instructions"),
        ("How the Internet Works, Unplugged", "A Human-Network Message-Passing Game"),
        ("Online Safety Case Studies", "Discussing Real-World Scenario Cards"),
        ("Binary and Logic Puzzles", "Unplugged Binary Counting and Logic Puzzles"),
        ("First Look at Shared Laptops", "Exploring the Desktop and File Structure Together"),
    ],
    "KS3": [
        ("How Computers Really Work", "An Unplugged Model of CPU, Memory and Storage"),
        ("Networks Unplugged", "Building a Human Network Diagram"),
        ("Algorithms and Pseudocode on Paper", "Tracing and Writing Algorithms by Hand"),
        ("Cybersecurity Case Studies", "Analysing Real-World Breach Case Studies"),
        ("Data Ethics Debate", "Who Owns Your Data Online?"),
        ("Binary, Logic and Boolean Puzzles", "Unplugged Binary and Logic Challenge Stations"),
        ("Careers in Computing", "Researching and Presenting a Computing Career"),
        ("First Look at Shared Devices", "Exploring the School's Device Setup Together"),
    ],
}

# Oak National Academy Computing (Primary) unit titles, Y1-Y6, in their
# published order.
OAK_UNITS = {
    "ict-y1": ["Digital painting", "Digital writing", "Creating animations in programs"],
    "ict-y2": [
        "Information technology in the world beyond school",
        "Using IT to organise and present data",
        "Building sequences in programs",
    ],
    "ict-y3": [
        "Computer networks",
        "Stop-frame animation",
        "Programming sequence using sound",
        "Organising data using databases",
        "Desktop publishing",
        "Events and actions in programs",
    ],
    "ict-y4": [
        "The internet",
        "Audio production",
        "Repetition in programs",
        "Data logging",
        "Photo editing",
        "Using repetition in programming to create a game",
    ],
    "ict-y5": [
        "Introduction to computer systems",
        "Video production",
        "Exploring selection in physical computing",
        "Flat-file databases",
        "Introduction to vector graphics",
        "Using selection in programming to develop a quiz",
    ],
    "ict-y6": [
        "Communication and the internet",
        "Web page creation",
        "Using variables in programming to develop a game",
        "Introduction to spreadsheets",
        "3D Modelling",
        "Sensing movement with physical computing",
    ],
}

# Original KS3 units (Y7-9): no Oak primary units apply here. Designed for
# more depth than Y1-6 and explicit groupwork every unit.
KS3_UNITS = {
    "ict-y7": [
        ("Networks and How the Internet Works", "groups build and present a network diagram of the school"),
        ("Python Fundamentals: Variables and Input/Output", "pair programming throughout"),
        ("Python Fundamentals: Selection and Loops", "pair programming with a group debugging challenge"),
        ("Productivity Deep Dive: Advanced Documents", "groups co-produce one shared report"),
        ("Data Representation: Binary and Images", "team puzzle stations, rotating every 10 minutes"),
        ("Group Project: Build a Simple Website", "teams of 3-4 build and present a multi-page site"),
    ],
    "ict-y8": [
        ("Cybersecurity and Digital Forensics", "groups investigate a case study and present findings"),
        ("Python: Functions and Lists", "pair programming with a code-review swap between pairs"),
        ("Spreadsheets: Modelling and Formulas", "groups build and present a shared data model"),
        ("Databases: Design and Query Basics", "groups design a database for a real scenario"),
        ("Media Project: Video or Podcast Production", "production teams of 3-4, roles rotate"),
        ("Group Hackathon: Solve a School Problem with Tech", "teams pitch, build and present a solution"),
    ],
    "ict-y9": [
        ("Advanced Python: Algorithms and Problem Solving", "pair programming, algorithm relay challenges"),
        ("Computer Systems and Architecture", "groups research a component and present to the class"),
        ("Web Development: Interactive Sites", "teams of 3-4 build an interactive site (HTML/CSS/JS basics)"),
        ("Data Science Basics: Analysing a Real Dataset", "groups investigate and present findings from real data"),
        ("Ethics and Impact of AI", "structured group debate with roles, then a class panel discussion"),
        ("Capstone Group Project: Pitch, Build, Present", "self-selected team project, presented to an audience"),
    ],
}

CUSTOM_POOL = {
    "KS1": [
        ("Typing Club — Home Row Warm-Up", "Find and practise the home-row keys, a few minutes at a time"),
        ("Typing Club — Building Speed", "Short, timed typing games to build confidence and speed"),
        ("Google Workspace — My Drive and Docs", "Create, name and save a simple document in Google Docs"),
        ("Microsoft Office — Word Basics", "Create, name and save a simple document in Word"),
        ("Digital Portfolio — Choosing My Best Work", "Pick a favourite piece of work and say why it's good"),
        ("Typing Club — Whole Keyboard Challenge", "Practise reaching beyond the home row, letter by letter"),
        ("Google Workspace — Slides: My First Presentation", "Make a 2-3 slide presentation about a favourite thing"),
        ("Microsoft Office — PowerPoint Basics", "Make a 2-3 slide presentation about a favourite thing"),
        ("Coding Playground — Free Choice", "A free-choice session with a simple block-coding tool"),
        ("Digital Portfolio — Show and Tell Prep", "Choose and rehearse sharing one piece of work with the class"),
    ],
    "KS2": [
        ("Typing Club — Speed and Accuracy Challenge", "A timed typing challenge, tracking personal-best progress"),
        ("Google Workspace — Docs, Sheets and Slides Refresher", "A mixed refresher task across the three tools"),
        ("Microsoft Office — Word, Excel and PowerPoint Refresher", "A mixed refresher task across the three tools"),
        ("Independent Project — Choose Your Own Mini-Challenge", "Pick a mini-challenge from a menu and complete it"),
    ],
    "KS3": [
        ("Typing Club — Professional Speed Challenge", "A timed challenge aiming for real touch-typing speed"),
        ("Productivity Masterclass — Google Workspace for Group Projects", "Shared docs, comments and version history for teamwork"),
        ("Productivity Masterclass — Microsoft 365 for Group Projects", "Co-authoring, comments and version history for teamwork"),
        ("Independent/Group Choice Project", "Pick a challenge from a menu, solo or in a self-formed group"),
    ],
}

# Each class's named End-of-Term project, one for Term 1 (built from the
# "settling-in" unplugged weeks — deliberately low-tech since T1 has limited
# device access) and one for Term 3 (a flagship build using skills from that
# class's Term 2 unit work). Shown directly in the Overview topic column as
# "End of Term Project - <name>".
PROJECTS = {
    "ict-y1": {
        1: "Being Safe & Kind Online Poster",
        3: "My Favourite Animal Fact-File",
    },
    "ict-y2": {
        1: "Our ICT Room Rules & Safety Guide",
        3: "My Hobby Data Survey",
    },
    "ict-y3": {
        1: "Internet Safety Campaign Poster",
        3: "Stop-Frame Animation Short Film",
    },
    "ict-y4": {
        1: "How the Internet Works Infographic",
        3: "My Own Simple Game",
    },
    "ict-y5": {
        1: "Computer Systems Explainer",
        3: "Class News Report (Video Production)",
    },
    "ict-y6": {
        1: "Staying Safe Online Campaign",
        3: "Build My Own Webpage",
    },
    "ict-y7": {
        1: "School Network Investigation Report",
        3: "Python Text Adventure Game",
    },
    "ict-y8": {
        1: "Cybersecurity Awareness Campaign",
        3: "School News Podcast/Video Series",
    },
    "ict-y9": {
        1: "Computer Systems Deep-Dive Report",
        3: "Data Science Investigation — Analysing a Real Dataset",
    },
}

CLASS_KEY_STAGE = {
    "ict-y1": "KS1",
    "ict-y2": "KS1",
    "ict-y3": "KS2",
    "ict-y4": "KS2",
    "ict-y5": "KS2",
    "ict-y6": "KS2",
    "ict-y7": "KS3",
    "ict-y8": "KS3",
    "ict-y9": "KS3",
}

CONTENT_WEEKS_TARGET = 24


def _unit_sessions(title, group_note=None):
    """Expand one unit title into its 2 weekly sessions."""
    explore_sub = f"Explore & learn: {title}"
    create_sub = f"Create & share: {title}" + (f" ({group_note})" if group_note else "")
    return [
        {"topic": title, "subtopic": explore_sub, "source": f"Oak National Academy: {title}"},
        {"topic": title, "subtopic": create_sub, "source": f"Oak National Academy: {title}"},
    ]


def _ks3_unit_sessions(title, group_note):
    return [
        {"topic": title, "subtopic": f"Explore & learn: {title} ({group_note})", "source": "Original KS3 unit"},
        {"topic": title, "subtopic": f"Build & present: {title} ({group_note})", "source": "Original KS3 unit"},
    ]


def build_class_weeks(class_id: str) -> list:
    """Returns exactly CONTENT_WEEKS_TARGET (24) week dicts:
    {topic, subtopic, source, equipmentMode}."""
    key_stage = CLASS_KEY_STAGE[class_id]

    weeks = []
    for i, (topic, subtopic) in enumerate(UNPLUGGED_WEEKS[key_stage]):
        mode = "shared-laptops" if i == len(UNPLUGGED_WEEKS[key_stage]) - 1 else "unplugged"
        weeks.append({"topic": topic, "subtopic": subtopic, "source": "Settling-in (low/no device)", "equipmentMode": mode})

    if class_id in OAK_UNITS:
        for title in OAK_UNITS[class_id]:
            for s in _unit_sessions(title):
                weeks.append({**s, "equipmentMode": "shared-laptops"})
    else:
        for title, group_note in KS3_UNITS[class_id]:
            for s in _ks3_unit_sessions(title, group_note):
                weeks.append({**s, "equipmentMode": "1-1-devices"})

    remaining = CONTENT_WEEKS_TARGET - len(weeks)
    pool = CUSTOM_POOL[key_stage]
    for i in range(remaining):
        topic, subtopic = pool[i % len(pool)]
        weeks.append({"topic": topic, "subtopic": subtopic, "source": "Custom (flexible slot)", "equipmentMode": "shared-laptops"})

    assert len(weeks) == CONTENT_WEEKS_TARGET, f"{class_id}: {len(weeks)} weeks, expected {CONTENT_WEEKS_TARGET}"
    return weeks
