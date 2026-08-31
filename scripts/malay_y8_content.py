"""Malay Enrichment Y8 — a beginner Bahasa Malaysia course for international
students with little or no prior Malay, covering listening, speaking,
reading and writing from the ground up through everyday, practical themes.

Malay Enrichment Y8 meets 2x/week (Mon 75min, Tue 35min). Each week below is
ONE shared theme, delivered as a 2-day arc:
  Mon "teach"    -- introduce new vocabulary/phrases across all 4 skills
  Tue "practise" -- a shorter, game-based consolidation and speaking session

build_malay_y8.py turns each week into 2 separate Lesson dicts (Mon/Tue), so
each session is independently plannable and markable Done.
"""

# --- Term 1: Everyday survival Malay (15 weeks incl. meta; 8 content weeks) ---
TERM1 = [
    {
        "topic": "Greetings and Introducing Yourself",
        "subtopic": "Salam dan Memperkenalkan Diri",
        "objectives": [
            "Listen to and understand common greetings (Selamat pagi/tengah hari/petang, Apa khabar?).",
            "Say a greeting and introduce themselves: name, where they're from.",
            "Read simple greeting phrases aloud with correct pronunciation.",
            "Write a short self-introduction of 2-3 sentences.",
        ],
        "resources": ["Greeting flashcards", "A simple 'Nama saya...' sentence frame", "Audio clips of native greetings, if available"],
    },
    {
        "topic": "Numbers 1-20",
        "subtopic": "Nombor 1 hingga 20",
        "objectives": [
            "Listen to and recognise spoken numbers 1-20.",
            "Count aloud from 1 to 20 with correct pronunciation.",
            "Read numerals and their Malay words side by side.",
            "Write numbers 1-20 in Malay from dictation.",
        ],
        "resources": ["Number cards 1-20 (numeral and word)", "Dice or counters for a counting game", "Mini-whiteboards"],
    },
    {
        "topic": "Family Members",
        "subtopic": "Ahli Keluarga",
        "objectives": [
            "Listen to a short description of someone's family and identify who's who.",
            "Say the Malay words for immediate family members (ibu, bapa, adik, abang, kakak).",
            "Read a simple family tree labelled in Malay.",
            "Write 2-3 sentences describing their own family.",
        ],
        "resources": ["Family tree template", "Family member flashcards", "A model family-description paragraph"],
    },
    {
        "topic": "Colours and Basic Descriptions",
        "subtopic": "Warna dan Penerangan Ringkas",
        "objectives": [
            "Listen to a description of an object and identify its colour.",
            "Say the Malay names for common colours.",
            "Read a short sentence describing an object's colour and size.",
            "Write a simple sentence using a colour word (e.g. Bola itu merah).",
        ],
        "resources": ["Colour flashcards/objects", "Classroom items for a 'point and say' game", "Mini-whiteboards"],
    },
    {
        "topic": "Days, Months and Time",
        "subtopic": "Hari, Bulan dan Masa",
        "objectives": [
            "Listen to and identify a day of the week or month being said.",
            "Say the days of the week and months of the year in order.",
            "Read a simple weekly timetable written in Malay.",
            "Write today's day and date in Malay.",
        ],
        "resources": ["Days/months flashcards", "A blank weekly timetable template", "A classroom calendar"],
    },
    {
        "topic": "Classroom Language and School Items",
        "subtopic": "Bahasa Bilik Darjah dan Alatan Sekolah",
        "objectives": [
            "Listen to and follow simple classroom instructions (duduk, berdiri, buka buku).",
            "Say the Malay names for common school items (buku, pensel, beg sekolah).",
            "Read a short list of classroom instructions.",
            "Write a short list of items in their school bag, in Malay.",
        ],
        "resources": ["School item flashcards/realia", "Classroom instruction cards", "Mini-whiteboards"],
    },
    {
        "topic": "Food and Drinks",
        "subtopic": "Makanan dan Minuman",
        "objectives": [
            "Listen to someone ordering food and identify what they asked for.",
            "Say the Malay names for common foods and drinks, and 'Saya nak...' (I want...).",
            "Read a simple menu written in Malay.",
            "Write a short shopping/order list in Malay.",
        ],
        "resources": ["Food/drink flashcards", "A simple mock menu", "Play money (optional, for a role-play)"],
    },
    {
        "topic": "Asking and Giving Simple Directions",
        "subtopic": "Bertanya dan Memberi Arah",
        "objectives": [
            "Listen to simple directions and follow them on a map.",
            "Say key direction phrases (kiri, kanan, lurus, belok).",
            "Read a simple map with Malay direction labels.",
            "Write directions from one point to another on a simple map.",
        ],
        "resources": ["A simple classroom/school map", "Direction word cards", "Mini-whiteboards"],
    },
    {
        "topic": "Consolidation",
        "subtopic": "Ulangkaji Kemahiran Term Ini",
        "objectives": [
            "Revisit greetings, numbers, family and colours vocabulary.",
            "Revisit days, months, classroom language and food vocabulary.",
            "Practise all four skills (listening, speaking, reading, writing) together.",
        ],
        "resources": ["All Term 1 flashcards", "Mixed-skills activity stations", "Mini-whiteboards"],
    },
    {
        "topic": "Revision",
        "subtopic": "Bersedia untuk Ujian Lisan dan Bertulis",
        "objectives": [
            "Identify which Term 1 skills feel secure and which need more practice.",
            "Practise the type of task expected in the oral and written check.",
            "Ask for help on anything still unclear before the check.",
        ],
        "resources": ["Practice task cards", "Mini-whiteboards", "Term 1 skills checklist (self-tick)"],
    },
    {
        "topic": "Examination Week",
        "subtopic": "Penilaian Lisan dan Bertulis Term 1",
        "objectives": [
            "Show listening and speaking skills through a short paired conversation.",
            "Show reading and writing skills through a short written task.",
            "Use vocabulary from this term's themes accurately.",
        ],
        "resources": ["Assessment task cards", "Paired-conversation prompt cards", "Mini-whiteboards"],
    },
    {
        "topic": "End of Term Project — My Malay Phrasebook",
        "subtopic": "Plan and Choose 10 Useful Phrases",
        "objectives": [
            "Choose 10 phrases from this term that they find most useful.",
            "Sort them into categories (greetings, food, directions...).",
            "Plan how to illustrate or explain each phrase.",
        ],
        "resources": ["Blank phrasebook template", "This term's flashcards for reference", "Coloured pens/pencils"],
    },
    {
        "topic": "End of Term Project — My Malay Phrasebook",
        "subtopic": "Build the Phrasebook Pages",
        "objectives": [
            "Write each phrase clearly with its English meaning.",
            "Illustrate or find an image for each phrase.",
            "Check spelling and pronunciation notes with a partner.",
        ],
        "resources": ["Phrasebook pages in progress", "Coloured pens/pencils", "Dictionaries/word lists"],
    },
    {
        "topic": "End of Term Project — My Malay Phrasebook",
        "subtopic": "Finish and Practise Reading It Aloud",
        "objectives": [
            "Complete and decorate every page of the phrasebook.",
            "Practise reading 5 phrases aloud with confidence.",
            "Say one phrase they are proud of learning.",
        ],
        "resources": ["Completed phrasebook pages", "Stapler or binder", "A quiet reading corner"],
    },
    {
        "topic": "Portfolio Showcase — Share My Phrasebook",
        "subtopic": "Pembentangan Buku Frasa Saya",
        "objectives": [
            "Present their phrasebook and read 3-5 phrases aloud to a partner or small group.",
            "Listen to a classmate's phrasebook and try out one of their phrases.",
            "Reflect on what they learned about Malay this term.",
        ],
        "resources": ["Finished phrasebooks", "Simple 'kind comment' sentence starters", "Certificates (optional)"],
    },
]

