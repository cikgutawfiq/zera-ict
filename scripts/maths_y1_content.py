"""Suggested Year 1 Maths scope & sequence, aligned to Cambridge Primary
Mathematics Stage 1 strands (Number, Geometry, Measure, Statistics).

These are original topic titles, objectives and lesson plans written to match
the well-known structure and progression of that framework -- not verbatim
Cambridge text. Arranged across the school's 3-term calendar in the same
rhythm used for the ICT classes (consolidation / revision / examination week
/ end-of-term project / portfolio showcase in the closing weeks of each term).

Maths Y1 meets 3x/week (Tue, Thu, Fri). Each week below is ONE shared topic,
delivered as a 3-day arc:
  Tue  "explore"     -- introduce the idea hands-on
  Thu  "practice"    -- worked examples + guided/independent practice
  Fri  "consolidate" -- show-what-you-know + reflect

build_maths_y1.py turns each week into 3 separate Lesson dicts (one per
session day) via day_variant(), so each session is independently plannable
and markable Done -- they are not the same lesson repeated.
"""

# --- Term 1: Number foundations + Shape (15 weeks) ---
TERM1 = [
    {
        "topic": "Counting to 5",
        "subtopic": "Say Numbers and Match Them to Objects",
        "objectives": [
            "Count a small group of objects (up to 5), touching each one once.",
            "Say the number names in order from 1 to 5.",
            "Match a spoken number to the correct number of objects.",
        ],
        "resources": ["Counters or small toys", "Number cards 1-5", "A counting rhyme, e.g. '1, 2, Buckle My Shoe'"],
    },
    {
        "topic": "Counting to 10",
        "subtopic": "Say and Recognise Numbers 1-10",
        "objectives": [
            "Count objects up to 10, one at a time, touching each item.",
            "Recognise and read numerals 0-10.",
            "Match a group of objects to the correct numeral card.",
        ],
        "resources": ["Counting cubes or bears", "Number cards 0-10", "A number line 0-10, printed or on the board"],
    },
    {
        "topic": "Comparing Numbers to 10",
        "subtopic": "More, Fewer and the Same",
        "objectives": [
            "Compare two small groups of objects and say which has more or fewer.",
            "Use the words 'more than', 'fewer than' and 'the same as' correctly.",
            "Line objects up to compare two groups directly.",
        ],
        "resources": ["Two colours of counters", "Comparison mats (two hoops or drawn circles)", "Number cards 0-10"],
    },
    {
        "topic": "Ordering Numbers to 10",
        "subtopic": "Before, After and Between",
        "objectives": [
            "Put a jumbled set of numbers 1-10 back in order.",
            "Say the number that comes before or after a given number.",
            "Find a missing number on a number line 0-10.",
        ],
        "resources": ["Number cards 0-10 (for ordering)", "A large floor number line", "Washing-line and pegs (optional)"],
    },
    {
        "topic": "2D Shapes",
        "subtopic": "Naming and Sorting Circles, Squares, Triangles and Rectangles",
        "objectives": [
            "Name a circle, square, triangle and rectangle correctly.",
            "Sort a mixed set of shapes by name.",
            "Spot these 2D shapes in objects around the classroom.",
        ],
        "resources": ["Shape tiles/blocks", "A 'shape hunt' checklist", "Sorting hoops or trays"],
    },
    {
        "topic": "3D Shapes",
        "subtopic": "Naming Cubes, Spheres, Cones and Cylinders",
        "objectives": [
            "Name a cube, sphere, cone and cylinder correctly.",
            "Match a 3D shape name to an everyday object (e.g. a ball is a sphere).",
            "Describe a 3D shape using words like 'flat face', 'curved' and 'corner'.",
        ],
        "resources": ["3D shape set", "Everyday objects (ball, box, tin, party hat)", "Feely bag"],
    },
    {
        "topic": "Addition to 10",
        "subtopic": "Combining Two Groups and Counting All",
        "objectives": [
            "Combine two small groups of objects and count the total.",
            "Use the '+' and '=' symbols to record a simple addition.",
            "Solve a simple 'how many altogether?' story problem to 10.",
        ],
        "resources": ["Counters or cubes", "Mini-whiteboards", "Simple picture addition story cards"],
    },
    {
        "topic": "Subtraction to 10",
        "subtopic": "Taking Away and Counting What's Left",
        "objectives": [
            "Start with a group of objects, take some away, and count what's left.",
            "Use the '-' and '=' symbols to record a simple subtraction.",
            "Solve a simple 'how many are left?' story problem to 10.",
        ],
        "resources": ["Counters or cubes", "Mini-whiteboards", "Simple picture subtraction story cards"],
    },
    {
        "topic": "Consolidation",
        "subtopic": "Number and Shape Skills Rotation",
        "objectives": [
            "Revisit counting, comparing and ordering numbers to 10.",
            "Revisit naming and sorting 2D and 3D shapes.",
            "Revisit simple addition and subtraction to 10.",
        ],
        "resources": ["All Term 1 manipulatives", "Mixed-skills activity trays", "Mini-whiteboards"],
    },
    {
        "topic": "Revision",
        "subtopic": "Ready for the Practical Check",
        "objectives": [
            "Identify which Term 1 skills feel secure and which need more practice.",
            "Practise the type of task expected in the practical check.",
            "Ask for help on anything still unclear before the check.",
        ],
        "resources": ["Practice task cards", "Mini-whiteboards", "Term 1 skills checklist (self-tick)"],
    },
    {
        "topic": "Examination Week",
        "subtopic": "Term 1 Practical Assessment",
        "objectives": [
            "Show counting, comparing and ordering of numbers to 10.",
            "Show naming and sorting of 2D and 3D shapes.",
            "Show simple addition and subtraction to 10.",
        ],
        "resources": ["Assessment task cards", "Counters/cubes", "Shape set"],
    },
    {
        "topic": "End of Term Project",
        "subtopic": "'My Number Storybook' — Plan and Count",
        "objectives": [
            "Choose a favourite number 1-10 and count that many of a chosen object.",
            "Plan one page of a number storybook for that number.",
            "Say a simple sentence describing the page.",
        ],
        "resources": ["Blank storybook template", "Counters/small objects to count and draw", "Pencils and crayons"],
    },
    {
        "topic": "End of Term Project",
        "subtopic": "'My Number Storybook' — Draw and Write Numbers",
        "objectives": [
            "Draw the correct number of objects to match the numeral on each page.",
            "Write or trace the numeral neatly next to the picture.",
            "Check a partner's page for the right number of objects.",
        ],
        "resources": ["Storybook pages in progress", "Numeral tracing cards", "Pencils and crayons"],
    },
    {
        "topic": "End of Term Project",
        "subtopic": "'My Number Storybook' — Finish and Practise Reading It Aloud",
        "objectives": [
            "Complete and colour every page of the number storybook.",
            "Practise reading the storybook aloud in number order.",
            "Say one thing they are proud of in their storybook.",
        ],
        "resources": ["Completed storybook pages", "Stapler or binder", "A quiet reading corner"],
    },
    {
        "topic": "Portfolio Showcase",
        "subtopic": "Share My Number Storybook",
        "objectives": [
            "Read or present the number storybook to a partner or small group.",
            "Listen politely to a classmate's storybook and give one kind comment.",
            "Reflect on what they learned about numbers this term.",
        ],
        "resources": ["Finished storybooks", "Simple 'kind comment' sentence starters", "Certificates (optional)"],
    },
]

