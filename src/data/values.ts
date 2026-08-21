/**
 * Moral value + quote + food-for-thought bank.
 *
 * Each lesson gets one moral value, one quote (with author) and one short
 * reflection prompt. Assignment is deterministic and per-class: every class
 * (e.g. ICT Y5) walks the two lists in a fixed order that starts at a
 * different offset per class, so within a single class no value or quote
 * repeats across the whole year (up to 41 lessons — the pool has 41 entries),
 * while two different classes can land on the same one in the same week —
 * that's fine, since different pupils see it.
 *
 * assignMoralContent(classId, indexInClassYear) is called once per lesson in
 * chronological order (Term 1 week 1 first, ..., Term 3 last week) with a
 * running index — see scripts/build_seed.py for the Python mirror used at
 * seed time, and src/lib/parseSow.ts for the browser-upload path.
 */

export type MoralEntry = { value: string; description: string };
export type QuoteEntry = { text: string; author: string };

// 41 entries — exactly enough for the 41 lessons any one class sees across a
// full year (15 + 11 + 15 weeks), so no class ever wraps around and repeats.
export const MORAL_VALUES: MoralEntry[] = [
  { value: "Patience", description: "Good work takes time — slow down and get it right." },
  { value: "Honesty", description: "Tell the truth about your work, including your mistakes." },
  { value: "Perseverance", description: "Keep trying even when the first attempt does not work." },
  { value: "Kindness", description: "A kind word to a struggling classmate costs nothing." },
  { value: "Responsibility", description: "Own your work, your files and your mistakes." },
  { value: "Curiosity", description: "Ask 'why' and 'what if' — that is where real learning starts." },
  { value: "Respect", description: "Respect other people's work, ideas and privacy." },
  { value: "Cooperation", description: "The best projects are built by people who help each other." },
  { value: "Diligence", description: "Small, steady effort beats a rushed burst at the end." },
  { value: "Courage", description: "Sharing unfinished work for feedback takes courage — and pays off." },
  { value: "Gratitude", description: "Notice and thank the people who help you learn." },
  { value: "Integrity", description: "Do the right thing even when nobody is checking." },
  { value: "Humility", description: "The best learners admit what they do not know yet." },
  { value: "Fairness", description: "Give credit where it's due, and take feedback the same way you'd give it." },
  { value: "Self-discipline", description: "Doing the boring warm-up daily is what makes the fun part possible." },
  { value: "Empathy", description: "Design for the person who will actually use what you make." },
  { value: "Resilience", description: "A bug or a crash is information, not a verdict on you." },
  { value: "Generosity", description: "Share what you have figured out — it does not run out." },
  { value: "Focus", description: "One task done well beats five tasks half-done." },
  { value: "Trustworthiness", description: "Do what you said you would do, especially when no one is watching." },
  { value: "Open-mindedness", description: "Someone else's way of solving it might be better than yours." },
  { value: "Precision", description: "In computing, close enough is often not close enough." },
  { value: "Courtesy", description: "Online or offline, good manners cost nothing and change everything." },
  { value: "Initiative", description: "Don't wait to be told — if you can see the next step, take it." },
  { value: "Accountability", description: "If it's your file, it's your responsibility." },
  { value: "Optimism", description: "Assume the next attempt can work, and it usually does." },
  { value: "Thoughtfulness", description: "Think about who reads your work before you publish it." },
  { value: "Discretion", description: "Not everything needs to be posted, sent or shared." },
  { value: "Teamwork", description: "A team that communicates clearly finishes faster than one that doesn't." },
  { value: "Adaptability", description: "Plans change; good learners adjust without giving up." },
  { value: "Punctuality", description: "Being on time and ready to start respects everyone else's time too." },
  { value: "Modesty", description: "Let good work speak for itself." },
  { value: "Compassion", description: "Notice when a classmate is struggling, and offer to help before they ask." },
  { value: "Creativity", description: "There is rarely only one right way to solve a problem." },
  { value: "Vigilance", description: "A careless click online can undo a lot of careful work." },
  { value: "Loyalty", description: "Stick with your team and your commitments, especially when it's hard." },
  { value: "Wisdom", description: "Knowing when NOT to use a shortcut is as important as knowing the shortcut." },
  { value: "Enthusiasm", description: "Bring energy to a task and it usually goes better." },
  { value: "Reliability", description: "Be the person whose saved file is always where they said it would be." },
  { value: "Stewardship", description: "Take care of shared equipment and shared files — they are not just yours." },
  { value: "Consideration", description: "Think about how your choices affect the people working near you." },
];

