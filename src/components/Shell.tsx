"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useAuth } from "@/lib/auth";
import { OWNER_EMAIL } from "@/lib/firebase";
import { DEV_PREVIEW } from "@/lib/devPreview";

const TABS = [
  { href: "/", label: "Today", icon: "●" },
  { href: "/calendar", label: "This week", icon: "▦" },
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

  const isActive = (href: string) => (href === "/" ? pathname === "/" : pathname?.startsWith(href));

  return (
    <div className="min-h-screen lg:flex">
      {/* Desktop sidebar */}
      <aside
        className="no-print hidden shrink-0 flex-col lg:flex lg:fixed lg:inset-y-0 lg:left-0 lg:w-64 lg:border-r"
        style={{ background: "var(--sidebar-bg)", borderColor: "var(--sidebar-border)" }}
      >
        <div className="flex items-center gap-2 px-5 py-6">
          <span aria-hidden className="text-lg" style={{ color: "var(--sidebar-text-active)" }}>
            ✦
          </span>
          <span className="text-base font-bold" style={{ color: "var(--sidebar-text-active)" }}>
            ZERA ICT GUY :)
          </span>
        </div>
        <nav className="flex-1 px-3">
          <ul className="space-y-1">
            {TABS.map((tab) => {
              const active = isActive(tab.href);
              return (
                <li key={tab.href}>
                  <Link
                    href={tab.href}
                    className="flex items-center gap-3 rounded-lg px-3 py-2.5 text-[15px] font-semibold transition-colors"
                    style={{
                      color: active ? "var(--sidebar-text-active)" : "var(--sidebar-text)",
                      background: active ? "var(--sidebar-active-bg)" : "transparent",
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
        {user?.email && (
          <div
            className="border-t px-5 py-4 text-xs"
            style={{ borderColor: "var(--sidebar-border)", color: "var(--sidebar-text)" }}
          >
            Signed in as
            <br />
            <span className="font-semibold" style={{ color: "var(--sidebar-text-active)" }}>
              {user.email}
            </span>
          </div>
        )}
      </aside>

      {/* Mobile brand strip */}
      <div className="blur-bar no-print flex items-center justify-center gap-1.5 border-b border-[color:var(--border)] py-1.5 text-[11px] font-semibold tracking-wide text-[color:var(--muted)] lg:hidden">
        <span aria-hidden>✦</span> ZERA ICT GUY :)
      </div>

      <div className="min-w-0 flex-1 pb-20 lg:pb-0 lg:pl-64">{children}</div>

      {/* Mobile bottom tab bar */}
      <nav className="blur-bar no-print fixed bottom-0 inset-x-0 border-t border-[color:var(--border)] pb-[env(safe-area-inset-bottom)] lg:hidden">
        <ul className="mx-auto flex max-w-3xl px-2 py-1.5">
          {TABS.map((tab) => {
            const active = isActive(tab.href);
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
