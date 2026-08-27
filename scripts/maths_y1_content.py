"""Year 1 Maths scope & sequence, mapped to the official Cambridge Primary
Mathematics Curriculum Framework (0096) Stage 1 learning objectives.

Every one of Stage 1's 55 objectives (Number: Nn1-12, Nc1-22; Geometry:
Gs1-3, Gp1; Measure: Mm1, Ml1-3, Mt1-3; Handling data: Dh1; Problem solving:
Pt1-9) is covered exactly once across the 3 terms below -- each week's
`codes` list names which ones. Topic titles and objective wording here are
original paraphrases written to match the sense of the official objective,
not verbatim Cambridge text; the `codes` are the traceable link back to the
framework (source: Cambridge Primary Mathematics Curriculum Framework with
codes, Cambridge International Examinations).

Termly shape, matching Cambridge's own suggested progression (number and
shape first, calculation and measure once counting is secure, multiplication/
division and data handling last):
  Term 1 -- Number: counting, place value, comparing/ordering; Geometry
  Term 2 -- Calculation: addition & subtraction, doubles/halves; Measure
  Term 3 -- Calculation: early multiplication/division; Money, Time, Data;
            a dedicated Problem solving week (Pt1-9 are embedded throughout
            the framework, not their own strand -- one capstone week plus
            the day-variant "explain your thinking" framing in every session
            keeps them genuinely present all year, not just in that week)

Arranged in the same consolidation / revision / examination week / end-of-
term project / portfolio showcase rhythm used for the ICT classes.
"""

# --- Term 1: Number foundations + Shape (15 weeks) ---
TERM1 = [
    {
        "topic": "Counting and Number Recognition to 20",
        "subtopic": "Say, Read and Write Numbers 0-20",
        "codes": ["1Nn1", "1Nn2", "1Nn3"],
        "objectives": [
            "Recite numbers in order forwards to 20 and beyond, and count back from 20 to 0.",
            "Read and write numerals from 0 to 20.",
            "Count a group of up to 20 objects, touching each one once and keeping track of the total.",
        ],
        "resources": ["Counting cubes or bears", "Number cards 0-20", "A number line 0-20"],
    },
    {
        "topic": "Comparing and Ordering Numbers",
        "subtopic": "More, Fewer, Between and Ordinal Numbers",
        "codes": ["1Nn7", "1Nn8", "1Nn9"],
        "objectives": [
            "Say the number that is 1 or 10 more or less than a given number up to 30.",
            "Compare two numbers using more or fewer, and give a number that lies between them.",
            "Order numbers to at least 20 on a number track, and use ordinal numbers (1st, 2nd, 3rd...).",
        ],
        "resources": ["Number cards 0-20", "A large floor number track", "Washing-line and pegs (optional)"],
    },
    {
        "topic": "Place Value Basics",
        "subtopic": "Tens and Ones, and the = Sign",
        "codes": ["1Nn6", "1Nn10", "1Nn4"],
        "objectives": [
            "Begin to split a two-digit number into a ten and some ones, and put it back together.",
            "Understand and use the = sign to show that two amounts are equal.",
            "Count on in tens from 0 or a single-digit number, up to 100 or just over.",
        ],
        "resources": ["Ten-frame boards", "Counters", "Mini-whiteboards"],
    },
    {
        "topic": "Counting in Twos and Estimating",
        "subtopic": "Odd/Even Patterns and Sensible Guesses",
        "codes": ["1Nn5", "1Nn11"],
        "objectives": [
            "Count on in twos, starting to notice odd and even numbers to 20 as 'every other number'.",
            "Make a sensible estimate of a group of objects (up to about 30), then check by counting.",
        ],
        "resources": ["Counters in pairs", "Jars or trays of objects to estimate", "Mini-whiteboards"],
    },
    {
        "topic": "2D Shapes",
        "subtopic": "Naming and Sorting Circles, Squares, Triangles and Rectangles",
        "codes": ["1Gs1"],
        "objectives": [
            "Name a circle, square, triangle and rectangle correctly.",
            "Sort a mixed set of 2D shapes by name and by features such as number of sides.",
            "Use 2D shapes to make a pattern or a simple picture.",
        ],
        "resources": ["Shape tiles/blocks", "A 'shape hunt' checklist", "Sorting hoops or trays"],
    },
    {
        "topic": "3D Shapes and Symmetry",
        "subtopic": "Naming Solid Shapes and Spotting a Line of Symmetry",
        "codes": ["1Gs2", "1Gs3"],
        "objectives": [
            "Name a cube, cylinder, cone and sphere correctly, using flat/curved faces to describe them.",
            "Match a 3D shape name to an everyday object.",
            "Recognise when a simple shape or pattern has a line of symmetry, using a mirror or by folding.",
        ],
        "resources": ["3D shape set", "Everyday objects (ball, tin, party hat, box)", "Small mirrors"],
    },
    {
        "topic": "Position and Direction",
        "subtopic": "Above, Below, Left, Right and Simple Movement",
        "codes": ["1Gp1"],
        "objectives": [
            "Use everyday words for direction and distance (above, below, near, far, forwards, backwards).",
            "Describe the movement of an object or a person using this language.",
            "Follow a simple spoken direction to move an object or themselves.",
        ],
        "resources": ["Floor grid or playground chalk grid", "A toy or counter to move", "Direction word cards"],
    },
    {
        "topic": "Number Pairs to 10",
        "subtopic": "Know Pairs That Make 10, and Begin 6-9",
        "codes": ["1Nc1", "1Nc2"],
        "objectives": [
            "Know, by heart, all the pairs of numbers that add to 10 (e.g. 6 and 4).",
            "Record the related addition and subtraction facts for pairs to 10.",
            "Begin to know pairs of numbers that add to 6, 7, 8 and 9.",
        ],
        "resources": ["Ten-frame boards", "Number-pair domino cards", "Mini-whiteboards"],
    },
    {
        "topic": "Consolidation",
        "subtopic": "Number, Shape and Position Skills Rotation",
        "codes": [],
        "objectives": [
            "Revisit counting, comparing, ordering and place-value basics from this term.",
            "Revisit naming and sorting 2D and 3D shapes, and using direction language.",
            "Revisit number pairs to 10.",
        ],
        "resources": ["All Term 1 manipulatives", "Mixed-skills activity trays", "Mini-whiteboards"],
    },
    {
        "topic": "Revision",
        "subtopic": "Ready for the Practical Check",
        "codes": [],
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
        "codes": [],
        "objectives": [
            "Show counting, comparing and ordering of numbers to 20.",
            "Show naming and sorting of 2D and 3D shapes, and use of direction language.",
            "Show number pairs to 10.",
        ],
        "resources": ["Assessment task cards", "Counters/cubes", "Shape set"],
    },
    {
        "topic": "End of Term Project",
        "subtopic": "'My Number Storybook' — Plan and Count",
        "codes": [],
        "objectives": [
            "Choose a favourite number 1-20 and count that many of a chosen object.",
            "Plan one page of a number storybook for that number.",
            "Say a simple sentence describing the page.",
        ],
        "resources": ["Blank storybook template", "Counters/small objects to count and draw", "Pencils and crayons"],
    },
    {
        "topic": "End of Term Project",
        "subtopic": "'My Number Storybook' — Draw and Write Numbers",
        "codes": [],
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
        "codes": [],
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
        "codes": [],
        "objectives": [
            "Read or present the number storybook to a partner or small group.",
            "Listen politely to a classmate's storybook and give one kind comment.",
            "Reflect on what they learned about numbers this term.",
        ],
        "resources": ["Finished storybooks", "Simple 'kind comment' sentence starters", "Certificates (optional)"],
    },
]

