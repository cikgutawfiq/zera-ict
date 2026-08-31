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

# Real unit titles from Oak National Academy's Computing (Secondary Core)
# programme (https://www.thenational.academy/teachers/programmes/computing-
# secondary-core/units) -- original session content written to fit these
# unit names, not verbatim Oak lesson content. Each (title, thread, group
# note) becomes 2 of our weekly sessions.
KS3_UNITS = {
    "ict-y7": [
        ("Clear Messaging in Digital Media", "Creating media", "groups design and critique a digital media message"),
        ("Computer Networks and Data Transmission", "Networks", "groups build and present a network diagram of the school"),
        ("Using Media to Gain Support for a Cause", "Creating media", "groups produce a persuasive media campaign"),
        ("Fundamental Programming Constructs (Block-Based)", "Programming", "pair programming throughout"),
        ("Physical Computing with the micro:bit", "Design and development", "small groups share kits, rotating roles"),
        ("Data Modelling", "Data and information", "groups build and present a data model"),
    ],
    "ict-y8": [
        ("Developing Vector Graphics", "Creating media", "peer critique in pairs"),
        ("Computer Systems and Data Science", "Computing systems", "groups investigate and present a systems topic"),
        ("Developing for the Web", "Design and development", "teams of 3-4 build a multi-page site"),
        ("Data Representation: Text and Numbers", "Data and information", "pair investigation stations"),
        ("Mobile App Development", "Design and development", "teams of 3-4 design and prototype an app"),
        ("Introduction to Python Programming", "Programming", "pair programming with a code-review swap"),
    ],
    "ict-y9": [
        ("Python Programming with Sequences of Data", "Programming", "pair programming, algorithm relay challenges"),
        ("3D Animation", "Creating media", "production teams of 3-4, roles rotate"),
        ("Using Data Science", "Data and information", "groups investigate a real dataset and present findings"),
        ("Data Representation: Images and Sound", "Data and information", "pair investigation stations"),
        ("Introduction to Cybersecurity", "Safety and security", "groups investigate a case study and present findings"),
        ("Machine Learning Using the micro:bit", "Artificial intelligence", "small groups share kits, rotating roles"),
    ],
}

OAK_SECONDARY_UNITS_URL = "https://www.thenational.academy/teachers/programmes/computing-secondary-core/units"

# Oak "thread" filter slugs, matching the pattern of the ?threads=... URL
# param (e.g. ?threads=artificial-intelligence).
THREAD_SLUGS = {
    "Creating media": "creating-media",
    "Networks": "networks",
    "Programming": "programming",
    "Design and development": "design-and-development",
    "Data and information": "data-and-information",
    "Computing systems": "computing-systems",
    "Safety and security": "safety-and-security",
    "Artificial intelligence": "artificial-intelligence",
}


def thread_url(thread: str) -> str:
    slug = THREAD_SLUGS.get(thread)
    return f"{OAK_SECONDARY_UNITS_URL}?threads={slug}" if slug else OAK_SECONDARY_UNITS_URL


CUSTOM_POOL = {
    "KS1": [
        ("Typing Club — Home Row Warm-Up", "Find and practise the home-row keys, a few minutes at a time", "https://www.typingclub.com/"),
        ("Typing Club — Building Speed", "Short, timed typing games to build confidence and speed", "https://www.typingclub.com/"),
        ("Google Workspace — My Drive and Docs", "Create, name and save a simple document in Google Docs", "https://docs.google.com/"),
        ("Microsoft Office — Word Basics", "Create, name and save a simple document in Word", "https://www.microsoft.com/en-us/microsoft-365/word"),
        ("Digital Portfolio — Choosing My Best Work", "Pick a favourite piece of work and say why it's good", None),
        ("Typing Club — Whole Keyboard Challenge", "Practise reaching beyond the home row, letter by letter", "https://www.typingclub.com/"),
        ("Google Workspace — Slides: My First Presentation", "Make a 2-3 slide presentation about a favourite thing", "https://slides.google.com/"),
        ("Microsoft Office — PowerPoint Basics", "Make a 2-3 slide presentation about a favourite thing", "https://www.microsoft.com/en-us/microsoft-365/powerpoint"),
        ("Coding Playground — Free Choice", "A free-choice session with a simple block-coding tool", None),
        ("Digital Portfolio — Show and Tell Prep", "Choose and rehearse sharing one piece of work with the class", None),
    ],
    "KS2": [
        ("Typing Club — Speed and Accuracy Challenge", "A timed typing challenge, tracking personal-best progress", "https://www.typingclub.com/"),
        ("Google Workspace — Docs, Sheets and Slides Refresher", "A mixed refresher task across the three tools", "https://workspace.google.com/"),
        ("Microsoft Office — Word, Excel and PowerPoint Refresher", "A mixed refresher task across the three tools", "https://www.microsoft.com/en-us/microsoft-365"),
        ("Independent Project — Choose Your Own Mini-Challenge", "Pick a mini-challenge from a menu and complete it", None),
    ],
}

