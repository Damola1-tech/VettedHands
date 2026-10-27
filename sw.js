self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", (e) => e.waitUntil(self.clients.claim()));

self.addEventListener("push", (e) => {
  // Tell any open VettedHands window to refresh now, so the screen changes at the same moment as the alert.
  e.waitUntil(self.clients.matchAll({ type: "window", includeUncontrolled: true }).then((list) => list.forEach((c) => c.postMessage({ type: "vh-refresh" }))));
  let d = {};
  try { d = e.data ? e.data.json() : {}; } catch (err) { d = { title: "VettedHands", body: e.data ? e.data.text() : "" }; }
  e.waitUntil(self.registration.showNotification(d.title || "VettedHands", {
    body: d.body || "",
    icon: "apple-touch-icon.png",
    badge: "favicon-96.png",
    tag: d.tag || undefined,
    renotify: !!d.tag,
    vibrate: [100, 50, 100],
    data: { url: d.url || "./", nt: d.nt || "", rid: d.rid || "" },
  }));
});

self.addEventListener("notificationclick", (e) => {
  e.notification.close();
  const target = new URL((e.notification.data && e.notification.data.url) || "./", self.registration.scope).href;
  e.waitUntil(self.clients.matchAll({ type: "window", includeUncontrolled: true }).then((list) => {
    const nd = e.notification.data || {};
    for (const c of list) {
      if (c.url.startsWith(self.registration.scope) && "focus" in c) {
        c.postMessage({ type: "vh-open", nt: nd.nt || "", rid: nd.rid || "" }); // the open app jumps to the right screen
        return c.focus();
      }
    }
    const u = new URL(target);
    if (nd.nt) u.searchParams.set("nt", nd.nt);
    if (nd.rid) u.searchParams.set("rid", nd.rid);
    return self.clients.openWindow(u.href); // a closed app opens straight onto the right screen
  }));
});