# --- Term 2: Daily life & description (11 weeks incl. meta; 8 content weeks) ---
TERM2 = [
    {
        "topic": "Body Parts and Feelings",
        "subtopic": "Anggota Badan dan Perasaan",
        "objectives": [
            "Listen to a description of how someone feels or what hurts.",
            "Say the Malay words for body parts and feelings (gembira, sedih, letih).",
            "Read a short dialogue about feeling unwell.",
            "Write a sentence describing how they feel today.",
        ],
        "resources": ["Body part diagram/flashcards", "Feelings flashcards", "A simple 'Saya rasa...' sentence frame"],
    },
    {
        "topic": "Weather and Seasons",
        "subtopic": "Cuaca dan Musim",
        "objectives": [
            "Listen to a weather report and identify the weather described.",
            "Say common weather words (panas, hujan, berangin).",
            "Read a simple weather forecast written in Malay.",
            "Write a sentence describing today's weather.",
        ],
        "resources": ["Weather flashcards", "A mock weather-forecast template", "Mini-whiteboards"],
    },
    {
        "topic": "Shopping and Money",
        "subtopic": "Membeli-belah dan Wang",
        "objectives": [
            "Listen to a shop conversation and identify what was bought and its price.",
            "Say prices in Ringgit and ask 'Berapa harga ini?' (How much is this?).",
            "Read simple price tags and a mock receipt.",
            "Write a short shopping dialogue with a partner.",
        ],
        "resources": ["Play money (Ringgit)", "Mock price-tag cards", "A simple shop role-play set-up"],
    },
    {
        "topic": "Hobbies and Free Time",
        "subtopic": "Hobi dan Masa Lapang",
        "objectives": [
            "Listen to someone describing their hobby and identify it.",
            "Say what hobby they enjoy: 'Saya suka...' (I like...).",
            "Read short hobby descriptions and match them to pictures.",
            "Write 2-3 sentences about their own hobbies.",
        ],
        "resources": ["Hobby flashcards/pictures", "A 'Saya suka...' sentence frame", "Mini-whiteboards"],
    },
    {
        "topic": "Describing People and Things",
        "subtopic": "Menerangkan Orang dan Benda",
        "objectives": [
            "Listen to a description of a person or object and identify them from a group.",
            "Say simple descriptive sentences using adjectives (tinggi, kecil, cantik).",
            "Read a short paragraph describing a person.",
            "Write a short description of a classmate or a favourite object.",
        ],
        "resources": ["Adjective flashcards", "Pictures of people/objects to describe", "Mini-whiteboards"],
    },
    {
        "topic": "Daily Routines",
        "subtopic": "Rutin Harian",
        "objectives": [
            "Listen to someone describing their daily routine and put the events in order.",
            "Say what time they do daily activities: 'Saya bangun pada pukul...' (I wake up at...).",
            "Read a simple daily-routine timetable.",
            "Write 3-4 sentences describing their own daily routine.",
        ],
        "resources": ["Daily-routine picture cards", "A blank routine timetable template", "Mini-whiteboards"],
    },
    {
        "topic": "Places in Town",
        "subtopic": "Tempat di Bandar",
        "objectives": [
            "Listen to someone say where they are going and identify the place.",
            "Say the names of common places in town (sekolah, kedai, hospital, taman).",
            "Read simple signs and building labels in Malay.",
            "Write a sentence saying where they went and why.",
        ],
        "resources": ["Place flashcards", "A simple town map", "Mini-whiteboards"],
    },
    {
        "topic": "Talking About Yesterday",
        "subtopic": "Bercakap Tentang Semalam (Kata Kerja Lampau)",
        "objectives": [
            "Listen to someone describe what they did yesterday and identify the activities.",
            "Say 1-2 things they did yesterday using simple past-time markers (semalam, tadi).",
            "Read a short diary-style paragraph about yesterday.",
            "Write 2-3 sentences about what they did yesterday.",
        ],
        "resources": ["Activity picture cards", "A simple diary-entry template", "Mini-whiteboards"],
    },
    {
        "topic": "Consolidation",
        "subtopic": "Ulangkaji Kemahiran Term Ini",
        "objectives": [
            "Revisit feelings, weather, shopping and hobbies vocabulary.",
            "Revisit descriptions, daily routines and places in town.",
            "Practise all four skills together, focusing on speaking confidence.",
        ],
        "resources": ["All Term 2 flashcards", "Mixed-skills activity stations", "Mini-whiteboards"],
    },
    {
        "topic": "Revision",
        "subtopic": "Bersedia untuk Ujian Lisan dan Bertulis",
        "objectives": [
            "Identify which Term 2 skills feel secure and which need more practice.",
            "Practise the type of task expected in the oral and written check.",
            "Ask for help on anything still unclear before the check.",
        ],
        "resources": ["Practice task cards", "Mini-whiteboards", "Term 2 skills checklist (self-tick)"],
    },
    {
        "topic": "Examination Week",
        "subtopic": "Penilaian Lisan dan Bertulis Term 2",
        "objectives": [
            "Show speaking skills through a short role-play (shopping or ordering food).",
            "Show reading and writing skills through a short written task.",
            "Use vocabulary from this term's themes accurately.",
        ],
        "resources": ["Assessment task cards", "Role-play prompt cards", "Mini-whiteboards"],
    },
]

