"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useAuth } from "@/lib/auth";
import { OWNER_EMAIL } from "@/lib/firebase";
import { DEV_PREVIEW } from "@/lib/devPreview";

const TABS = [
  { href: "/", label: "Today", icon: "●" },
  { href: "/week", label: "Week", icon: "▦" },
  { href: "/classes", label: "Classes", icon: "▤" },
  { href: "/admin", label: "Admin", icon: "⚙" },
];

export default function Shell({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const { user, loading, isOwner, error, signIn, signOut } = useAuth();

  // Presentation mode takes over the whole viewport — no chrome.
  if (pathname?.endsWith("/present")) return <>{children}</>;

  if (!DEV_PREVIEW && loading) {
    return (
      <main className="min-h-[60vh] grid place-items-center p-6">
        <p className="text-[color:var(--muted)] text-sm">Loading…</p>
      </main>
    );
  }

  if (!DEV_PREVIEW && !isOwner) {
    return (
      <main className="min-h-[70vh] grid place-items-center p-6">
        <div className="card w-full max-w-sm p-6 text-center">
          <h1 className="text-lg font-bold">ZERA ICT GUY :)</h1>
          <p className="mt-2 text-sm text-[color:var(--muted)]">
            {user
              ? `Signed in as ${user.email}. This dashboard is private to ${OWNER_EMAIL}.`
              : "Sign in with your school Google account to see your timetable and lessons."}
          </p>
          {error && <p className="mt-3 text-sm text-[color:var(--warn)]">{error}</p>}
          <div className="mt-5 flex flex-col gap-2">
            {user ? (
              <button className="btn" onClick={signOut}>
                Sign out
              </button>
            ) : (
              <button className="btn btn-primary" onClick={signIn}>
                Sign in with Google
              </button>
            )}
          </div>
        </div>
      </main>
    );
  }

  return (
    <div className="min-h-screen pb-20">
      <div className="blur-bar no-print flex items-center justify-center gap-1.5 border-b border-[color:var(--border)] py-1.5 text-[11px] font-semibold tracking-wide text-[color:var(--muted)]">
        <span aria-hidden>✦</span> ZERA ICT GUY :)
      </div>
      {children}
      <nav className="blur-bar no-print fixed bottom-0 inset-x-0 border-t border-[color:var(--border)] pb-[env(safe-area-inset-bottom)]">
        <ul className="mx-auto flex max-w-3xl px-2 py-1.5">
          {TABS.map((tab) => {
            const active = tab.href === "/" ? pathname === "/" : pathname?.startsWith(tab.href);
            return (
              <li key={tab.href} className="flex-1">
                <Link
                  href={tab.href}
                  className="flex flex-col items-center gap-0.5 rounded-xl py-2 text-[11px] font-semibold transition-colors"
                  style={{
                    color: active ? "var(--accent)" : "var(--muted)",
                    background: active ? "var(--accent-soft)" : "transparent",
                    transitionDuration: "var(--dur-fast)",
                    transitionTimingFunction: "var(--ease)",
                  }}
                >
                  <span aria-hidden className="text-base leading-none">
                    {tab.icon}
                  </span>
                  {tab.label}
                </Link>
              </li>
            );
          })}
        </ul>
      </nav>
    </div>
  );
}
