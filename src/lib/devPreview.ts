/**
 * Dev-only offline preview.
 *
 * With `NEXT_PUBLIC_DEV_PREVIEW=1` in a local `next dev` run, the app renders
 * from src/data/seed.json with no sign-in and no Firestore. It is hard-gated on
 * NODE_ENV so a production build can never enable it, whatever the env var says.
 */
export const DEV_PREVIEW =
  process.env.NODE_ENV === "development" && process.env.NEXT_PUBLIC_DEV_PREVIEW === "1";
