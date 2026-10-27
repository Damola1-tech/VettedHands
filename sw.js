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
    data: { url: d.url || "./" },
  }));
});

self.addEventListener("notificationclick", (e) => {
  e.notification.close();
  const target = new URL((e.notification.data && e.notification.data.url) || "./", self.registration.scope).href;
  e.waitUntil(self.clients.matchAll({ type: "window", includeUncontrolled: true }).then((list) => {
    for (const c of list) { if (c.url.startsWith(self.registration.scope) && "focus" in c) return c.focus(); }
    return self.clients.openWindow(target);
  }));
});