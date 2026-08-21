import type { NextConfig } from "next";

// The dashboard is embedded as an iframe on cikgutawfiq.com/zera-ict.
// frame-ancestors (not X-Frame-Options) is what allows that, and Next does not
// send X-Frame-Options by default — so nothing needs to be removed.
const FRAME_ANCESTORS = [
  "'self'",
  "https://cikgutawfiq.com",
  "https://*.cikgutawfiq.com",
].join(" ");

const nextConfig: NextConfig = {
  async headers() {
    return [
      {
        source: "/:path*",
        headers: [
          { key: "Content-Security-Policy", value: `frame-ancestors ${FRAME_ANCESTORS};` },
          { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
          { key: "X-Content-Type-Options", value: "nosniff" },
        ],
      },
    ];
  },
};

export default nextConfig;