# --- Term 2: Calculation (addition, subtraction, doubles) + Measure (11 weeks) ---
TERM2 = [
    {
        "topic": "Addition as Combining",
        "subtopic": "Counting On and Recording Addition Sentences",
        "codes": ["1Nc8", "1Nc14", "1Nc17"],
        "objectives": [
            "Understand addition as combining two groups and counting on; record it as a number sentence.",
            "Begin to use the +, - and = signs to record a calculation.",
            "Recognise a missing-number symbol, e.g. 6 + [ ] = 10, and find the missing number.",
        ],
        "resources": ["Counters or cubes", "Mini-whiteboards", "Simple picture addition story cards"],
    },
    {
        "topic": "Subtraction as Taking Away",
        "subtopic": "Counting Back and 'How Many More to Make?'",
        "codes": ["1Nc9", "1Nc10"],
        "objectives": [
            "Understand subtraction as counting back and 'take away'; record it as a number sentence.",
            "Understand difference as 'how many more to make?' and solve a simple example.",
        ],
        "resources": ["Counters or cubes", "Mini-whiteboards", "Simple picture subtraction story cards"],
    },
    {
        "topic": "Counting On and Back to Calculate",
        "subtopic": "Number-Line Jumps and Adding the Larger Number First",
        "codes": ["1Nc11", "1Nc12", "1Nc15", "1Nc16"],
        "objectives": [
            "Add or subtract a single-digit number by counting on or back.",
            "Find two more or two less than a number to 20, recording the jumps on a number line.",
            "Know that changing the order of two numbers being added does not change the total.",
            "Add a pair of numbers by putting the larger number first and counting on.",
        ],
        "resources": ["Number line 0-20", "Mini-whiteboards", "Two dice or spinners"],
    },
    {
        "topic": "Doubles and Near Doubles",
        "subtopic": "Doubling, Near Doubles, and Folding for Halves",
        "codes": ["1Nc5", "1Nc6", "1Nn12"],
        "objectives": [
            "Know doubles of numbers up to at least double 5.",
            "Work out a 'near double' (e.g. 5 + 6) using a doubles fact already known.",
            "Find half of a small number or shape by sharing or folding, and recognise a correctly halved shape.",
        ],
        "resources": ["Counters", "Paper shapes for folding", "Mini-whiteboards"],
    },
    {
        "topic": "Bridging Ten and Adding Three Numbers",
        "subtopic": "Using Pairs to 10 to Add Past It",
        "codes": ["1Nc3", "1Nc4", "1Nc13", "1Nc18"],
        "objectives": [
            "Add more than two small numbers, spotting pairs that make 10 to help.",
            "Begin to use pairs to 10 to bridge 10 when adding or subtracting (e.g. 8 + 3: add 2, then 1).",
            "Relate counting on/back in tens to finding 10 more or less than a number under 100.",
            "Begin to add a single-digit number to a two-digit number.",
        ],
        "resources": ["Ten-frame boards", "Number line 0-100", "Mini-whiteboards"],
    },
    {
        "topic": "Length",
        "subtopic": "Comparing and Measuring with Non-Standard Units",
        "codes": ["1Ml1", "1Ml3"],
        "objectives": [
            "Compare the length of two objects by placing them side by side.",
            "Measure an object's length using non-standard units (e.g. cubes, hand spans).",
            "Use comparative language correctly: longer, shorter, heavier, lighter.",
        ],
        "resources": ["Interlocking cubes", "A selection of classroom objects to measure", "Recording sheet"],
    },
    {
        "topic": "Mass and Capacity",
        "subtopic": "Comparing Weight and How Full a Container Is",
        "codes": ["1Ml1", "1Ml2"],
        "objectives": [
            "Compare two objects by direct comparison and say which is heavier or lighter.",
            "Estimate and compare the capacity of two containers, then check with non-standard units.",
            "Order a small set of containers from emptiest to fullest.",
        ],
        "resources": ["Balance scale", "Water/sand and containers of different sizes", "Recording sheet"],
    },
    {
        "topic": "Position and Direction, Revisited",
        "subtopic": "Giving and Following Directions",
        "codes": ["1Gp1"],
        "objectives": [
            "Use direction and distance language confidently to describe a route.",
            "Give a partner a simple direction to follow, and follow one given to them.",
            "Describe the position of an object using this term's measure and position vocabulary together.",
        ],
        "resources": ["Floor grid or playground chalk grid", "A toy or counter to move", "Direction cards"],
    },
    {
        "topic": "Consolidation",
        "subtopic": "Calculation and Measure Skills Rotation",
        "codes": [],
        "objectives": [
            "Revisit addition and subtraction strategies from this term.",
            "Revisit doubles, near doubles and bridging ten.",
            "Revisit comparing length, mass and capacity.",
        ],
        "resources": ["All Term 2 manipulatives", "Mixed-skills activity trays", "Mini-whiteboards"],
    },
    {
        "topic": "Revision",
        "subtopic": "Ready for the Practical Check",
        "codes": [],
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
        "codes": [],
        "objectives": [
            "Show addition and subtraction strategies, including doubles and bridging ten.",
            "Show comparing of length, mass and capacity.",
            "Show direction and position language.",
        ],
        "resources": ["Assessment task cards", "Ten-frame boards", "Measuring resources"],
    },
]

