export type AltTopic = { title: string; description: string };

const ICT_KS1: AltTopic[] = [
  { title: "Keyboard Explorers", description: "Practise finding letters and symbols on a real keyboard through a game." },
  { title: "Robot Friends", description: "Give simple step-by-step directions to a floor robot or on-screen character." },
  { title: "Picture Story", description: "Use a drawing tool to create a 3-panel picture story with captions." },
  { title: "Internet Detectives", description: "Learn to spot if a picture or fact online looks true or made-up, with an adult's help." },
  { title: "Sound Recorder", description: "Record a short voice message and play it back, learning about microphones." },
  { title: "Shape Pictures", description: "Use simple shapes and colours in a paint program to build a picture of their choosing." },
];

const ICT_KS2: AltTopic[] = [
  { title: "Spreadsheet Detectives", description: "Use simple formulas to solve a class survey mystery." },
  { title: "Stop-Motion Animation", description: "Plan and shoot a short stop-motion clip using a tablet camera." },
  { title: "Website Builder", description: "Build a simple multi-page website about a hobby using a drag-and-drop tool." },
  { title: "Coding a Quiz Game", description: "Use block coding to build a quiz game with score-keeping." },
  { title: "Digital Poster Campaign", description: "Design a poster persuading classmates to care about an issue, citing sources." },
  { title: "Data Logging", description: "Use a sensor or app to record data over time and graph the results." },
];

const ICT_KS3: AltTopic[] = [
  { title: "App Prototyping", description: "Storyboard and wireframe a mobile app idea using a free prototyping tool." },
  { title: "Python Mini-Games", description: "Build a simple text-based game in Python using loops and conditionals." },
  { title: "Cyber Security Basics", description: "Investigate common online scams and design a class safety poster." },
  { title: "Database Design Project", description: "Design and build a small relational database for a real-world scenario." },
  { title: "Video Editing Challenge", description: "Edit raw footage into a 60-second short film with transitions and titles." },
  { title: "Networking Fundamentals", description: "Explore how devices connect, and build a simple network diagram." },
];

const MATHS_KS1: AltTopic[] = [
  { title: "Number Hunt", description: "Practise counting and number recognition through a treasure-hunt game." },
  { title: "Shape Detectives", description: "Sort 2D and 3D shapes found around the classroom." },
  { title: "Measuring Me", description: "Use non-standard units to measure classroom objects and each other." },
  { title: "Money Market", description: "Role-play buying and selling with play coins, practising simple addition." },
  { title: "Pattern Parade", description: "Spot, continue and create repeating patterns using objects and colours." },
  { title: "Time Tellers", description: "Practise reading clocks to the hour and half hour through games." },
];

const MALAY_KS3: AltTopic[] = [
  { title: "Peribahasa Detective", description: "Explore Malay proverbs and match them to real-life situations." },
  { title: "Dialog Harian", description: "Practise everyday conversational Malay through role-play scenarios." },
  { title: "Cerita Rakyat", description: "Read and retell a Malay folktale, then create a short comic strip." },
  { title: "Menulis Surat", description: "Practise writing a formal and an informal letter in Malay." },
  { title: "Debat Ringkas", description: "Hold a mini debate in Malay on a light-hearted topic." },
  { title: "Lagu & Lirik", description: "Analyse the lyrics of a Malay song for vocabulary and meaning." },
];

const BUCKETS: Record<string, AltTopic[]> = {
  "ICT|KS1": ICT_KS1,
  "ICT|KS2": ICT_KS2,
  "ICT|KS3": ICT_KS3,
  "Mathematics|KS1": MATHS_KS1,
  "Malay Enrichment|KS3": MALAY_KS3,
};

function shuffled<T>(items: T[]): T[] {
  const arr = [...items];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

export function pickAlternativeTopics(
  subject: string,
  keyStage: string,
  excludeTitle: string,
  count = 3,
): AltTopic[] {
  const pool = BUCKETS[`${subject}|${keyStage}`] ?? ICT_KS2;
  const filtered = pool.filter((t) => t.title.toLowerCase() !== excludeTitle.trim().toLowerCase());
  const source = filtered.length >= count ? filtered : pool;
  return shuffled(source).slice(0, count);
}