export const QUOTES: QuoteEntry[] = [
  { text: "It always seems impossible until it's done.", author: "Nelson Mandela" },
  { text: "The expert in anything was once a beginner.", author: "Helen Hayes" },
  { text: "Success is the sum of small efforts, repeated day in and day out.", author: "Robert Collier" },
  { text: "Do not wait for the perfect moment. Take the moment and make it perfect.", author: "Unknown" },
  { text: "The only way to do great work is to love what you do.", author: "Steve Jobs" },
  { text: "Mistakes are proof that you are trying.", author: "Unknown" },
  { text: "A person who never made a mistake never tried anything new.", author: "Albert Einstein" },
  { text: "Well done is better than well said.", author: "Benjamin Franklin" },
  { text: "It is not that I'm so smart. I just stay with problems longer.", author: "Albert Einstein" },
  { text: "Give me six hours to chop down a tree and I will spend the first four sharpening the axe.", author: "Abraham Lincoln" },
  { text: "The best way to predict the future is to create it.", author: "Peter Drucker" },
  { text: "Quality is not an act, it is a habit.", author: "Aristotle" },
  { text: "You don't have to be great to start, but you have to start to be great.", author: "Zig Ziglar" },
  { text: "Simplicity is the ultimate sophistication.", author: "Leonardo da Vinci" },
  { text: "Debugging is twice as hard as writing the code in the first place.", author: "Brian Kernighan" },
  { text: "First, solve the problem. Then, write the code.", author: "John Johnson" },
  { text: "Talk is cheap. Show me the code.", author: "Linus Torvalds" },
  { text: "The computer was born to solve problems that did not exist before.", author: "Bill Gates" },
  { text: "Everybody in this country should learn to program a computer, because it teaches you how to think.", author: "Steve Jobs" },
  { text: "Technology is best when it brings people together.", author: "Matt Mullenweg" },
  { text: "Coming together is a beginning; keeping together is progress; working together is success.", author: "Henry Ford" },
  { text: "If you want to go fast, go alone. If you want to go far, go together.", author: "African proverb" },
  { text: "Kind words can be short and easy to speak, but their echoes are truly endless.", author: "Mother Teresa" },
  { text: "Honesty is the first chapter in the book of wisdom.", author: "Thomas Jefferson" },
  { text: "The way to get started is to quit talking and begin doing.", author: "Walt Disney" },
  { text: "You miss 100 percent of the shots you don't take.", author: "Wayne Gretzky" },
  { text: "Fall seven times, stand up eight.", author: "Japanese proverb" },
  { text: "What we learn with pleasure we never forget.", author: "Alfred Mercier" },
  { text: "Learning never exhausts the mind.", author: "Leonardo da Vinci" },
  { text: "Genius is one percent inspiration and ninety-nine percent perspiration.", author: "Thomas Edison" },
  { text: "Do the best you can until you know better. Then, when you know better, do better.", author: "Maya Angelou" },
  { text: "A ship is safe in harbour, but that's not what ships are for.", author: "William Shedd" },
  { text: "In the middle of difficulty lies opportunity.", author: "Albert Einstein" },
  { text: "The only real mistake is the one from which we learn nothing.", author: "Henry Ford" },
  { text: "Small daily improvements are the key to staggering long-term results.", author: "James Clear" },
  { text: "Alone we can do so little; together we can do so much.", author: "Helen Keller" },
  { text: "Whether you think you can, or you think you can't — you're right.", author: "Henry Ford" },
  { text: "Good, better, best. Never let it rest until your good is better and your better is best.", author: "St. Jerome" },
  { text: "A goal without a plan is just a wish.", author: "Antoine de Saint-Exupery" },
  { text: "Character is doing the right thing when nobody's looking.", author: "J.C. Watts" },
  { text: "Well begun is half done.", author: "Aristotle" },
];

export type MoralContent = {
  moralValue: string;
  moralDescription: string;
  quote: string;
  quoteAuthor: string;
  foodForThought: string;
};

const FOOD_FRAMES = [
  "Where in today's lesson could you practise {value}?",
  "Name one moment this week you showed {value} — or wish you had.",
  "How would today's task go differently without {value}?",
  "Who do you know that shows {value} well? What do they do?",
  "Is {value} always easy, or does it sometimes take effort?",
];

