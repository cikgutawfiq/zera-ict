"use client";

import { createContext, useContext, useEffect, useState, type ReactNode } from "react";
import {
  onAuthStateChanged,
  signInWithPopup,
  signOut as fbSignOut,
  browserLocalPersistence,
  setPersistence,
  type User,
} from "firebase/auth";
import { getFirebaseAuth, googleProvider, OWNER_EMAIL } from "./firebase";

type AuthState = {
  user: User | null;
  loading: boolean;
  isOwner: boolean;
  error: string | null;
  signIn: () => Promise<void>;
  signOut: () => Promise<void>;
};

const Ctx = createContext<AuthState | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const auth = getFirebaseAuth();
    setPersistence(auth, browserLocalPersistence).catch(() => {});
    return onAuthStateChanged(auth, (u) => {
      setUser(u);
      setLoading(false);
    });
  }, []);

  const signIn = async () => {
    setError(null);
    try {
      // Popup, not redirect: the redirect flow breaks inside a cross-origin iframe.
      await signInWithPopup(getFirebaseAuth(), googleProvider);
    } catch (e) {
      const code = (e as { code?: string }).code ?? "";
      setError(
        code === "auth/popup-blocked"
          ? "Your browser blocked the sign-in popup. Allow popups for this page, or open the dashboard in its own tab."
          : `Sign-in failed (${code || (e as Error).message}).`,
      );
    }
  };

  const signOut = async () => {
    await fbSignOut(getFirebaseAuth());
  };

  const isOwner = !!user && user.email?.toLowerCase() === OWNER_EMAIL.toLowerCase();

  return <Ctx.Provider value={{ user, loading, isOwner, error, signIn, signOut }}>{children}</Ctx.Provider>;
}

export function useAuth(): AuthState {
  const v = useContext(Ctx);
  if (!v) throw new Error("useAuth must be used inside <AuthProvider>");
  return v;
}
