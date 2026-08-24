"use client";

import { useRef, useState } from "react";
import html2canvas from "html2canvas";
import { jsPDF } from "jspdf";

export type MindMapNode = {
  id: string;
  title: string;
  subtitle?: string;
};

const PALETTE = [
  "#2563eb",
  "#059669",
  "#d97706",
  "#dc2626",
  "#7c3aed",
  "#0891b2",
  "#db2777",
  "#65a30d",
  "#4f46e5",
  "#ea580c",
  "#0d9488",
  "#9333ea",
  "#ca8a04",
  "#e11d48",
  "#0284c7",
];

function polar(cx: number, cy: number, r: number, angle: number) {
  return { x: cx + r * Math.cos(angle), y: cy + r * Math.sin(angle) };
}

export function MindMap({
  centerTitle,
  centerSubtitle,
  nodes,
  filename,
}: {
  centerTitle: string;
  centerSubtitle?: string;
  nodes: MindMapNode[];
  filename: string;
}) {
  const ref = useRef<HTMLDivElement>(null);
  const [exporting, setExporting] = useState(false);

  const N = nodes.length;
  const W = 1500;
  const H = Math.max(1000, 620 + N * 26);
  const cx = W / 2;
  const cy = H / 2;
  const r1 = Math.min(560, 300 + N * 9);
  const r2 = r1 + 150;

  const positions = nodes.map((n, i) => {
    const angle = -Math.PI / 2 + i * ((2 * Math.PI) / N);
    const topic = polar(cx, cy, r1, angle);
    const sub = n.subtitle ? polar(cx, cy, r2, angle) : null;
    const color = PALETTE[i % PALETTE.length];
    return { node: n, angle, topic, sub, color };
  });

  const exportPdf = async () => {
    if (!ref.current) return;
    setExporting(true);
    try {
      const canvas = await html2canvas(ref.current, {
        backgroundColor: "#ffffff",
        scale: 1.5,
        logging: false,
      });
      const doc = new jsPDF({
        unit: "px",
        format: [canvas.width, canvas.height],
        orientation: canvas.width >= canvas.height ? "landscape" : "portrait",
        compress: true,
      });
      doc.addImage(canvas.toDataURL("image/jpeg", 0.85), "JPEG", 0, 0, canvas.width, canvas.height);
      doc.save(filename);
    } finally {
      setExporting(false);
    }
  };

  return (
    <div>
      <div className="no-print mb-3 flex justify-end">
        <button className="btn btn-sm btn-primary" onClick={exportPdf} disabled={exporting || N === 0}>
          {exporting ? "Exporting…" : "📥 Save as PDF"}
        </button>
      </div>

      {N === 0 ? (
        <div className="card p-8 text-center text-sm text-[color:var(--muted)]">
          No topics set for this class &amp; term yet.
        </div>
      ) : (
        <div className="overflow-x-auto rounded-2xl border border-[color:var(--border)]">
          <div
            ref={ref}
            style={{ width: W, height: H, position: "relative", background: "#ffffff" }}
          >
            <svg width={W} height={H} style={{ position: "absolute", inset: 0 }}>
              {positions.map(({ topic, sub, color }, i) => (
                <g key={i}>
                  <line x1={cx} y1={cy} x2={topic.x} y2={topic.y} stroke={color} strokeWidth={3} opacity={0.55} />
                  {sub && (
                    <line x1={topic.x} y1={topic.y} x2={sub.x} y2={sub.y} stroke={color} strokeWidth={2} opacity={0.35} />
                  )}
                </g>
              ))}
            </svg>

            {/* Center node */}
            <div
              style={{
                position: "absolute",
                left: cx,
                top: cy,
                transform: "translate(-50%, -50%)",
                width: 260,
                borderRadius: 20,
                background: "#111827",
                color: "#ffffff",
                padding: "18px 20px",
                textAlign: "center",
                boxShadow: "0 8px 24px rgba(0,0,0,0.18)",
              }}
            >
              <div style={{ fontSize: 20, fontWeight: 800, lineHeight: 1.25 }}>{centerTitle}</div>
              {centerSubtitle && (
                <div style={{ fontSize: 13, marginTop: 4, opacity: 0.75, fontWeight: 600 }}>{centerSubtitle}</div>
              )}
            </div>

            {positions.map(({ node, topic, sub, color }, i) => (
              <div key={node.id}>
                <div
                  style={{
                    position: "absolute",
                    left: topic.x,
                    top: topic.y,
                    transform: "translate(-50%, -50%)",
                    width: 190,
                    borderRadius: 14,
                    background: color,
                    color: "#ffffff",
                    padding: "10px 12px",
                    textAlign: "center",
                    fontSize: 13,
                    fontWeight: 700,
                    lineHeight: 1.3,
                    boxShadow: "0 4px 12px rgba(0,0,0,0.15)",
                  }}
                >
                  {node.title}
                </div>
                {sub && node.subtitle && (
                  <div
                    style={{
                      position: "absolute",
                      left: sub.x,
                      top: sub.y,
                      transform: "translate(-50%, -50%)",
                      width: 170,
                      borderRadius: 12,
                      background: "#ffffff",
                      border: `2px solid ${color}`,
                      color: "#1f2937",
                      padding: "8px 10px",
                      textAlign: "center",
                      fontSize: 11.5,
                      fontWeight: 600,
                      lineHeight: 1.3,
                    }}
                  >
                    {node.subtitle}
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
