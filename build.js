// Build step: turns the in-browser JSX into plain, minified JavaScript so the app loads fast.
// Run with:  node build.js   (needs: npm install esbuild). Output goes to ./dist
const fs = require("fs");
const path = require("path");
const esbuild = require("esbuild");

const OUT = "dist";
const PAGES = ["index.html", "Admin.html"];
const SKIP = new Set(["dist", "node_modules", ".git", ".github", "build.js", "package.json", "package-lock.json", ".gitignore", "README.md"]);

fs.rmSync(OUT, { recursive: true, force: true });
fs.mkdirSync(OUT);

for (const f of fs.readdirSync(".")) {
  if (SKIP.has(f) || fs.statSync(f).isDirectory()) continue;
  if (PAGES.includes(f)) continue;
  fs.copyFileSync(f, path.join(OUT, f));
}

for (const page of PAGES) {
  if (!fs.existsSync(page)) continue;
  let html = fs.readFileSync(page, "utf8");
  const re = /<script type="text\/babel"[^>]*>([\s\S]*?)<\/script>/;
  const m = html.match(re);
  if (!m) throw new Error(page + ": no text/babel script found");
  const out = esbuild.transformSync(m[1], { loader: "jsx", minify: true, target: ["es2018", "safari13"], legalComments: "none" });
  html = html.replace(re, "");
  html = html.replace(/<script src="[^"]*babel[^"]*"><\/script>\s*/i, "");
  // run after the page has loaded (Babel used to do this for us)
  const code = out.code.replace(/<\/script/gi, "<\\/script");
  html = html.replace("</body>", () => "<script>" + code + "</script>\n</body>");
  fs.writeFileSync(path.join(OUT, page), html);
  console.log(page, Math.round(fs.statSync(page).size / 1024) + " KB ->", Math.round(fs.statSync(path.join(OUT, page)).size / 1024) + " KB");
}