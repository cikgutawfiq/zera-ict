# Zera ICT — Lesson Dashboard

One place to plan and deliver every lesson: the Scheme of Work, mapped onto the actual
teacher timetable, with a full lesson plan on each card — opened on a phone, minutes before
the bell.

Built for **Mr Tawfiq bin Rahmat** (Zera International School, 2026/2027). Private to a single
Google account; embedded as an iframe on `cikgutawfiq.com/zera-ict`.

## What's in it

| Screen | What it does |
| --- | --- |
| `/` **Today** | The classes you teach today, in period order with times. Deep link a date with `/?date=2026-09-22`. |
| `/lesson/[id]` | Value of the Day (moral value, quote, food-for-thought), a 5–10 min Ice Breaker (with a 🎲 Randomize button), side-by-side topic/subtopic, an equipment chip (✏️ Unplugged / 👥 Shared laptops / 💻 1 device each), a **"Not feeling this topic?"** panel with 3 level-appropriate alternative topic ideas (🔀 reroll, or swap one straight in), objectives, a per-step lesson plan (instructions / what students do / how to assess), activities, success criteria, resources, a **Worksheets & assessment** section (printable PDFs, see below) and a Reflection box. Every field is editable in place. Mark **Done** / **Carried over** — a carried-over lesson automatically takes over that class's *next* scheduled slot (flagged with a "Carried over from Week N" banner) instead of quietly falling behind the calendar; it stays there until marked Done. |
| `/lesson/[id]/present` | Full-screen presentation mode: big type, arrow keys or buttons, screen wake-lock on. Opens on the Value of the Day, then the Ice Breaker, then the lesson plan. |
| `/calendar` **This week** | The five weekdays, each with its own column on desktop (a real week board) and stacked on mobile. |
| `/classes`, `/class/[id]` | Every class; each term is its own collapsible section (the current term opens by default), with **+ Week** to add more. |
| `/overview` | Pick a year/class and see every week's topic for the *whole year* (all 3 terms) as one top-down table — Term / Week / Topic / "what students will learn" / **Lesson detail** (a fuller, genuinely week-specific description of what actually happens). **Click any row** to jump straight into that week's full lesson plan — going **Back** returns to this same class, not the default. **📥 Save (PDF)** exports that one class as a single landscape page; **📚 Export Y1–Y9 pack (PDF)** builds a 9-page pack, one page per ICT class, in one file. End-of-term project weeks show the actual project name right in the Topic column (e.g. "End of Term Project — Build My Own Webpage"), so what students are building is visible at a glance, not hidden behind a generic label. |
| `/admin` | Upload the two SOW workbooks to re-sync Term 1 from your phone, seed / re-sync from the bundled SOW, add or remove terms and weeks (each term is an accordion — collapsed by default, only one open at a time), an **ICT module & project plan** table (every module, its term/week, its live tool link, and its KS1/KS2/KS3 project side by side), sign out. |

## Look and feel

Corporate light blue / grey, Outlook-and-SharePoint-adjacent — see the tokens at the top of
`src/app/globals.css`. On screens ≥1024px a fixed dark-navy sidebar replaces the mobile bottom
tab bar, and pages widen and grid-ify to use the space (Classes becomes a 2–3 column grid, the
lesson page splits into a content column plus a sticky status/Value-of-the-Day/Ice-Breaker rail).
Below 1024px everything collapses back to the single-column, bottom-tab mobile layout.

## Data

- **Seeded**: 369 ICT lessons (Y1–Y9, all three terms, see "ICT curriculum" below), 123
  **Maths Y1** sessions (see "Maths Y1" below), and 82 **Malay Enrichment Y8** sessions (see
  "Malay Enrichment Y8" below).
- **Projects**: every class (all 9 ICT classes, Maths Y1, Malay Enrichment Y8) has at least one
  named, concrete End-of-Term Project — not a generic "the project" placeholder. ICT classes get
  two (Term 1: a low-tech campaign/report tied to that term's unplugged weeks; Term 3: a
  flagship build using that term's unit skills, e.g. Y3 "Stop-Frame Animation Short Film", Y6
  "Build My Own Webpage", Y9 "Data Science Investigation"). Project names are defined in
  `scripts/ict_content.py`'s `PROJECTS` dict and show directly in the Overview's Topic column.
- **Equipment mode**: every lesson optionally carries `equipmentMode` —
  `unplugged` / `shared-laptops` / `1-1-devices` — shown as a chip on the lesson card and
  lesson page. Every class opens its year with 8 low/no-device weeks (Term 1, weeks 1-8),
  since laptop access may be limited (as few as 4 shared machines, in rotating groups) for the
  first couple of months of term. Content and plan wording for those weeks is genuinely
  device-free (paper, discussion, movement), not just relabelled.
