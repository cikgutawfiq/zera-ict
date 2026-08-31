"""Year 1 Maths scope & sequence, mapped to Oak National Academy's Year 1
Maths units (https://www.thenational.academy/teachers/programmes/maths-
primary/units) -- real unit titles/order/lesson-counts, not verbatim Oak
lesson content. Each unit is allocated a number of our weeks roughly
proportional to its Oak lesson count (15-lesson units get 2 weeks, 5-lesson
units get 1), so all 18 units fit exactly into the 24 content weeks
available across the 3 terms:

  Term 1 (weeks 1-8): units 1-5   -- counting, comparing, 2D/3D shape
  Term 2 (weeks 1-8): units 6-11a -- composition of numbers, addition/
                                     subtraction facts (unit 11 spans the
                                     Term 2/3 boundary, which is normal --
                                     a unit can run across terms)
  Term 3 (weeks 1-8): units 11b-18 -- composition 11-19, coins, position,
                                       time

Maths Y1 meets 3x/week (Tue/Thu/Fri); build_maths_y1.py turns each of these
weeks into 3 session-lessons (explore / practise / consolidate), each with
its own editable content and Done status.
"""

# --- Term 1: Units 1-5 (15 weeks total incl. meta weeks; 8 content weeks) ---
TERM1 = [
    {
        "topic": "Counting, Recognising and Comparing Numbers 0-10",
        "subtopic": "Say, Read and Match Numbers to Objects",
        "source": "Oak National Academy — Year 1 Maths, Unit 1 (Part 1 of 2)",
        "objectives": [
            "Count a group of objects up to 10, touching each one once.",
            "Read and recognise numerals 0-10.",
            "Match a numeral to the correct number of objects.",
        ],
        "resources": ["Counting cubes or bears", "Number cards 0-10", "A number line 0-10"],
    },
    {
        "topic": "Counting, Recognising and Comparing Numbers 0-10",
        "subtopic": "Comparing: More, Fewer and the Same",
        "source": "Oak National Academy — Year 1 Maths, Unit 1 (Part 2 of 2)",
        "objectives": [
            "Compare two groups of objects and say which has more or fewer.",
            "Use the words 'more than', 'fewer than' and 'the same as' correctly.",
            "Order a small set of numbers 0-10.",
        ],
        "resources": ["Two colours of counters", "Comparison mats (two hoops)", "Number cards 0-10"],
    },
    {
        "topic": "Counting to and from 20",
        "subtopic": "Say, Read and Count On to 20",
        "source": "Oak National Academy — Year 1 Maths, Unit 2 (Part 1 of 2)",
        "objectives": [
            "Count on from any number to 20.",
            "Read and recognise numerals 11-20.",
            "Count a group of up to 20 objects accurately.",
        ],
        "resources": ["Counting cubes or bears", "Number cards 0-20", "A number line 0-20"],
    },
    {
        "topic": "Counting to and from 20",
        "subtopic": "Counting Back from 20",
        "source": "Oak National Academy — Year 1 Maths, Unit 2 (Part 2 of 2)",
        "objectives": [
            "Count back from 20 to 0.",
            "Find the number that is one more or one less than a given number to 20.",
            "Say a missing number on a number line 0-20.",
        ],
        "resources": ["Number line 0-20", "Number cards 0-20", "Mini-whiteboards"],
    },
    {
        "topic": "Counting in Tens — Decade Numbers",
        "subtopic": "Counting On in Tens: 10, 20, 30...",
        "source": "Oak National Academy — Year 1 Maths, Unit 3",
        "objectives": [
            "Count on in tens from 0.",
            "Recognise the decade numbers (10, 20, 30...) up to 100.",
            "Say what comes next in a count of tens.",
        ],
        "resources": ["Bundles of ten straws or cubes", "A 1-100 number square", "Mini-whiteboards"],
    },
    {
        "topic": "Pattern in Counting from 20 to 100",
        "subtopic": "Spotting the Pattern in the Tens",
        "source": "Oak National Academy — Year 1 Maths, Unit 4",
        "objectives": [
            "Recite numbers forwards from 20 towards 100.",
            "Spot the repeating pattern in the ones digit as the tens change.",
            "Use a 1-100 number square to find a given number.",
        ],
        "resources": ["A 1-100 number square", "Number cards 21-100", "Mini-whiteboards"],
    },
    {
        "topic": "Comparing Quantities — Part-Part-Whole",
        "subtopic": "Splitting a Whole into Two Parts",
        "source": "Oak National Academy — Year 1 Maths, Unit 5 (Part 1 of 2)",
        "objectives": [
            "Split a group of objects into two parts and say how many are in each.",
            "Use a part-part-whole model (e.g. a bar or two hoops) to show this.",
            "Find different ways to split the same whole number.",
        ],
        "resources": ["Counters", "Part-part-whole mats/hoops", "Mini-whiteboards"],
    },
    {
        "topic": "Comparing Quantities — Part-Part-Whole",
        "subtopic": "Finding a Missing Part or the Whole",
        "source": "Oak National Academy — Year 1 Maths, Unit 5 (Part 2 of 2)",
        "objectives": [
            "Given the whole and one part, work out the missing part.",
            "Given two parts, work out the whole.",
            "Explain their thinking using the part-part-whole model.",
        ],
        "resources": ["Counters", "Part-part-whole mats/hoops", "Mini-whiteboards"],
    },
    {
        "topic": "Consolidation",
        "subtopic": "Number and Comparing Skills Rotation",
        "source": "",
        "objectives": [
            "Revisit counting, comparing and ordering numbers to 20.",
            "Revisit counting in tens and the pattern to 100.",
            "Revisit the part-part-whole model.",
        ],
        "resources": ["All Term 1 manipulatives so far", "Mixed-skills activity trays", "Mini-whiteboards"],
    },
    {
        "topic": "Revision",
        "subtopic": "Ready for the Practical Check",
        "source": "",
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
        "source": "",
        "objectives": [
            "Show counting, comparing and ordering of numbers to 20.",
            "Show counting in tens and the pattern to 100.",
            "Show understanding of the part-part-whole model.",
        ],
        "resources": ["Assessment task cards", "Counters/cubes", "Number square"],
    },
    {
        "topic": "End of Term Project",
        "subtopic": "'My Number Storybook' — Plan and Count",
        "source": "",
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
        "source": "",
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
        "source": "",
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
        "source": "",
        "objectives": [
            "Read or present the number storybook to a partner or small group.",
            "Listen politely to a classmate's storybook and give one kind comment.",
            "Reflect on what they learned about numbers this term.",
        ],
        "resources": ["Finished storybooks", "Simple 'kind comment' sentence starters", "Certificates (optional)"],
    },
]

