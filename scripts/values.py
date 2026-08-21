"""Python mirror of src/data/values.ts — keep the two lists in sync.

Used by build_seed.py so the seed JSON already carries moralValue / quote /
quoteAuthor / foodForThought per lesson. The browser-side uploader
(src/lib/parseSow.ts) uses the TS original for the same computation when new
lessons are created from a re-uploaded workbook.
"""

MORAL_VALUES = [
    ("Patience", "Good work takes time - slow down and get it right."),
    ("Honesty", "Tell the truth about your work, including your mistakes."),
    ("Perseverance", "Keep trying even when the first attempt does not work."),
    ("Kindness", "A kind word to a struggling classmate costs nothing."),
    ("Responsibility", "Own your work, your files and your mistakes."),
    ("Curiosity", "Ask 'why' and 'what if' - that is where real learning starts."),
    ("Respect", "Respect other people's work, ideas and privacy."),
    ("Cooperation", "The best projects are built by people who help each other."),
    ("Diligence", "Small, steady effort beats a rushed burst at the end."),
    ("Courage", "Sharing unfinished work for feedback takes courage - and pays off."),
    ("Gratitude", "Notice and thank the people who help you learn."),
    ("Integrity", "Do the right thing even when nobody is checking."),
    ("Humility", "The best learners admit what they do not know yet."),
    ("Fairness", "Give credit where it's due, and take feedback the same way you'd give it."),
    ("Self-discipline", "Doing the boring warm-up daily is what makes the fun part possible."),
    ("Empathy", "Design for the person who will actually use what you make."),
    ("Resilience", "A bug or a crash is information, not a verdict on you."),
    ("Generosity", "Share what you have figured out - it does not run out."),
    ("Focus", "One task done well beats five tasks half-done."),
    ("Trustworthiness", "Do what you said you would do, especially when no one is watching."),
    ("Open-mindedness", "Someone else's way of solving it might be better than yours."),
    ("Precision", "In computing, close enough is often not close enough."),
    ("Courtesy", "Online or offline, good manners cost nothing and change everything."),
    ("Initiative", "Don't wait to be told - if you can see the next step, take it."),
    ("Accountability", "If it's your file, it's your responsibility."),
    ("Optimism", "Assume the next attempt can work, and it usually does."),
    ("Thoughtfulness", "Think about who reads your work before you publish it."),
    ("Discretion", "Not everything needs to be posted, sent or shared."),
    ("Teamwork", "A team that communicates clearly finishes faster than one that doesn't."),
    ("Adaptability", "Plans change; good learners adjust without giving up."),
    ("Punctuality", "Being on time and ready to start respects everyone else's time too."),
    ("Modesty", "Let good work speak for itself."),
    ("Compassion", "Notice when a classmate is struggling, and offer to help before they ask."),
    ("Creativity", "There is rarely only one right way to solve a problem."),
    ("Vigilance", "A careless click online can undo a lot of careful work."),
    ("Loyalty", "Stick with your team and your commitments, especially when it's hard."),
    ("Wisdom", "Knowing when NOT to use a shortcut is as important as knowing the shortcut."),
    ("Enthusiasm", "Bring energy to a task and it usually goes better."),
    ("Reliability", "Be the person whose saved file is always where they said it would be."),
    ("Stewardship", "Take care of shared equipment and shared files - they are not just yours."),
    ("Consideration", "Think about how your choices affect the people working near you."),
]