# --- Term 3: Culture, community & looking ahead (15 weeks incl. meta; 8 content weeks) ---
TERM3 = [
    {
        "topic": "Malaysian Festivals and Culture",
        "subtopic": "Perayaan dan Budaya Malaysia",
        "objectives": [
            "Listen to a short description of a Malaysian festival and identify which one.",
            "Say the names of major Malaysian festivals and one custom for each.",
            "Read a short passage about a festival celebration.",
            "Write 2-3 sentences about a festival they find interesting.",
        ],
        "resources": ["Festival picture cards", "Short festival reading passages", "Mini-whiteboards"],
    },
    {
        "topic": "Animals and Nature",
        "subtopic": "Haiwan dan Alam Semula Jadi",
        "objectives": [
            "Listen to animal names and match them to pictures.",
            "Say the Malay names for common animals, including some unique to Malaysia.",
            "Read a short fact-file about a Malaysian animal (e.g. orang utan).",
            "Write 2-3 sentences describing a favourite animal.",
        ],
        "resources": ["Animal flashcards (including Malaysian wildlife)", "A short animal fact-file template", "Mini-whiteboards"],
    },
    {
        "topic": "Transport and Travel",
        "subtopic": "Pengangkutan dan Perjalanan",
        "objectives": [
            "Listen to travel plans and identify the transport being used.",
            "Say the Malay names for transport (bas, kereta, tren, kapal terbang).",
            "Read a simple travel itinerary written in Malay.",
            "Write a sentence about how they travel to school.",
        ],
        "resources": ["Transport flashcards", "A mock travel-itinerary template", "Mini-whiteboards"],
    },
    {
        "topic": "Talking About Tomorrow",
        "subtopic": "Bercakap Tentang Esok (Kata Kerja Masa Depan)",
        "objectives": [
            "Listen to someone's plans and identify what they will do.",
            "Say 1-2 plans using simple future-time markers (esok, akan).",
            "Read a short paragraph about someone's weekend plans.",
            "Write 2-3 sentences about their own plans for tomorrow or the weekend.",
        ],
        "resources": ["Plan/activity picture cards", "A simple planner template", "Mini-whiteboards"],
    },
    {
        "topic": "Health and Going to the Doctor",
        "subtopic": "Kesihatan dan Ke Klinik",
        "objectives": [
            "Listen to a short clinic conversation and identify the problem.",
            "Say how they feel and ask for help: 'Saya sakit...' (I am sick with...).",
            "Read a simple clinic sign-in form.",
            "Write a short note explaining they feel unwell.",
        ],
        "resources": ["Illness/symptom flashcards", "A mock clinic form", "Mini-whiteboards"],
    },
    {
        "topic": "Phone Calls and Making Plans",
        "subtopic": "Panggilan Telefon dan Membuat Rancangan",
        "objectives": [
            "Listen to a short phone call and identify the plan being made.",
            "Say a simple phone greeting and make a suggestion: 'Jom kita...' (Let's...).",
            "Read a short text-message style conversation.",
            "Write a short message inviting a friend to do something.",
        ],
        "resources": ["Phone-call dialogue cards", "Mock phone/message templates", "Mini-whiteboards"],
    },
    {
        "topic": "Malaysian Food Culture Deep-Dive",
        "subtopic": "Budaya Makanan Malaysia",
        "objectives": [
            "Listen to a description of a Malaysian dish and identify it.",
            "Say the names of well-known Malaysian dishes and one thing about each.",
            "Read a simple recipe or food-stall menu.",
            "Write 2-3 sentences recommending a dish to a friend.",
        ],
        "resources": ["Malaysian food picture cards", "A simple recipe/menu extract", "Mini-whiteboards"],
    },
    {
        "topic": "Presenting About Myself and My Country",
        "subtopic": "Membentangkan Diri dan Negara Saya",
        "objectives": [
            "Listen to a short self/country introduction and note key facts.",
            "Say a short introduction covering name, country and one fact about home.",
            "Read their own draft introduction aloud with growing confidence.",
            "Write a short paragraph introducing themselves and their home country.",
        ],
        "resources": ["A self-introduction sentence-frame", "World map (optional)", "Mini-whiteboards"],
    },
    {
        "topic": "Consolidation",
        "subtopic": "Ulangkaji Kemahiran Sepanjang Tahun",
        "objectives": [
            "Revisit vocabulary and phrases from across the whole year.",
            "Choose an area they want more practice in and work on it.",
            "Help a partner with a phrase or skill they find secure.",
        ],
        "resources": ["A full year's flashcards", "Mixed-skills activity stations", "Mini-whiteboards"],
    },
    {
        "topic": "Revision",
        "subtopic": "Bersedia untuk Ujian Lisan dan Bertulis",
        "objectives": [
            "Identify which whole-year skills feel secure and which need more practice.",
            "Practise the type of task expected in the oral and written check.",
            "Ask for help on anything still unclear before the check.",
        ],
        "resources": ["Practice task cards", "Mini-whiteboards", "Whole-year skills checklist (self-tick)"],
    },
    {
        "topic": "Examination Week",
        "subtopic": "Penilaian Lisan dan Bertulis Term 3",
        "objectives": [
            "Show a short prepared self-introduction, spoken aloud.",
            "Show reading and writing skills through a short written task.",
            "Use vocabulary from across the year accurately.",
        ],
        "resources": ["Assessment task cards", "Self-introduction prompt cards", "Mini-whiteboards"],
    },
    {
        "topic": "End of Term Project — Malaysian Culture Presentation",
        "subtopic": "Plan and Choose a Topic",
        "objectives": [
            "Choose one aspect of Malaysian culture to research (festival, food, place or custom).",
            "Plan the key Malay phrases and facts they want to include.",
            "Sketch out what their presentation will look like.",
        ],
        "resources": ["Planning sheet", "This year's flashcards/notes for reference", "Coloured pens/pencils"],
    },
    {
        "topic": "End of Term Project — Malaysian Culture Presentation",
        "subtopic": "Build the Presentation",
        "objectives": [
            "Prepare a poster, slideshow or short script for their presentation.",
            "Include at least 5 Malay words or phrases with their meanings.",
            "Practise saying the Malay parts aloud with a partner.",
        ],
        "resources": ["Presentation materials (card, or a shared device)", "This year's flashcards/notes", "Feedback sentence starters"],
    },
    {
        "topic": "End of Term Project — Malaysian Culture Presentation",
        "subtopic": "Rehearse Presenting It",
        "objectives": [
            "Rehearse presenting clearly and at a good pace.",
            "Practise answering a simple question about their topic in Malay or English.",
            "Give a partner one tip to make their presentation clearer.",
        ],
        "resources": ["Finished presentation materials", "Rehearsal partner", "Feedback sentence starters"],
    },
    {
        "topic": "Portfolio Showcase — Malaysian Culture Fair",
        "subtopic": "Hari Pameran Budaya Malaysia",
        "objectives": [
            "Present their Malaysian culture topic to the class or visitors.",
            "Listen to a classmate's presentation and ask one question.",
            "Reflect on their favourite thing they learned about Malay this year.",
        ],
        "resources": ["All finished presentations", "Simple question sentence starters", "Certificates (optional)"],
    },
]

TERMS = {"term-1": TERM1, "term-2": TERM2, "term-3": TERM3}
