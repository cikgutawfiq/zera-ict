"""ICT Y1-Y9 curriculum spine.

Every ICT class (Y1-Y9) follows the SAME set of 16 modules — the same
tools and topics all the way through the school — with the content,
vocabulary and the module's project scaled up by key stage (KS1/KS2/KS3)
rather than swapped out year to year. This keeps the whole school on one
consistent map of "what ICT covers" while still stretching older pupils.

Every class gets, in this order:
  1. 8 "settling in" weeks at the very start of Term 1 (equipmentMode
     unplugged/shared-laptops) -- for the first ~2 months, while laptop
     access may be limited (as few as 4 shared machines in rotating groups).
  2. All 16 modules below, one week each, tier-scaled to that class's key
     stage -- each with its own project (something to present or produce)
     and a direct link to the real tool/reference where one applies.

24 content weeks (8 unplugged + 16 modules) + the existing 17 consolidation/
revision/exam/project/showcase weeks = 41, split 8/8/8 across Term 1/2/3
(content) same as before -- modules 1-8 land in Term 2, 9-16 in Term 3.
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

OAK_SECONDARY_UNITS_URL = "https://www.thenational.academy/teachers/programmes/computing-secondary-core/units"
THREAD_SLUGS = {
    "Artificial intelligence": "artificial-intelligence",
    "Data and information": "data-and-information",
    "Safety and security": "safety-and-security",
    "Design and development": "design-and-development",
    "Creating media": "creating-media",
}


def _thread_url(thread: str) -> str:
    return f"{OAK_SECONDARY_UNITS_URL}?threads={THREAD_SLUGS[thread]}"


def _tier(ks1, ks2, ks3):
    return {"KS1": ks1, "KS2": ks2, "KS3": ks3}


# The 16 modules every class follows, in delivery order. Each module has:
#   name          -- shown as the lesson topic, identical at every key stage
#   resourceUrl   -- the real tool/reference link, shown in Resources
#   equipmentMode -- KS1/KS2 pair up on shared laptops; KS3 work individually
#   tiers         -- {KS1, KS2, KS3}: subtopic, objectives (3) and project
#                     (what pupils present or produce), scaled by key stage
MODULES = [
    {
        "name": "Google Interland",
        "resourceUrl": "https://beinternetawesome.withgoogle.com/en_us/interland",
        "equipmentMode": {"KS1": "shared-laptops", "KS2": "shared-laptops", "KS3": "1-1-devices"},
        "tiers": _tier(
            {
                "subtopic": "Playing Kind Kingdom and Mindful Mountain",
                "objectives": [
                    "Play through 2 Interland worlds with a partner.",
                    "Talk about one kind choice and one safe choice made in the game.",
                    "Say one rule for being safe online.",
                ],
                "project": "Draw a 'Being Safe and Kind Online' poster using one idea from Interland.",
            },
            {
                "subtopic": "Completing Reality River and Tower of Treasure",
                "objectives": [
                    "Complete 2 Interland worlds, explaining choices made along the way.",
                    "Identify a real vs fake example from Reality River.",
                    "Explain why strong passwords matter, using Tower of Treasure.",
                ],
                "project": "Write a one-page online-safety tips leaflet based on what Interland taught.",
            },
            {
                "subtopic": "Completing all 4 Interland worlds and discussing real scenarios",
                "objectives": [
                    "Complete all 4 Interland worlds independently.",
                    "Relate each world's lesson to a real online scenario they've encountered or heard of.",
                    "Evaluate which online-safety skill they personally need to work on most.",
                ],
                "project": "Produce a short online-safety awareness poster or 60-second video script for younger pupils.",
            },
        ),
    },
    {
        "name": "Typing Club",
        "resourceUrl": "https://www.typingclub.com/",
        "equipmentMode": {"KS1": "shared-laptops", "KS2": "shared-laptops", "KS3": "1-1-devices"},
        "tiers": _tier(
            {
                "subtopic": "Finding the home-row keys",
                "objectives": [
                    "Find the home-row keys without looking at the keyboard.",
                    "Type a few home-row letters correctly.",
                    "Sit with correct typing posture.",
                ],
                "project": "Reach a personal-best score on a home-row typing game.",
            },
            {
                "subtopic": "Building speed and accuracy across the keyboard",
                "objectives": [
                    "Type using the correct finger for each key, beyond the home row.",
                    "Track their words-per-minute (WPM) over several sessions.",
                    "Reduce typing errors through repeated practice.",
                ],
                "project": "Reach a target WPM with under 10% errors, recorded in a typing log.",
            },
            {
                "subtopic": "Professional speed and sustained accuracy",
                "objectives": [
                    "Type accurately for a sustained passage without looking at the keyboard.",
                    "Reach a target professional typing speed.",
                    "Reflect on their typing progress across the year.",
                ],
                "project": "Reach a professional target WPM and write a short typed reflection on their progress.",
            },
        ),
    },
    {
        "name": "Microsoft Word",
        "resourceUrl": "https://www.microsoft.com/en-us/microsoft-365/word",
        "equipmentMode": {"KS1": "shared-laptops", "KS2": "shared-laptops", "KS3": "1-1-devices"},
        "tiers": _tier(
            {
                "subtopic": "Typing and formatting a simple sentence",
                "objectives": [
                    "Open Word and type a short sentence.",
                    "Change the font size and colour of their text.",
                    "Save their document with a sensible name.",
                ],
                "project": "A simple 'All About Me' page with a title, one sentence and a picture.",
            },
            {
                "subtopic": "Formatting a multi-paragraph document",
                "objectives": [
                    "Use headings and paragraphs to organise a document.",
                    "Insert and resize an image.",
                    "Use a bullet or numbered list correctly.",
                ],
                "project": "A one-page formatted report with a heading, an image and a bullet list.",
            },
            {
                "subtopic": "Styles, headers/footers and a table of contents",
                "objectives": [
                    "Apply heading styles consistently across a multi-page document.",
                    "Add headers, footers and page numbers.",
                    "Generate and update a table of contents.",
                ],
                "project": "A multi-page formatted report using styles and an auto-generated table of contents.",
            },
        ),
    },
    {
        "name": "Google Docs",
        "resourceUrl": "https://docs.google.com/",
        "equipmentMode": {"KS1": "shared-laptops", "KS2": "shared-laptops", "KS3": "1-1-devices"},
        "tiers": _tier(
            {
                "subtopic": "Typing a shared class sentence together",
                "objectives": [
                    "Open a shared Google Doc.",
                    "Type one sentence into the shared document.",
                    "Watch a classmate's typing appear in real time.",
                ],
                "project": "A shared class page, each pupil contributing one sentence.",
            },
            {
                "subtopic": "Co-authoring a shared document with comments",
                "objectives": [
                    "Add and reply to a comment on a shared document.",
                    "Contribute a paragraph to a group piece of writing.",
                    "Use the shared document without overwriting a partner's work.",
                ],
                "project": "A group-written short story, each pupil contributing a section and commenting on others'.",
            },
            {
                "subtopic": "Co-authoring with suggestions and version history",
                "objectives": [
                    "Use Suggesting mode to propose an edit rather than overwrite text.",
                    "Accept or reject a suggestion from a teammate.",
                    "Use version history to see how a document changed over time.",
                ],
                "project": "A collaboratively edited report with tracked suggestions and resolved comments.",
            },
        ),
    },
    {
        "name": "Microsoft Excel",
        "resourceUrl": "https://www.microsoft.com/en-us/microsoft-365/excel",
        "equipmentMode": {"KS1": "shared-laptops", "KS2": "shared-laptops", "KS3": "1-1-devices"},
        "tiers": _tier(
            {
                "subtopic": "Entering numbers into a simple table",
                "objectives": [
                    "Type numbers into cells in a grid.",
                    "Add a simple title to a table.",
                    "Colour a cell to highlight the biggest number.",
                ],
                "project": "A simple table counting a class's favourite colours or fruits.",
            },
            {
                "subtopic": "Simple formulas and a chart",
                "objectives": [
                    "Use the SUM formula to total a column of numbers.",
                    "Use the AVERAGE formula on a set of numbers.",
                    "Create a simple bar or pie chart from data.",
                ],
                "project": "A survey-results spreadsheet with a total, an average, and a chart.",
            },
            {
                "subtopic": "Formulas, conditional formatting and charts",
                "objectives": [
                    "Use a formula that references other cells (e.g. a running total).",
                    "Apply conditional formatting to highlight values automatically.",
                    "Choose an appropriate chart type for a dataset and label it clearly.",
                ],
                "project": "A data-model or simple budget spreadsheet with formulas, conditional formatting and a chart.",
            },
        ),
    },
    {
        "name": "Google Sheets",
        "resourceUrl": "https://sheets.google.com/",
        "equipmentMode": {"KS1": "shared-laptops", "KS2": "shared-laptops", "KS3": "1-1-devices"},
        "tiers": _tier(
            {
                "subtopic": "Entering numbers into a shared sheet together",
                "objectives": [
                    "Type a number into a shared spreadsheet.",
                    "Find a cell using its row and column.",
                    "Watch a classmate's entry appear in real time.",
                ],
                "project": "A class shared counting sheet everyone contributes a row to.",
            },
            {
                "subtopic": "Building a shared spreadsheet with simple formulas",
                "objectives": [
                    "Enter data into a shared spreadsheet alongside a group.",
                    "Use a simple formula (SUM or AVERAGE) on shared data.",
                    "Create a chart from the group's data.",
                ],
                "project": "A group survey spreadsheet with a shared formula and chart.",
            },
            {
                "subtopic": "Building a shared data model with formulas and charts",
                "objectives": [
                    "Design a shared spreadsheet structure with a group before entering data.",
                    "Use formulas that reference data entered by teammates.",
                    "Present the group's chart and explain what it shows.",
                ],
                "project": "A group data-modelling spreadsheet with formulas, a chart and shared editing.",
            },
        ),
    },
    {
        "name": "Canva Design",
        "resourceUrl": "https://www.canva.com/",
        "equipmentMode": {"KS1": "shared-laptops", "KS2": "shared-laptops", "KS3": "1-1-devices"},
        "tiers": _tier(
            {
                "subtopic": "Making a simple picture from a template",
                "objectives": [
                    "Open a Canva template.",
                    "Change the text and colours on a template.",
                    "Save/download their design.",
                ],
                "project": "A simple poster made from a Canva template.",
            },
            {
                "subtopic": "Designing a poster with text and images",
                "objectives": [
                    "Combine text, images and shapes on a Canva design.",
                    "Choose colours and fonts that work well together.",
                    "Resize and position elements neatly.",
                ],
                "project": "An original poster promoting something, e.g. a class event.",
            },
            {
                "subtopic": "Designing with brand consistency for a real audience",
                "objectives": [
                    "Design a poster or social graphic using a consistent colour/font scheme.",
                    "Consider audience and purpose when choosing images and wording.",
                    "Export a design ready to share or print.",
                ],
                "project": "A branded poster or social-media graphic campaign for a chosen cause.",
            },
        ),
    },
    {
        "name": "Google Forms",
        "resourceUrl": "https://forms.google.com/",
        "equipmentMode": {"KS1": "shared-laptops", "KS2": "shared-laptops", "KS3": "1-1-devices"},
        "tiers": _tier(
            {
                "subtopic": "Answering a simple class survey",
                "objectives": [
                    "Open a link to a class survey.",
                    "Choose an answer to a simple question.",
                    "Submit the form.",
                ],
                "project": "Answer a class survey and look at the results together as a class.",
            },
            {
                "subtopic": "Building a simple survey and reading results",
                "objectives": [
                    "Add 2-3 questions to a Google Form.",
                    "Choose an appropriate question type (multiple choice, short answer).",
                    "Read the results summary after collecting responses.",
                ],
                "project": "A short class survey with results read and summarised.",
            },
            {
                "subtopic": "Designing, collecting and analysing survey responses",
                "objectives": [
                    "Design a survey with a clear purpose and varied question types.",
                    "Collect responses from a real audience (class or year group).",
                    "Analyse the response summary and draw a conclusion.",
                ],
                "project": "A designed survey with collected responses and a short written results analysis.",
            },
        ),
    },
    {
        "name": "Microsoft PowerPoint",
        "resourceUrl": "https://www.microsoft.com/en-us/microsoft-365/powerpoint",
        "equipmentMode": {"KS1": "shared-laptops", "KS2": "shared-laptops", "KS3": "1-1-devices"},
        "tiers": _tier(
            {
                "subtopic": "A 2-3 slide presentation about a favourite thing",
                "objectives": [
                    "Add a title and a picture to a slide.",
                    "Add a second slide.",
                    "Say one sentence about each slide.",
                ],
                "project": "A 2-3 slide 'my favourite...' presentation.",
            },
            {
                "subtopic": "A multi-slide presentation with images and transitions",
                "objectives": [
                    "Build a 4-5 slide presentation with a clear structure.",
                    "Add images that support the content on each slide.",
                    "Add a simple transition between slides.",
                ],
                "project": "A 5-slide presentation on a class topic, presented to the class.",
            },
            {
                "subtopic": "A polished presentation with strong visuals",
                "objectives": [
                    "Design slides with a consistent, uncluttered visual style.",
                    "Use notes to support (not read from) a delivered talk.",
                    "Deliver the presentation clearly to an audience.",
                ],
                "project": "A polished multi-slide presentation delivered to an audience.",
            },
        ),
    },
    {
        "name": "Google Slides",
        "resourceUrl": "https://slides.google.com/",
        "equipmentMode": {"KS1": "shared-laptops", "KS2": "shared-laptops", "KS3": "1-1-devices"},
        "tiers": _tier(
            {
                "subtopic": "Adding to a shared class slide",
                "objectives": [
                    "Open a shared Google Slides file.",
                    "Add a picture to their own slide.",
                    "Look at a classmate's slide.",
                ],
                "project": "One shared class slideshow, each pupil adding a picture to their own slide.",
            },
            {
                "subtopic": "Building a group presentation with shared slides",
                "objectives": [
                    "Contribute one slide to a shared group presentation.",
                    "Keep a consistent style with the rest of the group's slides.",
                    "Present their own slide to the group.",
                ],
                "project": "A group presentation, each pupil owning and presenting one slide.",
            },
            {
                "subtopic": "Co-building a team presentation with comments and history",
                "objectives": [
                    "Co-build a shared presentation with a team, dividing sections fairly.",
                    "Use comments to give and receive feedback on slides.",
                    "Use version history to track how the presentation developed.",
                ],
                "project": "A team presentation co-built and delivered together.",
            },
        ),
    },
    {
        "name": "Google Sites",
        "resourceUrl": "https://sites.google.com/",
        "equipmentMode": {"KS1": "shared-laptops", "KS2": "shared-laptops", "KS3": "1-1-devices"},
        "tiers": _tier(
            {
                "subtopic": "Looking at and adding to a simple class site",
                "objectives": [
                    "Look at a simple example website as a class.",
                    "Suggest what could go on a class page.",
                    "Add one piece of content to a class-built page, with support.",
                ],
                "project": "A simple one-page class site about a favourite topic, built together.",
            },
            {
                "subtopic": "Building a simple personal website",
                "objectives": [
                    "Create a page with a title, text and an image.",
                    "Add a second linked page to their site.",
                    "Publish their site so it can be viewed.",
                ],
                "project": "A 2-3 page personal website about a hobby or interest.",
            },
            {
                "subtopic": "Building a multi-page site with navigation and design choices",
                "objectives": [
                    "Plan a site's structure (pages and navigation) before building.",
                    "Apply a consistent design/theme across pages.",
                    "Publish and share the finished site.",
                ],
                "project": "A multi-page website for a chosen purpose — portfolio, campaign or club.",
            },
        ),
    },
    {
        "name": "Artificial Intelligence",
        "resourceUrl": _thread_url("Artificial intelligence"),
        "equipmentMode": {"KS1": "shared-laptops", "KS2": "shared-laptops", "KS3": "1-1-devices"},
        "tiers": _tier(
            {
                "subtopic": "What is AI? Spotting AI in everyday life",
                "objectives": [
                    "Give an example of something that uses AI (e.g. a voice assistant).",
                    "Understand that AI is a computer program that has learned from examples.",
                    "Talk about one thing AI is good at and one thing it isn't.",
                ],
                "project": "A simple poster: 'AI in My Life', with 3 examples.",
            },
            {
                "subtopic": "Trying safe AI tools and discussing how they work",
                "objectives": [
                    "Try an age-appropriate AI tool with teacher guidance.",
                    "Explain, simply, that AI learns patterns from lots of data.",
                    "Identify a mistake an AI tool made and discuss why.",
                ],
                "project": "A short write-up comparing 2 AI tools they tried, with one strength and one limitation each.",
            },
            {
                "subtopic": "Using AI tools critically: bias, ethics and limitations",
                "objectives": [
                    "Use an AI tool critically, checking its output rather than trusting it blindly.",
                    "Explain what bias in AI means, with an example.",
                    "Discuss an ethical question AI raises (e.g. jobs, privacy, fairness).",
                ],
                "project": "A short report or presentation on an AI ethics issue, with real examples.",
            },
        ),
    },
    {
        "name": "Data and Information",
        "resourceUrl": _thread_url("Data and information"),
        "equipmentMode": {"KS1": "shared-laptops", "KS2": "shared-laptops", "KS3": "1-1-devices"},
        "tiers": _tier(
            {
                "subtopic": "Sorting and counting simple data",
                "objectives": [
                    "Sort a set of objects into groups by one property.",
                    "Count how many are in each group.",
                    "Say which group has the most or fewest.",
                ],
                "project": "A simple pictogram of a class survey (e.g. favourite fruit).",
            },
            {
                "subtopic": "Collecting, organising and presenting data",
                "objectives": [
                    "Collect data from classmates using a tally chart.",
                    "Organise the data into a table.",
                    "Present the data as a bar chart or pictogram.",
                ],
                "project": "A data report with a chart and a one-paragraph written conclusion.",
            },
            {
                "subtopic": "Data representation, analysis and drawing conclusions",
                "objectives": [
                    "Choose an appropriate way to represent a real dataset.",
                    "Identify a pattern or trend in the data.",
                    "Draw and justify a conclusion from the data.",
                ],
                "project": "A data-investigation report analysing a real or class dataset, with a justified conclusion.",
            },
        ),
    },
    {
        "name": "Safety and Security",
        "resourceUrl": _thread_url("Safety and security"),
        "equipmentMode": {"KS1": "shared-laptops", "KS2": "shared-laptops", "KS3": "1-1-devices"},
        "tiers": _tier(
            {
                "subtopic": "Simple online safety rules",
                "objectives": [
                    "State one rule for staying safe online.",
                    "Say what to do if something online feels wrong.",
                    "Recognise a trusted adult they could tell.",
                ],
                "project": "A class online-safety rules poster.",
            },
            {
                "subtopic": "Passwords, privacy and spotting scams",
                "objectives": [
                    "Explain what makes a password strong.",
                    "Explain why personal information should stay private online.",
                    "Spot the warning signs of a simple online scam.",
                ],
                "project": "A cybersecurity tips leaflet or poster for younger pupils.",
            },
            {
                "subtopic": "Cybersecurity threats, case studies and protection",
                "objectives": [
                    "Describe a real cybersecurity threat (e.g. phishing, malware).",
                    "Analyse a real-world case study and identify what went wrong.",
                    "Recommend a protection measure that could have prevented it.",
                ],
                "project": "A cybersecurity awareness campaign (poster or video) based on a real case study.",
            },
        ),
    },
    {
        "name": "Design and Development",
        "resourceUrl": _thread_url("Design and development"),
        "equipmentMode": {"KS1": "shared-laptops", "KS2": "shared-laptops", "KS3": "1-1-devices"},
        "tiers": _tier(
            {
                "subtopic": "Simple sequencing with instructions",
                "objectives": [
                    "Put a simple set of instructions in the correct order.",
                    "Follow a partner's step-by-step instructions.",
                    "Spot when a step is missing or wrong.",
                ],
                "project": "A simple sequence of instructions (on paper or with a simple app) for a everyday task.",
            },
            {
                "subtopic": "Block-based programming with loops and selection",
                "objectives": [
                    "Use a repeat/loop block to make an action happen several times.",
                    "Use an if/selection block to make a decision in a program.",
                    "Test and debug a short block-based program.",
                ],
                "project": "A simple game or animation built with block-based coding.",
            },
            {
                "subtopic": "Text-based programming with functions and logic",
                "objectives": [
                    "Write a program using variables and simple logic (if/else).",
                    "Define and call a function to organise code.",
                    "Test a program and fix bugs found.",
                ],
                "project": "A working Python program — e.g. a simple game or useful tool — using at least one function.",
            },
        ),
    },
    {
        "name": "Creating Media",
        "resourceUrl": _thread_url("Creating media"),
        "equipmentMode": {"KS1": "shared-laptops", "KS2": "shared-laptops", "KS3": "1-1-devices"},
        "tiers": _tier(
            {
                "subtopic": "Simple digital painting/drawing",
                "objectives": [
                    "Use a digital painting tool to draw a picture.",
                    "Choose different brushes and colours.",
                    "Save their finished picture.",
                ],
                "project": "A digital picture or painting on a chosen theme.",
            },
            {
                "subtopic": "Combining images, audio or simple animation",
                "objectives": [
                    "Combine at least two media types (e.g. images and text, or images and audio).",
                    "Sequence frames or slides to tell a short story.",
                    "Share the finished piece with the class.",
                ],
                "project": "A short animation, or an audio/video piece, on a chosen topic.",
            },
            {
                "subtopic": "Producing and editing polished media",
                "objectives": [
                    "Plan a media piece (storyboard or script) before producing it.",
                    "Use editing tools to refine a video, audio or animation piece.",
                    "Present the finished, edited piece to an audience.",
                ],
                "project": "A polished media production — video, podcast or animation — with visible editing.",
            },
        ),
    },
]

# Each class's named End-of-Term project, one for Term 1 (built from the
# "settling-in" unplugged weeks — deliberately low-tech since T1 has limited
# device access) and one for Term 3 (a flagship build drawing on the year's
# modules). Shown directly in the Overview topic column as
# "End of Term Project - <name>".
PROJECTS = {
    "ict-y1": {1: "Being Safe & Kind Online Poster", 3: "My Favourite Animal Fact-File"},
    "ict-y2": {1: "Our ICT Room Rules & Safety Guide", 3: "My Hobby Data Survey"},
    "ict-y3": {1: "Internet Safety Campaign Poster", 3: "My Class Website"},
    "ict-y4": {1: "How the Internet Works Infographic", 3: "My Own Simple Game"},
    "ict-y5": {1: "Computer Systems Explainer", 3: "Class News Report (Media Production)"},
    "ict-y6": {1: "Staying Safe Online Campaign", 3: "Build My Own Webpage"},
    "ict-y7": {1: "School Network Investigation Report", 3: "Cybersecurity Awareness Campaign"},
    "ict-y8": {1: "Cybersecurity Case Study Report", 3: "School News Podcast/Video Series"},
    "ict-y9": {1: "Computer Systems Deep-Dive Report", 3: "Data Science Investigation — Analysing a Real Dataset"},
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
assert len(MODULES) == 16


def build_class_weeks(class_id: str) -> list:
    """Returns exactly CONTENT_WEEKS_TARGET (24) week dicts:
    {topic, subtopic, source, equipmentMode, objectives, project,
    resourceUrl?, resourceLabel?}."""
    key_stage = CLASS_KEY_STAGE[class_id]

    weeks = []
    for i, (topic, subtopic) in enumerate(UNPLUGGED_WEEKS[key_stage]):
        mode = "shared-laptops" if i == len(UNPLUGGED_WEEKS[key_stage]) - 1 else "unplugged"
        weeks.append({"topic": topic, "subtopic": subtopic, "source": "Settling-in (low/no device)", "equipmentMode": mode})

    for module in MODULES:
        tier = module["tiers"][key_stage]
        weeks.append(
            {
                "topic": module["name"],
                "subtopic": tier["subtopic"],
                "source": f"Module: {module['name']} ({key_stage})",
                "equipmentMode": module["equipmentMode"][key_stage],
                "objectives": tier["objectives"],
                "project": tier["project"],
                "resourceUrl": module.get("resourceUrl"),
                "resourceLabel": module["name"],
            }
        )

    assert len(weeks) == CONTENT_WEEKS_TARGET, f"{class_id}: {len(weeks)} weeks, expected {CONTENT_WEEKS_TARGET}"
    return weeks


def module_plan_table() -> list:
    """One row per module x key stage, for the Admin 'Module & project plan'
    view: which term/week it lands in (module N lands in content week N,
    i.e. Term 2 for modules 1-8, Term 3 for modules 9-16, matching
    build_class_weeks/build_ict.py's term split), what it covers, and its
    project at each key stage."""
    rows = []
    for i, module in enumerate(MODULES):
        term = 2 if i < 8 else 3
        week_in_term = (i % 8) + 1
        rows.append(
            {
                "order": i + 1,
                "term": term,
                "weekInTerm": week_in_term,
                "name": module["name"],
                "resourceUrl": module.get("resourceUrl"),
                "tiers": {
                    ks: {"subtopic": module["tiers"][ks]["subtopic"], "project": module["tiers"][ks]["project"]}
                    for ks in ("KS1", "KS2", "KS3")
                },
            }
        )
    return rows