QUOTES = [
    ("It always seems impossible until it's done.", "Nelson Mandela"),
    ("The expert in anything was once a beginner.", "Helen Hayes"),
    ("Success is the sum of small efforts, repeated day in and day out.", "Robert Collier"),
    ("Do not wait for the perfect moment. Take the moment and make it perfect.", "Unknown"),
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("Mistakes are proof that you are trying.", "Unknown"),
    ("A person who never made a mistake never tried anything new.", "Albert Einstein"),
    ("Well done is better than well said.", "Benjamin Franklin"),
    ("It is not that I'm so smart. I just stay with problems longer.", "Albert Einstein"),
    ("Give me six hours to chop down a tree and I will spend the first four sharpening the axe.", "Abraham Lincoln"),
    ("The best way to predict the future is to create it.", "Peter Drucker"),
    ("Quality is not an act, it is a habit.", "Aristotle"),
    ("You don't have to be great to start, but you have to start to be great.", "Zig Ziglar"),
    ("Simplicity is the ultimate sophistication.", "Leonardo da Vinci"),
    ("Debugging is twice as hard as writing the code in the first place.", "Brian Kernighan"),
    ("First, solve the problem. Then, write the code.", "John Johnson"),
    ("Talk is cheap. Show me the code.", "Linus Torvalds"),
    ("The computer was born to solve problems that did not exist before.", "Bill Gates"),
    ("Everybody in this country should learn to program a computer, because it teaches you how to think.", "Steve Jobs"),
    ("Technology is best when it brings people together.", "Matt Mullenweg"),
    ("Coming together is a beginning; keeping together is progress; working together is success.", "Henry Ford"),
    ("If you want to go fast, go alone. If you want to go far, go together.", "African proverb"),
    ("Kind words can be short and easy to speak, but their echoes are truly endless.", "Mother Teresa"),
    ("Honesty is the first chapter in the book of wisdom.", "Thomas Jefferson"),
    ("The way to get started is to quit talking and begin doing.", "Walt Disney"),
    ("You miss 100 percent of the shots you don't take.", "Wayne Gretzky"),
    ("Fall seven times, stand up eight.", "Japanese proverb"),
    ("What we learn with pleasure we never forget.", "Alfred Mercier"),
    ("Learning never exhausts the mind.", "Leonardo da Vinci"),
    ("Genius is one percent inspiration and ninety-nine percent perspiration.", "Thomas Edison"),
    ("Do the best you can until you know better. Then, when you know better, do better.", "Maya Angelou"),
    ("A ship is safe in harbour, but that's not what ships are for.", "William Shedd"),
    ("In the middle of difficulty lies opportunity.", "Albert Einstein"),
    ("The only real mistake is the one from which we learn nothing.", "Henry Ford"),
    ("Small daily improvements are the key to staggering long-term results.", "James Clear"),
    ("Alone we can do so little; together we can do so much.", "Helen Keller"),
    ("Whether you think you can, or you think you can't - you're right.", "Henry Ford"),
    ("Good, better, best. Never let it rest until your good is better and your better is best.", "St. Jerome"),
    ("A goal without a plan is just a wish.", "Antoine de Saint-Exupery"),
    ("Character is doing the right thing when nobody's looking.", "J.C. Watts"),
    ("Well begun is half done.", "Aristotle"),
]

FOOD_FRAMES = [
    "Where in today's lesson could you practise {value}?",
    "Name one moment this week you showed {value} - or wish you had.",
    "How would today's task go differently without {value}?",
    "Who do you know that shows {value} well? What do they do?",
    "Is {value} always easy, or does it sometimes take effort?",
]


def hash_offset(class_id: str, modulo: int) -> int:
    h = 0
    for ch in class_id:
        h = (h * 31 + ord(ch)) & 0xFFFFFFFF
    return h % modulo


def assign_moral_content(class_id: str, index_in_class_year: int) -> dict:
    moral_offset = hash_offset(class_id, len(MORAL_VALUES))
    quote_offset = hash_offset(class_id + "::quote", len(QUOTES))
    value, description = MORAL_VALUES[(moral_offset + index_in_class_year) % len(MORAL_VALUES)]
    quote, author = QUOTES[(quote_offset + index_in_class_year) % len(QUOTES)]
    frame = FOOD_FRAMES[index_in_class_year % len(FOOD_FRAMES)]
    return {
        "moralValue": value,
        "moralDescription": description,
        "quote": quote,
        "quoteAuthor": author,
        "foodForThought": frame.replace("{value}", value.lower()),
    }
# Auto-derived from src/data/values.ts -- keep the two in sync.

ICE_BREAKERS_KS1 = [
    ("Copy My Clap", "Clap a short rhythm, class copies it back. Speed it up each round.", 5),
    ("Freeze Dance", "Play music, everyone dances; when it stops, freeze like a statue.", 5),
    ("Simon Says", "Classic Simon Says with computer-themed actions: 'click', 'type', 'save'.", 5),
    ("Two Truths and a Wish", "Each pupil says two true things and one thing they wish were true; partner guesses which.", 8),
    ("Animal Walk Around", "Walk around the room like different animals when the teacher calls one out.", 5),
    ("Would You Rather", "Ask a silly 'would you rather' question; pupils move to one side of the room to vote.", 6),
    ("Name That Sound", "Play three short sound clips; pupils guess what each one is.", 6),
    ("High Five Train", "Everyone stands and gives a high five to five different classmates before sitting.", 5),
    ("Colour Hunt", "Call out a colour; pupils touch something that colour in the room as fast as they can.", 5),
    ("Story Starter", "Teacher starts a silly one-sentence story; each pupil adds one sentence around the circle.", 8),
    ("Mirror Me", "In pairs, one leads slow movements, the other mirrors them exactly.", 6),
    ("Guess the Emotion", "Pull an emotion card and act it out silently; class guesses the feeling.", 6),
    ("Thumbs Up Weather Check", "Everyone shows how they're feeling with a thumbs up, sideways or down, and one word why.", 5),
    ("Silent Line-Up", "Line up in height order (or birthday month) without talking, using only gestures.", 7),
    ("Balloon Keep-Up", "Keep a balloon off the floor as a group, counting taps out loud together.", 6),
]

