// Usage: node scale-fonts.js index.html
// Makes a backup (index.before-fonts.html) and shrinks the font sizes of the redesigned screens.
const fs = require("fs");
const file = process.argv[2] || "index.html";
const raw = fs.readFileSync(file, "utf8");
const nl = raw.includes("\r\n") ? "\r\n" : "\n";
let s = raw.replace(/\r\n/g, "\n");
if (s.includes("/* fonts-scaled */")) { console.log("Already scaled. Nothing to do."); process.exit(0); }
fs.writeFileSync(file.replace(/\.html$/, ".before-fonts.html"), raw);

const start = s.indexOf("/* ===== Home (new design) ===== */");
const end = s.indexOf("@media (max-width: 480px) {", start);
if (start < 0 || end < 0) { console.log("Could not find the CSS section. Send me the file."); process.exit(1); }

function scale(f) {
  if (f < 12) return f;
  const k = f >= 24 ? 0.82 : f >= 17 ? 0.86 : f >= 13 ? 0.89 : 0.93;
  return Math.max(11, Math.round(f * k * 2) / 2);
}
const SKIP = /input|textarea|select|\.rf-text|\.rf-date/;
let n = 0;
let css = s.slice(start, end).replace(/([^{}]+)\{([^{}]*)\}/g, (all, sel, body) => {
  if (SKIP.test(sel)) return all;
  const nb = body.replace(/font-size:\s*([\d.]+)px/g, (m, v) => { n++; return "font-size:" + scale(parseFloat(v)) + "px"; });
  return sel + "{" + nb + "}";
});
s = s.slice(0, start) + "/* fonts-scaled */\n      " + css + s.slice(end);
fs.writeFileSync(file, s.replace(/\n/g, nl));
console.log("Done. Resized " + n + " font sizes. Backup: " + file.replace(/\.html$/, ".before-fonts.html"));