# --- Term 2: Units 6-11 (part), 11 weeks total; 8 content weeks ---
TERM2 = [
    {
        "topic": "Composition of Numbers 0 to 5",
        "subtopic": "All the Ways to Make Each Number to 5",
        "source": "Oak National Academy — Year 1 Maths, Unit 6",
        "objectives": [
            "Find different ways to make a number up to 5 from two parts.",
            "Represent a number to 5 using objects, fingers or a picture.",
            "Recognise that a number can be made of different combinations.",
        ],
        "resources": ["Counters", "Five-frame boards", "Mini-whiteboards"],
    },
    {
        "topic": "2D and 3D Shapes",
        "subtopic": "Recognise and Sort 2D Shapes",
        "source": "Oak National Academy — Year 1 Maths, Unit 7 (Part 1 of 2)",
        "objectives": [
            "Name a circle, square, triangle and rectangle correctly.",
            "Sort a mixed set of 2D shapes by name and by features.",
            "Compose and decompose shapes to make new pictures or patterns.",
        ],
        "resources": ["Shape tiles/blocks", "A 'shape hunt' checklist", "Sorting hoops or trays"],
    },
    {
        "topic": "2D and 3D Shapes",
        "subtopic": "Recognise, Compose and Manipulate 3D Shapes",
        "source": "Oak National Academy — Year 1 Maths, Unit 7 (Part 2 of 2)",
        "objectives": [
            "Name a cube, cuboid, cylinder, cone and sphere correctly.",
            "Build a model by combining 3D shapes.",
            "Match a 3D shape name to an everyday object.",
        ],
        "resources": ["3D shape set", "Everyday objects (ball, tin, box, party hat)", "Building blocks"],
    },
    {
        "topic": "Composition of Numbers 6 to 10",
        "subtopic": "All the Ways to Make Each Number to 10 (Part 1)",
        "source": "Oak National Academy — Year 1 Maths, Unit 8 (Part 1 of 2)",
        "objectives": [
            "Find different ways to make 6, 7 and 8 from two parts.",
            "Represent these numbers using a ten-frame.",
            "Record a number sentence for a combination found.",
        ],
        "resources": ["Ten-frame boards", "Counters", "Mini-whiteboards"],
    },
    {
        "topic": "Composition of Numbers 6 to 10",
        "subtopic": "All the Ways to Make Each Number to 10 (Part 2)",
        "source": "Oak National Academy — Year 1 Maths, Unit 8 (Part 2 of 2)",
        "objectives": [
            "Find different ways to make 9 and 10 from two parts.",
            "Know, by heart, at least one pair of numbers that makes 10.",
            "Compare combinations found by different pupils.",
        ],
        "resources": ["Ten-frame boards", "Counters", "Mini-whiteboards"],
    },
    {
        "topic": "Additive Structures: Addition",
        "subtopic": "Combining Two Groups and Counting All",
        "source": "Oak National Academy — Year 1 Maths, Unit 9",
        "objectives": [
            "Combine two small groups of objects and count the total.",
            "Use the '+' and '=' signs to record a simple addition.",
            "Solve a simple 'how many altogether?' story problem.",
        ],
        "resources": ["Counters or cubes", "Mini-whiteboards", "Simple picture addition story cards"],
    },
    {
        "topic": "Additive Structures: Addition and Subtraction",
        "subtopic": "Take Away and 'How Many More to Make?'",
        "source": "Oak National Academy — Year 1 Maths, Unit 10",
        "objectives": [
            "Understand subtraction as counting back and 'take away'.",
            "Understand difference as 'how many more to make?'.",
            "Choose whether a story problem needs addition or subtraction.",
        ],
        "resources": ["Counters or cubes", "Mini-whiteboards", "Mixed addition/subtraction story cards"],
    },
    {
        "topic": "Addition and Subtraction Facts Within 10",
        "subtopic": "Know Facts to 10 by Heart (Part 1)",
        "source": "Oak National Academy — Year 1 Maths, Unit 11 (Part 1 of 2)",
        "objectives": [
            "Know, by heart, the pairs of numbers that add to 10.",
            "Recall related subtraction facts for pairs to 10.",
            "Use a ten-frame to check a fact quickly.",
        ],
        "resources": ["Ten-frame boards", "Number-pair domino cards", "Mini-whiteboards"],
    },
    {
        "topic": "Consolidation",
        "subtopic": "Composition and Additive Structures Skills Rotation",
        "source": "",
        "objectives": [
            "Revisit composition of numbers to 10.",
            "Revisit addition and subtraction as combining/taking away.",
            "Revisit 2D and 3D shape recognition.",
        ],
        "resources": ["All Term 2 manipulatives", "Mixed-skills activity trays", "Mini-whiteboards"],
    },
    {
        "topic": "Revision",
        "subtopic": "Ready for the Practical Check",
        "source": "",
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
        "source": "",
        "objectives": [
            "Show composition of numbers to 10.",
            "Show addition and subtraction strategies.",
            "Show 2D and 3D shape recognition.",
        ],
        "resources": ["Assessment task cards", "Ten-frame boards", "Shape set"],
    },
]

