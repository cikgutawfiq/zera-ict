import type { Metadata, Viewport } from "next";
import "./globals.css";
import { AuthProvider } from "@/lib/auth";
import { DataProvider } from "@/lib/store";
import Shell from "@/components/Shell";

export const metadata: Metadata = {
  title: "Zera ICT — Lesson Dashboard",
  description: "Scheme of work, timetable and lesson plans for Mr Tawfiq bin Rahmat.",
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  themeColor: "#0d1117",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <AuthProvider>
          <DataProvider>
            <Shell>{children}</Shell>
          </DataProvider>
        </AuthProvider>
      </body>
    </html>
  );
}