- **ICT curriculum (Y1-Y9)**: every ICT class follows the **same 16 modules**, one per week —
  Google Interland, Typing Club, Microsoft Word, Google Docs, Microsoft Excel, Google Sheets,
  Canva Design, Google Forms, Microsoft PowerPoint, Google Slides, Google Sites, Artificial
  Intelligence, Data and Information, Safety and Security, Design and Development, and Creating
  Media — instead of a different topic list per year. Content, vocabulary and each module's
  **project** (see below) scale up by key stage (KS1/KS2/KS3) rather than swapping the topic out,
  so the whole school shares one consistent map of "what ICT covers." Every module links straight
  to the real tool (canva.com, typingclub.com, the Microsoft 365 / Google Workspace app pages,
  Interland) via the lesson's Resources section; the 5 non-tool modules link to Oak National
  Academy's matching Computing (Secondary Core) thread page instead (e.g.
  `?threads=artificial-intelligence`). Modules land in Term 2 (1-8) and Term 3 (9-16), after
  each class's 8 low/no-device settling-in weeks in Term 1. Source: `scripts/ict_content.py`
  (the `MODULES` table — name, tool link, and KS1/KS2/KS3 subtopic+objectives+project for each)
  and `scripts/build_ict.py` (the equipment-mode-aware lesson-plan generator). The original SOW
  workbooks and their derived files (`sow.raw.json`, `authored/`) still exist for the `/admin`
  re-upload path and historical reference, but no longer feed the seed.
- **Module & project plan (Admin)**: `/admin` has an **ICT module & project plan** table — every
  module, which term/week it falls in, its live tool/reference link, and its project at each key
  stage, all in one place so the whole year's "what will they make" plan is visible without
  clicking into 200+ individual lessons. Generated from `ict_content.py`'s `module_plan_table()`
  into `src/data/modulePlan.json` by `build_seed.py`.
- **Maths Y1**: aligned to **Oak National Academy's Year 1 Maths units**
  (thenational.academy/teachers/programmes/maths-primary/units) — the 18 real unit titles, each
  allocated roughly 1-2 of our weeks in proportion to its Oak lesson count, so all 18 fit
  exactly into the 24 content weeks across the year (**Term 1**: units 1-5, counting/comparing/
  shape; **Term 2**: units 6-11a, composition of numbers, addition/subtraction facts; **Term
  3**: units 11b-18, composition 11-19, coins, position, time). All 3 terms close with the same
  consolidation / revision / examination week / end-of-term project / portfolio showcase rhythm
  used for the ICT classes. Maths Y1 meets 3x/week (Tue/Thu/Fri), so each week's topic becomes 3
  independently-plannable sessions — Tue *explore*, Thu *practise*, Fri *consolidate* — each
  with its own lesson doc, its own editable content, and its own Done status (see "Multi-session
  classes" below — this is also where the Thu/Fri "marking one marks both" bug was fixed). See
  `scripts/maths_y1_content.py` (the 18 units, redistributed into 41 weeks) and
  `scripts/build_maths_y1.py` (the day-variant lesson-plan generator).
- **Malay Enrichment Y8**: a beginner Bahasa Malaysia course for international students with
  little or no prior Malay — 24 themed weeks (greetings, numbers, family, food, directions,
  shopping, weather, culture, festivals...) covering listening, speaking, reading and writing
  every week, in the same consolidation/revision/exam/project/showcase rhythm as the other
  classes. Malay Enrichment Y8 meets 2x/week (Mon 75min, Tue 35min), so each week is a 2-day
  arc — Mon *teach* (new vocabulary across all 4 skills), Tue *practise* (a shorter game-based
  consolidation and speaking session) — each an independently editable, independently
  gradeable session. See `scripts/malay_y8_content.py` (the 24 themes) and
  `scripts/build_malay_y8.py` (the day-variant lesson-plan generator).
- **Moral value / quote / food-for-thought**: every lesson gets one, assigned deterministically
  per class from a 41-entry pool so nothing repeats across a class's full year (see
  `src/data/values.ts`).
- **Ice breaker**: every lesson gets one 5–10 minute opener, age-banded by key stage (KS1/KS2/KS3
  pools, ~33 entries each, 99 games total). Hit **🎲 Randomize** on the lesson page to reroll from
  the same-key-stage pool.
- **Lesson plan steps**: each timed step optionally carries three parts — instructions (what you
  say/set up), what students do, and how to assess. New/edited steps can fill in all three; older
  steps keep just their instructions until you flesh them out. Not every one of the 369 lessons
  has been backfilled with the fuller three-part detail yet — the structure and editor are ready,
  filling them in is an ongoing pass.
- **Re-uploading Term 1**: `/admin` has file pickers for both workbooks — parsing happens in the
  browser (`read-excel-file`, no server, no Python needed) and feeds the same seed/re-sync flow.