# --- Term 3: Early multiplication/division + Money, Time, Data + Problem solving (15 weeks) ---
TERM3 = [
    {
        "topic": "Doubling, Halving and Sharing",
        "subtopic": "Double Any Single Digit, Halve Evens to 10",
        "codes": ["1Nc19", "1Nc20", "1Nc22"],
        "objectives": [
            "Double any single-digit number.",
            "Find half of an even number of objects up to 10 by sharing into two equal groups.",
            "Share a group of objects into two equal groups in a real context (e.g. sharing sweets fairly).",
        ],
        "resources": ["Counters/small objects", "Sharing plates or hoops", "Mini-whiteboards"],
    },
    {
        "topic": "Odd and Even Through Sharing",
        "subtopic": "Which Numbers Share Exactly, and Multiples of 2 and 10",
        "codes": ["1Nc21", "1Nc7"],
        "objectives": [
            "Try to share numbers up to 10 into two equal groups, and notice which ones have one left over.",
            "Use this to say whether a number to 10 is odd or even.",
            "Begin to recognise multiples of 2 and of 10.",
        ],
        "resources": ["Counters/small objects", "Sharing plates or hoops", "1-20 number square"],
    },
    {
        "topic": "Money",
        "subtopic": "Recognising Coins and Paying an Exact Amount",
        "codes": ["1Mm1"],
        "objectives": [
            "Recognise and name common coins.",
            "Work out how to pay an exact amount using smaller coins.",
            "Solve a simple 'how much altogether?' problem with coins.",
        ],
        "resources": ["Play coins", "Simple price-tag picture cards", "Mini-whiteboards"],
    },
    {
        "topic": "Telling Time",
        "subtopic": "O'Clock and Key Times of the Day",
        "codes": ["1Mt1", "1Mt2"],
        "objectives": [
            "Begin to understand and use units of time: minutes, hours, days, weeks, months and years.",
            "Read o'clock times on an analogue clock.",
            "Know key times of the day to the nearest hour (e.g. wake-up time, lunchtime, bedtime).",
        ],
        "resources": ["Teaching clock (geared, if available)", "Individual mini-clocks", "Daily-routine picture cards"],
    },
    {
        "topic": "Days and Familiar Events",
        "subtopic": "Ordering the Days of the Week",
        "codes": ["1Mt3"],
        "objectives": [
            "Order the days of the week correctly.",
            "Order a small set of familiar events (e.g. steps in the school day) by when they happen.",
            "Use words like 'before', 'after' and 'next' to talk about the order of events.",
        ],
        "resources": ["Days-of-the-week cards", "Daily-routine picture cards", "A classroom calendar"],
    },
    {
        "topic": "Counting to 50 and Beyond",
        "subtopic": "Extending the Number Sequence",
        "codes": ["1Nn1", "1Nn4"],
        "objectives": [
            "Recite numbers forwards well beyond 20, applying the counting patterns learned this year.",
            "Count on in tens from any number, continuing past 30 towards 100.",
            "Recognise the pattern in the tens as numbers reach 30, 40 and 50.",
        ],
        "resources": ["A 1-50 number square", "Number cards 21-50", "Counting objects in groups of ten"],
    },
    {
        "topic": "Data Handling",
        "subtopic": "Sorting and Showing Answers to a Question",
        "codes": ["1Dh1"],
        "objectives": [
            "Answer a simple question by sorting and organising objects or data.",
            "Show the results using a block graph or pictogram, and discuss what it shows.",
            "Sort the same objects a different way using a Venn or Carroll diagram.",
        ],
        "resources": ["Tally chart template", "Pictogram grid", "Sorting hoops for Venn/Carroll diagrams"],
    },
    {
        "topic": "Problem Solving Detectives",
        "subtopic": "Choosing Strategies, Checking Answers and Spotting Patterns",
        "codes": ["1Pt1", "1Pt2", "1Pt3", "1Pt4", "1Pt5", "1Pt6", "1Pt7", "1Pt8", "1Pt9"],
        "objectives": [
            "Choose an appropriate strategy for a calculation and explain the working out.",
            "Decide whether to add or subtract to solve a simple oral word problem, and represent it with objects.",
            "Check an addition by adding the numbers in a different order.",
            "Describe and continue a simple pattern, such as counting on or back in tens.",
        ],
        "resources": ["Mixed problem cards", "Counters/small objects", "Mini-whiteboards"],
    },
    {
        "topic": "Consolidation",
        "subtopic": "Whole-Year Skills Rotation",
        "codes": [],
        "objectives": [
            "Revisit number, shape, calculation, measure and data skills from across the year.",
            "Choose an area they want more practice in and work on it.",
            "Help a partner with a skill they find secure.",
        ],
        "resources": ["A full year's manipulatives", "Mixed-skills activity trays", "Mini-whiteboards"],
    },
    {
        "topic": "Revision",
        "subtopic": "Ready for the Practical Check",
        "codes": [],
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
        "codes": [],
        "objectives": [
            "Show doubling, halving, sharing and odd/even skills.",
            "Show money, time and data-handling skills.",
            "Show a chosen problem-solving strategy, explaining the working out.",
        ],
        "resources": ["Assessment task cards", "Counters/cubes", "Play coins"],
    },
    {
        "topic": "End of Term Project",
        "subtopic": "Maths Fair Stall — Plan and Practise",
        "codes": [],
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
        "codes": [],
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
        "codes": [],
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
        "codes": [],
        "objectives": [
            "Run their maths stall for visiting classmates or family.",
            "Play a classmate's stall game and give one kind comment.",
            "Reflect on their favourite maths topic from the whole year.",
        ],
        "resources": ["All finished stalls", "Simple 'kind comment' sentence starters", "Certificates (optional)"],
    },
]

TERMS = {"term-1": TERM1, "term-2": TERM2, "term-3": TERM3}