# --- Term 2: Number to 20, Measure, Position (11 weeks) ---
TERM2 = [
    {
        "topic": "Counting to 20",
        "subtopic": "Say and Recognise Numbers 11-20",
        "objectives": [
            "Count objects up to 20, one at a time.",
            "Recognise and read numerals 11-20.",
            "Continue a count from any number up to 20.",
        ],
        "resources": ["Counting cubes/bears", "Number cards 11-20", "A number line 0-20"],
    },
    {
        "topic": "Place Value to 20",
        "subtopic": "Tens and Ones with a Ten-Frame",
        "objectives": [
            "Show a number 11-20 as 'one ten and some ones' using a ten-frame.",
            "Explain that 14 means 1 ten and 4 ones.",
            "Build a given two-digit number using ten-frames and counters.",
        ],
        "resources": ["Ten-frame boards", "Counters", "Number cards 11-20"],
    },
    {
        "topic": "Addition to 20",
        "subtopic": "Adding with a Number Line and Ten-Frame",
        "objectives": [
            "Add two numbers with a total up to 20 using a number line.",
            "Add two numbers with a total up to 20 using a ten-frame.",
            "Solve a simple addition story problem to 20.",
        ],
        "resources": ["Number line 0-20", "Ten-frame boards", "Mini-whiteboards"],
    },
    {
        "topic": "Subtraction to 20",
        "subtopic": "Subtracting with a Number Line and Ten-Frame",
        "objectives": [
            "Subtract within 20 using a number line (counting back).",
            "Subtract within 20 using a ten-frame.",
            "Solve a simple subtraction story problem to 20.",
        ],
        "resources": ["Number line 0-20", "Ten-frame boards", "Mini-whiteboards"],
    },
    {
        "topic": "Doubling and Halving",
        "subtopic": "Double and Half of Small Numbers",
        "objectives": [
            "Find double a number up to 10 using objects.",
            "Find half of an even number up to 20 by sharing into two equal groups.",
            "Spot a doubles fact hidden in an addition (e.g. 6 + 6).",
        ],
        "resources": ["Counters", "Mirror or double-sided counters", "Mini-whiteboards"],
    },
    {
        "topic": "Length",
        "subtopic": "Comparing and Measuring Length with Non-Standard Units",
        "objectives": [
            "Compare two objects and say which is longer or shorter.",
            "Measure an object's length using non-standard units (e.g. cubes, hand spans).",
            "Order three or more objects by length.",
        ],
        "resources": ["Interlocking cubes", "A selection of classroom objects to measure", "Recording sheet"],
    },
    {
        "topic": "Mass and Capacity",
        "subtopic": "Comparing Heavier/Lighter and More/Less Full",
        "objectives": [
            "Compare two objects and say which is heavier or lighter, using a balance scale.",
            "Compare two containers and say which holds more or less.",
            "Order a small set of containers from emptiest to fullest.",
        ],
        "resources": ["Balance scale", "Water/sand and containers of different sizes", "Recording sheet"],
    },
    {
        "topic": "Position and Direction",
        "subtopic": "Above, Below, Left, Right and Simple Directions",
        "objectives": [
            "Use the words above, below, in front, behind, left and right correctly.",
            "Follow a simple set of directions to move an object or themselves.",
            "Give a partner a simple direction to follow.",
        ],
        "resources": ["Floor grid or playground chalk grid", "A toy or counter to move", "Direction cards"],
    },
    {
        "topic": "Consolidation",
        "subtopic": "Number, Measure and Position Skills Rotation",
        "objectives": [
            "Revisit counting, place value, addition and subtraction to 20.",
            "Revisit comparing length, mass and capacity.",
            "Revisit position and direction language.",
        ],
        "resources": ["All Term 2 manipulatives", "Mixed-skills activity trays", "Mini-whiteboards"],
    },
    {
        "topic": "Revision",
        "subtopic": "Ready for the Practical Check",
        "objectives": [
            "Identify which Term 2 skills feel secure and which need more practice.",
            "Practise the type of task expected in the practical check.",
            "Ask for help on anything still unclear before the check.",
        ],
        "resources": ["Practice task cards", "Mini-whiteboards", "Term 2 skills checklist (self-tick)"],
    },
    {
        "topic": "Examination Week",
        "subtopic": "Term 2 Practical Assessment",
        "objectives": [
            "Show counting, place value, addition and subtraction to 20.",
            "Show comparing of length, mass and capacity.",
            "Show understanding of position and direction language.",
        ],
        "resources": ["Assessment task cards", "Ten-frame boards", "Measuring resources"],
    },
]