- **Worksheets & rubric**: every lesson page has a **📄 3 worksheets** button that generates a
  three-page PDF (Foundation / Core / Challenge) client-side, using that lesson's own topic,
  subtopic, objectives, activities and success criteria as the source text — no two lessons
  produce the same worksheet. Each page opens with a "How to run this" delivery note (grouping,
  timing, how much support to expect) and mixes question types instead of a flat Q&A list — a
  word-scramble puzzle, a "Beat the clock" timed round, a self-assessment check-in, and, on the
  Challenge sheet, a boxed bonus/extension task. A separate **📊 Assessment rubric** button
  generates a 4-point scale (Superstar / Solid / Growing / Just Starting) built from the lesson's
  success criteria, with a usage note and grade-band legend, so a cover teacher or a student can
  see exactly how each criterion is graded. Both are generated entirely in the browser with
  `jspdf`/`jspdf-autotable` — nothing is stored or pre-rendered, so they always reflect the
  lesson's current (possibly edited) content. See `src/lib/worksheets.ts`.

Regenerate the seed after editing the curriculum content or the term calendars:

```bash
python scripts/extract_sow.py && python scripts/build_terms23.py && python scripts/build_seed.py
```

`scripts/extract_sow.py` reads the two original SOW workbooks from `~/Downloads` (override with
`SOW_DIR`) — only the term dates/weeks are still used from it (`src/data/sow.raw.json`).
`scripts/build_terms23.py` generates the Term 2/3 week calendars into `src/data/terms23.json`.
`scripts/build_seed.py` merges those calendars with `scripts/build_ict.py`'s ICT lessons,
`scripts/build_maths_y1.py`'s Maths Y1 sessions and `scripts/build_malay_y8.py`'s Malay
Enrichment Y8 sessions, assigns moral values/quotes/ice breakers, and writes
`src/data/seed.json`, which `/admin` writes to Firestore in batches. Existing lessons you have
edited are skipped unless you tick **Overwrite**.

### Multi-session classes

Maths Y1 (3x/week) and Malay Enrichment Y8 (2x/week) each get one lesson **per session**
instead of one shared lesson for the whole week — id `{classId}_{termId}_w{weekNo}_d{day}`
(`day` is 1=Mon..5=Fri, matching `Slot.day` in `timetable.ts`), with `weekLabel` like
`"Week 1 (Tue)"` to tell sessions apart. `lessonFor(classId, dateISO)` in `src/lib/store.tsx`
matches on both the week range and the weekday, so each session is independently plannable and
markable Done — marking Tuesday's session Done no longer marks Thursday's or Friday's Done too.
Classes with a single weekly session (all 9 ICT classes) keep the older
`{classId}_{termId}_w{weekNo}` id with no `day` field, unaffected. `/class/[classId]`'s
**+ Week** button detects a class's session count from `slotsForClass()` and creates one lesson
per session automatically.

If your live Firestore still has old pre-migration docs (one lesson shared across a whole
week, no `day` field), `lessonFor` now always prefers an exact weekday match over a day-less
lesson, so the old docs can no longer shadow the new per-session ones — but they'll still sit
there unused. Hit **Seed / re-sync** in `/admin` once to have `seed()` clean them up (it deletes
any Maths Y1 / Malay Enrichment Y8 doc with no `day` field, same edit-protection rules as
everything else it writes).

The moral value / quote / ice breaker bank lives in `src/data/values.ts` (TypeScript, used by
the app and the browser upload path) with a Python mirror in `scripts/values.py` (used by
`build_seed.py`) — edit both together.

## Firestore

Collections: `lessons` (flat, id `{classId}_{termId}_w{weekNo}`, or `..._d{day}` for
multi-session classes — see "Multi-session classes" above) and `terms`.
Access is locked to one verified Google account in `firestore.rules` — publish it with:

```bash
firebase deploy --only firestore:rules
```

## Timetable

`src/data/timetable.ts` holds the period grid, the 11 classes and all 16 timetable slots
(27 taught periods + Assembly and PE Support duties), transcribed from the printed
timetable dated 26.8.2026 v2. Edit that file when the timetable changes.

## Local development

```bash
npm install
npm run dev
```

Sign-in is required by default. For UI work without touching Firestore, create
`.env.development.local` with `NEXT_PUBLIC_DEV_PREVIEW=1` — the app then renders from
`src/data/seed.json` with no auth. This is hard-gated on `NODE_ENV` and can never activate
in a production build.

## Deployment

Vercel, from the `main` branch. Firebase's web config is public by design and is baked into
`src/lib/firebase.ts`; the `NEXT_PUBLIC_*` variables in `.env.local.example` can override it.

Manual steps in the Firebase console:

1. **Authentication → Sign-in method** → enable **Google**.
2. **Authentication → Settings → Authorized domains** → add the Vercel domain and
   `cikgutawfiq.com`.
3. **Firestore Database** → create the database, then publish `firestore.rules`.

Embedding uses `Content-Security-Policy: frame-ancestors` in `next.config.ts` — add any new
host there before iframing from it. Sign-in uses `signInWithPopup`, because the redirect flow
does not work inside a cross-origin iframe.