# --- Term 3: Units 11 (rest), 12-18, 15 weeks total; 8 content weeks ---
TERM3 = [
    {
        "topic": "Addition and Subtraction Facts Within 10",
        "subtopic": "Know Facts to 10 by Heart (Part 2)",
        "source": "Oak National Academy — Year 1 Maths, Unit 11 (Part 2 of 2)",
        "objectives": [
            "Recall addition and subtraction facts to 10 with increasing speed.",
            "Use known facts to solve a related problem (e.g. 6 + 4, then 60 + 40).",
            "Explain a strategy for working out a fact not yet memorised.",
        ],
        "resources": ["Ten-frame boards", "Number-pair domino cards", "Mini-whiteboards"],
    },
    {
        "topic": "Composition of Numbers 11 to 19",
        "subtopic": "Ten and Some Ones",
        "source": "Oak National Academy — Year 1 Maths, Unit 12",
        "objectives": [
            "Show a number 11-19 as 'one ten and some ones' using a ten-frame.",
            "Explain that, e.g., 14 means 1 ten and 4 ones.",
            "Build a given number 11-19 using ten-frames and counters.",
        ],
        "resources": ["Ten-frame boards", "Counters", "Number cards 11-19"],
    },
    {
        "topic": "Numbers 0 to 20 in Different Contexts",
        "subtopic": "Using Numbers to 20 in Real Situations",
        "source": "Oak National Academy — Year 1 Maths, Unit 13",
        "objectives": [
            "Apply counting and comparing skills to a real-life context (e.g. a class survey).",
            "Read numbers to 20 in different formats (digits, words, on a dial or scale).",
            "Solve a simple word problem involving numbers to 20.",
        ],
        "resources": ["Real-life context cards (menus, tickets, scoreboards)", "Number cards 0-20", "Mini-whiteboards"],
    },
    {
        "topic": "Unitising and Coin Recognition",
        "subtopic": "Counting in 2s, 5s and 10s",
        "source": "Oak National Academy — Year 1 Maths, Unit 14",
        "objectives": [
            "Count a group of objects by counting in 2s, 5s or 10s.",
            "Recognise that grouping makes counting large amounts faster.",
            "Recognise common coins as a first step towards unitising money.",
        ],
        "resources": ["Objects to group (pairs, hands of 5, bundles of 10)", "Play coins", "Mini-whiteboards"],
    },
    {
        "topic": "Unitising and Coin Recognition",
        "subtopic": "The Value of a Set of Coins",
        "source": "Oak National Academy — Year 1 Maths, Unit 15",
        "objectives": [
            "Recognise and name common coins.",
            "Find the total value of a small set of same-value coins.",
            "Solve a simple 'how much altogether?' problem with coins.",
        ],
        "resources": ["Play coins", "Simple price-tag picture cards", "Mini-whiteboards"],
    },
    {
        "topic": "Solving Problems in a Range of Contexts",
        "subtopic": "Choosing the Right Maths for the Problem",
        "source": "Oak National Academy — Year 1 Maths, Unit 16",
        "objectives": [
            "Decide which skill from this year (counting, comparing, adding, subtracting) a problem needs.",
            "Solve a mixed problem using objects, drawings or a number line.",
            "Explain how they solved a problem to a partner.",
        ],
        "resources": ["Mixed problem cards", "Counters/small objects", "Mini-whiteboards"],
    },
    {
        "topic": "Position and Direction",
        "subtopic": "Above, Below, Left, Right and Fractions of a Turn",
        "source": "Oak National Academy — Year 1 Maths, Unit 17",
        "objectives": [
            "Use everyday words for direction and distance.",
            "Follow a simple direction to move an object or themselves.",
            "Recognise a quarter turn and a half turn, clockwise and anti-clockwise.",
        ],
        "resources": ["Floor grid or playground chalk grid", "A toy or counter to move", "Direction cards"],
    },
    {
        "topic": "Time",
        "subtopic": "Sequencing Events and Telling the Time to the Hour and Half Hour",
        "source": "Oak National Academy — Year 1 Maths, Unit 18",
        "objectives": [
            "Order a small set of familiar events using 'before', 'after' and 'next'.",
            "Read o'clock times on an analogue clock.",
            "Read half past times on an analogue clock.",
        ],
        "resources": ["Teaching clock (geared, if available)", "Individual mini-clocks", "Daily-routine picture cards"],
    },
    {
        "topic": "Consolidation",
        "subtopic": "Whole-Year Skills Rotation",
        "source": "",
        "objectives": [
            "Revisit number, shape, measure and problem-solving skills from across the year.",
            "Choose an area they want more practice in and work on it.",
            "Help a partner with a skill they find secure.",
        ],
        "resources": ["A full year's manipulatives", "Mixed-skills activity trays", "Mini-whiteboards"],
    },
    {
        "topic": "Revision",
        "subtopic": "Ready for the Practical Check",
        "source": "",
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
        "source": "",
        "objectives": [
            "Show composition, coin and problem-solving skills.",
            "Show position, direction and time skills.",
            "Show a chosen strategy, explaining the working out.",
        ],
        "resources": ["Assessment task cards", "Counters/cubes", "Play coins"],
    },
    {
        "topic": "End of Term Project",
        "subtopic": "Maths Fair Stall — Plan and Practise",
        "source": "",
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
        "source": "",
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
        "source": "",
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
        "source": "",
        "objectives": [
            "Run their maths stall for visiting classmates or family.",
            "Play a classmate's stall game and give one kind comment.",
            "Reflect on their favourite maths topic from the whole year.",
        ],
        "resources": ["All finished stalls", "Simple 'kind comment' sentence starters", "Certificates (optional)"],
    },
]

TERMS = {"term-1": TERM1, "term-2": TERM2, "term-3": TERM3}