ICE_BREAKERS_KS2 = [
    ("20 Questions: Tech Edition", "Think of a device or app; class asks yes/no questions to guess it in 20 tries.", 8),
    ("Human Bingo", "Find classmates who match a fact on a bingo card ('has a pet', 'likes maths') and get their initials.", 8),
    ("Two Truths and a Lie", "Each pupil states two true facts and one false one; partner guesses the lie.", 8),
    ("Speed Sketch", "Draw a given word in 30 seconds; partner guesses what it is.", 6),
    ("Word Association Chain", "Say a word linked to the last one said, going around the room, no repeats.", 6),
    ("Would You Rather: Tech Edition", "Pose two tech dilemmas (e.g. lose your keyboard or your mouse); pupils vote and justify.", 7),
    ("One-Word Story", "Build a story one word at a time around the circle, then read it back for laughs.", 7),
    ("Emoji Translate", "Show a short sentence in emoji; pupils race to translate it back to words.", 6),
    ("The Great Paperclip Challenge", "In pairs, build the tallest free-standing tower from 10 paperclips in 3 minutes.", 8),
    ("Guess the Rule", "Teacher sorts objects/words by a secret rule; pupils guess the rule by suggesting the next item.", 8),
    ("Would You Rather Corners", "Post two options on opposite walls; pupils physically move to their choice and defend it.", 7),
    ("Rapid Fire Categories", "Call a category (fruits, coding words); pupils take turns naming one until someone's stuck.", 6),
    ("Mystery Object Bag", "Feel a hidden object in a bag and describe it with clues; class guesses what it is.", 7),
    ("Silent Sort", "Without talking, physically line up by a criterion (age, house number) using only gestures.", 7),
    ("This or That Rapid Round", "Quickfire this-or-that questions; pupils answer with a show of hands, fastest round wins.", 5),
]

ICE_BREAKERS_KS3 = [
    ("Two Truths and a Lie: Tech Edition", "Share two true facts and one false one about tech habits; class votes on the lie.", 8),
    ("60-Second Debate", "Pose a light debate topic (e.g. 'phones in class: yes or no'); pairs argue opposite sides for 60 seconds each.", 8),
    ("Rapid Recall Quiz", "Five rapid-fire recall questions from last lesson, answered on mini whiteboards.", 6),
    ("Would You Rather: Career Edition", "Pose two tech-career dilemmas; pupils vote and give one reason for their choice.", 7),
    ("One Word Check-In", "Each pupil shares one word describing their mood or week so far, no explanation needed.", 5),
    ("Guess the Acronym", "Show a tech acronym (RAM, URL, IDE); first to correctly expand it wins the round.", 6),
    ("Human Knot", "Small groups link hands in a tangle, then work together silently to untangle without letting go.", 8),
    ("Two-Minute Pitch", "Pair up and pitch a random object as if selling it, then swap partners.", 8),
    ("Fact or Fake", "Read out a surprising tech fact; class votes real or made up before the reveal.", 6),
    ("Speed Networking", "60 seconds each to introduce themselves to a new partner using three set questions, then rotate.", 8),
    ("This or That: Coding Edition", "Quickfire binary choices (tabs or spaces, light mode or dark mode) with hands-up voting.", 5),
    ("Silent Debate", "Write an opinion on paper and pass it around, adding written responses in silence for two minutes.", 8),
    ("Two-Truths Tech Trivia", "Teacher states two true and one false tech fact; class discusses in pairs before voting.", 7),
    ("Elevator Pitch Swap", "Explain what was learned last lesson in 30 seconds, as if to someone who missed it.", 6),
    ("Would You Rather: AI Edition", "Pose a light AI-ethics dilemma; pupils vote with their feet and defend their side briefly.", 8),
]


ICE_BREAKER_POOLS = {
    "KS1": ICE_BREAKERS_KS1,
    "KS2": ICE_BREAKERS_KS2,
    "KS3": ICE_BREAKERS_KS3,
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
    "maths-y1": "KS1",
    "me-y8": "KS3",
}


def assign_ice_breaker(class_id: str, index_in_class_year: int) -> dict:
    key_stage = CLASS_KEY_STAGE.get(class_id, "KS2")
    pool = ICE_BREAKER_POOLS[key_stage]
    offset = hash_offset(class_id + "::icebreaker", len(pool))
    title, description, minutes = pool[(offset + index_in_class_year) % len(pool)]
    return {
        "iceBreakerTitle": title,
        "iceBreakerDescription": description,
        "iceBreakerMinutes": minutes,
    }