# Y7-9 custom slots: the specific tools requested, spread across the 3 years
# (4 slots/year) so every tool gets covered exactly once across KS3, each
# linked straight to the real tool so it's one click away from the lesson.
CUSTOM_KS3_BY_CLASS = {
    "ict-y7": [
        ("Google Interland", "Play through Interland's challenges to practise online safety skills", "https://beinternetawesome.withgoogle.com/en_us/interland"),
        ("Typing Club — Speed and Accuracy", "Timed typing practice, tracking personal-best progress", "https://www.typingclub.com/"),
        ("Microsoft Word — Document Skills", "Format a multi-page document using styles, headers and a table of contents", "https://www.microsoft.com/en-us/microsoft-365/word"),
        ("Google Docs — Collaborative Writing", "Co-author a shared document with comments and suggestions", "https://docs.google.com/"),
    ],
    "ict-y8": [
        ("Microsoft Excel — Data Skills", "Build a spreadsheet with formulas, charts and conditional formatting", "https://www.microsoft.com/en-us/microsoft-365/excel"),
        ("Google Sheets — Shared Data Projects", "Build a shared spreadsheet model with a group, using formulas and charts", "https://sheets.google.com/"),
        ("Canva Design — Poster and Social Graphic", "Design a poster or social graphic using Canva's templates and tools", "https://www.canva.com/"),
        ("Google Forms — Build a Survey", "Design a survey, collect responses, and read the results", "https://forms.google.com/"),
    ],
    "ict-y9": [
        ("Microsoft PowerPoint — Presentation Skills", "Design and deliver a polished presentation with strong visuals", "https://www.microsoft.com/en-us/microsoft-365/powerpoint"),
        ("Google Slides — Team Presentation", "Co-build a shared team presentation with comments and version history", "https://slides.google.com/"),
        ("Google Sites — Build a Simple Website", "Design and publish a simple multi-page website with Google Sites", "https://sites.google.com/"),
        ("Independent/Group Choice Project", "Pick a challenge from a menu, solo or in a self-formed group", None),
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


def _ks3_unit_sessions(title, thread, group_note):
    url = thread_url(thread)
    label = f"Oak National Academy — {thread} units"
    return [
        {
            "topic": title,
            "subtopic": f"Explore & learn: {title} ({group_note})",
            "source": f"Oak National Academy: {title} ({thread})",
            "resourceUrl": url,
            "resourceLabel": label,
        },
        {
            "topic": title,
            "subtopic": f"Build & present: {title} ({group_note})",
            "source": f"Oak National Academy: {title} ({thread})",
            "resourceUrl": url,
            "resourceLabel": label,
        },
    ]


def build_class_weeks(class_id: str) -> list:
    """Returns exactly CONTENT_WEEKS_TARGET (24) week dicts:
    {topic, subtopic, source, equipmentMode, resourceUrl?, resourceLabel?}."""
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
        for title, thread, group_note in KS3_UNITS[class_id]:
            for s in _ks3_unit_sessions(title, thread, group_note):
                weeks.append({**s, "equipmentMode": "1-1-devices"})

    remaining = CONTENT_WEEKS_TARGET - len(weeks)
    pool = CUSTOM_KS3_BY_CLASS.get(class_id) or CUSTOM_POOL[key_stage]
    for i in range(remaining):
        topic, subtopic, url = pool[i % len(pool)]
        weeks.append(
            {
                "topic": topic,
                "subtopic": subtopic,
                "source": "Custom (flexible slot)",
                "equipmentMode": "shared-laptops",
                "resourceUrl": url,
                "resourceLabel": topic,
            }
        )

    assert len(weeks) == CONTENT_WEEKS_TARGET, f"{class_id}: {len(weeks)} weeks, expected {CONTENT_WEEKS_TARGET}"
    return weeks