/**
 * Ice breaker bank — a 5-10 minute activity to open every lesson, before the
 * main plan. Pools are age-banded (KS1/KS2/KS3) so a Y1 icebreaker never
 * lands on a Y9 class. Assignment reuses the same per-class rotation as the
 * moral value bank, scoped to the class's key stage pool.
 */
export type IceBreakerEntry = { title: string; description: string; minutes: number };

export const ICE_BREAKERS_KS1: IceBreakerEntry[] = [
  { title: "Copy My Clap", description: "Clap a short rhythm, class copies it back. Speed it up each round.", minutes: 5 },
  { title: "Freeze Dance", description: "Play music, everyone dances; when it stops, freeze like a statue.", minutes: 5 },
  { title: "Simon Says", description: "Classic Simon Says with computer-themed actions: 'click', 'type', 'save'.", minutes: 5 },
  { title: "Two Truths and a Wish", description: "Each pupil says two true things and one thing they wish were true; partner guesses which.", minutes: 8 },
  { title: "Animal Walk Around", description: "Walk around the room like different animals when the teacher calls one out.", minutes: 5 },
  { title: "Would You Rather", description: "Ask a silly 'would you rather' question; pupils move to one side of the room to vote.", minutes: 6 },
  { title: "Name That Sound", description: "Play three short sound clips; pupils guess what each one is.", minutes: 6 },
  { title: "High Five Train", description: "Everyone stands and gives a high five to five different classmates before sitting.", minutes: 5 },
  { title: "Colour Hunt", description: "Call out a colour; pupils touch something that colour in the room as fast as they can.", minutes: 5 },
  { title: "Story Starter", description: "Teacher starts a silly one-sentence story; each pupil adds one sentence around the circle.", minutes: 8 },
  { title: "Mirror Me", description: "In pairs, one leads slow movements, the other mirrors them exactly.", minutes: 6 },
  { title: "Guess the Emotion", description: "Pull an emotion card and act it out silently; class guesses the feeling.", minutes: 6 },
  { title: "Thumbs Up Weather Check", description: "Everyone shows how they're feeling with a thumbs up, sideways or down, and one word why.", minutes: 5 },
  { title: "Silent Line-Up", description: "Line up in height order (or birthday month) without talking, using only gestures.", minutes: 7 },
  { title: "Balloon Keep-Up", description: "Keep a balloon off the floor as a group, counting taps out loud together.", minutes: 6 },
];

export const ICE_BREAKERS_KS2: IceBreakerEntry[] = [
  { title: "20 Questions: Tech Edition", description: "Think of a device or app; class asks yes/no questions to guess it in 20 tries.", minutes: 8 },
  { title: "Human Bingo", description: "Find classmates who match a fact on a bingo card ('has a pet', 'likes maths') and get their initials.", minutes: 8 },
  { title: "Two Truths and a Lie", description: "Each pupil states two true facts and one false one; partner guesses the lie.", minutes: 8 },
  { title: "Speed Sketch", description: "Draw a given word in 30 seconds; partner guesses what it is.", minutes: 6 },
  { title: "Word Association Chain", description: "Say a word linked to the last one said, going around the room, no repeats.", minutes: 6 },
  { title: "Would You Rather: Tech Edition", description: "Pose two tech dilemmas (e.g. lose your keyboard or your mouse); pupils vote and justify.", minutes: 7 },
  { title: "One-Word Story", description: "Build a story one word at a time around the circle, then read it back for laughs.", minutes: 7 },
  { title: "Emoji Translate", description: "Show a short sentence in emoji; pupils race to translate it back to words.", minutes: 6 },
  { title: "The Great Paperclip Challenge", description: "In pairs, build the tallest free-standing tower from 10 paperclips in 3 minutes.", minutes: 8 },
  { title: "Guess the Rule", description: "Teacher sorts objects/words by a secret rule; pupils guess the rule by suggesting the next item.", minutes: 8 },
  { title: "Would You Rather Corners", description: "Post two options on opposite walls; pupils physically move to their choice and defend it.", minutes: 7 },
  { title: "Rapid Fire Categories", description: "Call a category (fruits, coding words); pupils take turns naming one until someone's stuck.", minutes: 6 },
  { title: "Mystery Object Bag", description: "Feel a hidden object in a bag and describe it with clues; class guesses what it is.", minutes: 7 },
  { title: "Silent Sort", description: "Without talking, physically line up by a criterion (age, house number) using only gestures.", minutes: 7 },
  { title: "This or That Rapid Round", description: "Quickfire this-or-that questions; pupils answer with a show of hands, fastest round wins.", minutes: 5 },
];