# --- Term 3: Patterns, Money, Time, Data, Number to 50 (15 weeks) ---
TERM3 = [
    {
        "topic": "Patterns",
        "subtopic": "Spotting, Continuing and Creating Repeating Patterns",
        "objectives": [
            "Spot the repeating unit in a simple AB, AAB or ABC pattern.",
            "Continue a repeating pattern using objects, colours or shapes.",
            "Create their own repeating pattern and explain the rule.",
        ],
        "resources": ["Coloured counters/beads", "Pattern strips", "Everyday pattern examples (fabric, tiles)"],
    },
    {
        "topic": "Money",
        "subtopic": "Recognising Coins and Simple Counting of Coins",
        "objectives": [
            "Recognise and name common coins.",
            "Count a small group of same-value coins.",
            "Solve a simple 'how much altogether?' problem with coins.",
        ],
        "resources": ["Play coins", "Simple price-tag picture cards", "Mini-whiteboards"],
    },
    {
        "topic": "Telling Time",
        "subtopic": "O'clock and Half Past on an Analogue Clock",
        "objectives": [
            "Read o'clock times on an analogue clock.",
            "Read half past times on an analogue clock.",
            "Match a time to an everyday activity (e.g. 7 o'clock — wake up).",
        ],
        "resources": ["Teaching clock (geared, if available)", "Individual mini-clocks", "Daily-routine picture cards"],
    },
    {
        "topic": "Counting to 50",
        "subtopic": "Say and Recognise Numbers 21-50",
        "objectives": [
            "Count on from any number up to 50.",
            "Recognise and read numerals 21-50.",
            "Spot the pattern in the tens as numbers reach 30, 40 and 50.",
        ],
        "resources": ["A 1-50 number square", "Number cards 21-50", "Counting objects in groups of ten"],
    },
    {
        "topic": "Addition and Subtraction to 20",
        "subtopic": "Mixed Practice — Choosing the Right Operation",
        "objectives": [
            "Decide whether a story problem needs addition or subtraction.",
            "Solve mixed addition and subtraction problems within 20.",
            "Check an answer using a different method (e.g. number line vs ten-frame).",
        ],
        "resources": ["Mixed story-problem cards", "Number line 0-20", "Ten-frame boards"],
    },
    {
        "topic": "Grouping and Sharing",
        "subtopic": "Early Multiplication and Division Through Equal Groups",
        "objectives": [
            "Make equal groups of objects and count the total.",
            "Share a group of objects equally between people.",
            "Say whether a share came out equal or with some left over.",
        ],
        "resources": ["Counters/small objects", "Sharing plates or hoops", "Mini-whiteboards"],
    },
    {
        "topic": "Data Handling",
        "subtopic": "Collecting Data and Making a Pictogram",
        "objectives": [
            "Ask a simple yes/no or choice question to classmates.",
            "Record results with tally marks or pictures.",
            "Turn the results into a simple pictogram.",
        ],
        "resources": ["Tally chart template", "Pictogram grid", "Sticky notes or picture stickers"],
    },
    {
        "topic": "Interpreting Data",
        "subtopic": "Reading and Answering Questions About a Pictogram",
        "objectives": [
            "Read how many of each category a pictogram shows.",
            "Say which category has the most or fewest.",
            "Answer a simple comparison question using the pictogram.",
        ],
        "resources": ["Last session's pictograms", "Question cards", "Mini-whiteboards"],
    },
    {
        "topic": "Consolidation",
        "subtopic": "Whole-Year Skills Rotation",
        "objectives": [
            "Revisit number, shape, measure and data skills from across the year.",
            "Choose an area they want more practice in and work on it.",
            "Help a partner with a skill they find secure.",
        ],
        "resources": ["A full year's manipulatives", "Mixed-skills activity trays", "Mini-whiteboards"],
    },
    {
        "topic": "Revision",
        "subtopic": "Ready for the Practical Check",
        "objectives": [
            "Identify which whole-year skills feel secure and which need more practice.",
            "Practise the type of task expected in the practical check.",
            "Ask for help on anything still unclear before the check.",
        ],
        "resources": ["Practice task cards", "Mini-whiteboards", "Whole-year skills checklist (self-tick)"],
    },
    {
        "topic": "Examination Week",
        "subtopic": "Term 3 Practical Assessment",
        "objectives": [
            "Show counting and number skills up to 50.",
            "Show addition, subtraction, grouping and sharing skills.",
            "Show measure, position and simple data-handling skills.",
        ],
        "resources": ["Assessment task cards", "Counters/cubes", "A 1-50 number square"],
    },
    {
        "topic": "End of Term Project",
        "subtopic": "Maths Fair Stall — Plan and Practise",
        "objectives": [
            "Choose one maths skill from this year to turn into a stall game.",
            "Plan what visitors to the stall will need to do.",
            "Practise explaining the game's rules in a full sentence.",
        ],
        "resources": ["Planning sheet", "Chosen skill's manipulatives", "Example stall-game ideas"],
    },
    {
        "topic": "End of Term Project",
        "subtopic": "Maths Fair Stall — Build the Activity",
        "objectives": [
            "Make the materials needed for the stall game.",
            "Decorate a simple sign explaining the game.",
            "Test the game with a partner and fix any problems.",
        ],
        "resources": ["Card, scissors, glue, crayons", "Chosen skill's manipulatives", "Sign template"],
    },
    {
        "topic": "End of Term Project",
        "subtopic": "Maths Fair Stall — Rehearse Explaining It",
        "objectives": [
            "Rehearse welcoming a visitor and explaining the game clearly.",
            "Practise being a patient, encouraging 'stallholder'.",
            "Give a partner one tip to make their explanation clearer.",
        ],
        "resources": ["Finished stall materials", "Rehearsal partner", "Feedback sentence starters"],
    },
    {
        "topic": "Portfolio Showcase",
        "subtopic": "Maths Fair Day",
        "objectives": [
            "Run their maths stall for visiting classmates or family.",
            "Play a classmate's stall game and give one kind comment.",
            "Reflect on their favourite maths topic from the whole year.",
        ],
        "resources": ["All finished stalls", "Simple 'kind comment' sentence starters", "Certificates (optional)"],
    },
]

TERMS = {"term-1": TERM1, "term-2": TERM2, "term-3": TERM3}
