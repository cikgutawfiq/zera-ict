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
| `/lesson/[id]` | Objectives, timed lesson plan, activities, success criteria, resources, plus the original SOW text. Every field is editable in place. Mark **Done** / **Carried over** and leave an after-the-lesson note. |
| `/lesson/[id]/present` | Full-screen presentation mode: big type, arrow keys or buttons, screen wake-lock on. |
| `/week` | All 27 periods, Monday to Friday, with week navigation. |
| `/classes`, `/class/[id]` | Every class, its weeks, and **+ Week** to add more. |
| `/admin` | Seed / re-sync from the SOW, add or remove terms and weeks, sign out. |

## Data

- **Source**: `SOW_ICT_KS1_KS2_Y1-6_2026-2027.xlsx` and `SOW_ICT_KS3_Y7-9_2026-2027.xlsx`
  (Term 1: Weeks 1–15, 26 Aug – 11 Dec 2026, plus a mid-term break and Examination Week).
- **Seeded**: 135 ICT lessons (Y1–Y9) with authored objectives / plan / activities /
  success criteria, plus 30 blank week rows for **Maths Y1** and **Malay Enrichment Y8**,
  which have no scheme of work yet.
- **Terms 2 and 3**: add them yourself in `/admin` → **+ Term**, then **+ Week**; add the
  lessons from each class page.

Regenerate the seed after editing the workbooks or the authored content:

```bash
python scripts/extract_sow.py && python scripts/build_seed.py
```

`scripts/extract_sow.py` reads the two workbooks from `~/Downloads` (override with `SOW_DIR`)
and writes `src/data/sow.raw.json`. `scripts/build_seed.py` merges that with
`src/data/authored/y1.json … y9.json` into `src/data/seed.json`, which `/admin` writes to
Firestore in batches. Existing lessons you have edited are skipped unless you tick
**Overwrite**.

## Firestore

Collections: `lessons` (flat, id `{classId}_{termId}_w{weekNo}`) and `terms`.
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