export const ICE_BREAKERS_KS3: IceBreakerEntry[] = [
  { title: "Two Truths and a Lie: Tech Edition", description: "Share two true facts and one false one about tech habits; class votes on the lie.", minutes: 8 },
  { title: "60-Second Debate", description: "Pose a light debate topic (e.g. 'phones in class: yes or no'); pairs argue opposite sides for 60 seconds each.", minutes: 8 },
  { title: "Rapid Recall Quiz", description: "Five rapid-fire recall questions from last lesson, answered on mini whiteboards.", minutes: 6 },
  { title: "Would You Rather: Career Edition", description: "Pose two tech-career dilemmas; pupils vote and give one reason for their choice.", minutes: 7 },
  { title: "One Word Check-In", description: "Each pupil shares one word describing their mood or week so far, no explanation needed.", minutes: 5 },
  { title: "Guess the Acronym", description: "Show a tech acronym (RAM, URL, IDE); first to correctly expand it wins the round.", minutes: 6 },
  { title: "Human Knot", description: "Small groups link hands in a tangle, then work together silently to untangle without letting go.", minutes: 8 },
  { title: "Two-Minute Pitch", description: "Pair up and pitch a random object as if selling it, then swap partners.", minutes: 8 },
  { title: "Fact or Fake", description: "Read out a surprising tech fact; class votes real or made up before the reveal.", minutes: 6 },
  { title: "Speed Networking", description: "60 seconds each to introduce themselves to a new partner using three set questions, then rotate.", minutes: 8 },
  { title: "This or That: Coding Edition", description: "Quickfire binary choices (tabs or spaces, light mode or dark mode) with hands-up voting.", minutes: 5 },
  { title: "Silent Debate", description: "Write an opinion on paper and pass it around, adding written responses in silence for two minutes.", minutes: 8 },
  { title: "Two-Truths Tech Trivia", description: "Teacher states two true and one false tech fact; class discusses in pairs before voting.", minutes: 7 },
  { title: "Elevator Pitch Swap", description: "Explain what was learned last lesson in 30 seconds, as if to someone who missed it.", minutes: 6 },
  { title: "Would You Rather: AI Edition", description: "Pose a light AI-ethics dilemma; pupils vote with their feet and defend their side briefly.", minutes: 8 },
];

const ICE_BREAKER_POOLS: Record<string, IceBreakerEntry[]> = {
  KS1: ICE_BREAKERS_KS1,
  KS2: ICE_BREAKERS_KS2,
  KS3: ICE_BREAKERS_KS3,
};

export type IceBreakerAssignment = {
  iceBreakerTitle: string;
  iceBreakerDescription: string;
  iceBreakerMinutes: number;
};

export function assignIceBreaker(
  classId: string,
  keyStage: string,
  indexInClassYear: number,
): IceBreakerAssignment {
  const pool = ICE_BREAKER_POOLS[keyStage] ?? ICE_BREAKERS_KS2;
  const offset = hashOffset(classId + "::icebreaker", pool.length);
  const entry = pool[(offset + indexInClassYear) % pool.length];
  return {
    iceBreakerTitle: entry.title,
    iceBreakerDescription: entry.description,
    iceBreakerMinutes: entry.minutes,
  };
}

/** Simple string hash so each classId gets a stable, spread-out starting offset. */
function hashOffset(classId: string, modulo: number): number {
  let h = 0;
  for (let i = 0; i < classId.length; i++) h = (h * 31 + classId.charCodeAt(i)) >>> 0;
  return h % modulo;
}

/**
 * indexInClassYear: 0-based position of this lesson within that class's full
 * chronological run of lessons for the academic year (Term 1 first lesson = 0).
 */
export function assignMoralContent(classId: string, indexInClassYear: number): MoralContent {
  const moralOffset = hashOffset(classId, MORAL_VALUES.length);
  const quoteOffset = hashOffset(classId + "::quote", QUOTES.length);
  const moral = MORAL_VALUES[(moralOffset + indexInClassYear) % MORAL_VALUES.length];
  const quote = QUOTES[(quoteOffset + indexInClassYear) % QUOTES.length];
  const frame = FOOD_FRAMES[indexInClassYear % FOOD_FRAMES.length];
  return {
    moralValue: moral.value,
    moralDescription: moral.description,
    quote: quote.text,
    quoteAuthor: quote.author,
    foodForThought: frame.replace("{value}", moral.value.toLowerCase()),
  };
}
