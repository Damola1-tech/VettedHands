# Builds the static service pages people can find on Google. Run: python3 gen-seo.py
import html, json
SITE = "https://vettedhands.com.ng"
PAGES = [
 dict(slug="electrician", trade="Electrician", plural="electricians", file="electrician-ado-ekiti.html",
  jobs=["Fixing sockets, switches and faulty wiring","Installing lights, fans and changeover switches","Tracing power trips and short circuits","House and shop wiring for new buildings"],
  intro="A bad electrician is a risk to your home, not just your wallet. Wiring done wrong can burn out appliances or start a fire.",
  tips=["Ask what caused the fault, not only how much the fix costs.","Agree what is included, such as cables and fittings, before work starts.","Be careful of anyone who asks for the full payment before touching the job."],
  faq=[("How do I find a good electrician in Ado-Ekiti?","Look for someone who is verified, has reviews from real customers, and will agree the price in writing before starting. VettedHands is being built to show exactly that."),("How much does an electrician cost in Ado-Ekiti?","It depends on the job. A small fix costs far less than rewiring a room. Always get the price agreed before work begins.")]),
 dict(slug="plumber", trade="Plumber", plural="plumbers", file="plumber-ado-ekiti.html",
  jobs=["Leaking taps, pipes and cisterns","Blocked sinks, toilets and drains","Installing water tanks, pumps and fittings","Bathroom and kitchen plumbing"],
  intro="A small leak that is ignored becomes a damaged ceiling or a big water bill. The right plumber fixes the cause, not just the drip.",
  tips=["Take a photo of the problem and send it before the visit, so the plumber can come prepared.","Ask whether parts are included in the price.","Check the fix before the plumber leaves, and keep the payment until you are happy."],
  faq=[("Where can I find a reliable plumber in Ado-Ekiti?","Choose a verified plumber with reviews from real customers. On VettedHands, your payment is held safely until you confirm the job is done."),("What should I do if a plumber does not finish the job?","Do not pay the rest. Report it. On VettedHands, our team reviews the case and can refund you.")]),
 dict(slug="tailor", trade="Tailor", plural="tailors", file="tailor-ado-ekiti.html",
  jobs=["Native wear, aso ebi and corporate outfits","Alterations and repairs","School uniforms and event outfits","Custom designs from a photo you show"],
  intro="Everyone has a story about a tailor who missed the deadline or ruined the fabric. A good tailor is worth finding and keeping.",
  tips=["Show a picture of the style you want and agree the date in writing.","Ask to see examples of their earlier work.","Confirm the price, fabric and number of fittings before you pay."],
  faq=[("How do I find a good tailor in Ado-Ekiti?","Look for a verified tailor with a portfolio and reviews. VettedHands lets you see their work and chat before you book."),("Should I pay a tailor upfront?","A small deposit may be normal, but paying everything before the work is risky. VettedHands holds your payment until you confirm the outfit is done.")]),
 dict(slug="barber", trade="Barber", plural="barbers", file="barber-ado-ekiti.html",
  jobs=["Haircuts and fades","Beard grooming and shaping","Home or event grooming","Kids' haircuts"],
  intro="A good barber knows your head shape and your style. Finding one you trust saves you from a bad cut before a big day.",
  tips=["Show a photo of the cut you want.","Agree the price and time before you sit down.","Check reviews or ask friends before trying someone new."],
  faq=[("How can I find a trusted barber in Ado-Ekiti?","Choose a verified barber with reviews from real customers. VettedHands is being built to make that easy."),("Can I book a barber to come to me?","Some barbers do home or event visits. Ask when you send your request and agree the price first.")]),
 dict(slug="phone repairer", trade="Phone Repairer", plural="phone repairers", file="phone-repair-ado-ekiti.html",
  jobs=["Cracked screens and broken glass","Battery and charging port problems","Water damage and software issues","Unlocking and phone setup"],
  intro="Handing over your phone means handing over your photos, chats and bank apps. You want someone verified and honest.",
  tips=["Back up your phone before any repair.","Ask what parts will be used, and whether they are original or not.","Agree the price before the repair starts, and test everything before you pay."],
  faq=[("Where can I repair my phone in Ado-Ekiti?","Look for a verified repairer with real reviews. VettedHands is being built so you can compare repairers, agree the price in the app and pay safely."),("How do I avoid being cheated by a phone repairer?","Agree the price first, ask what parts are used, and keep payment until it works. VettedHands holds your payment until you confirm.")]),
 dict(slug="carpenter", trade="Carpenter", plural="carpenters", file="carpenter-ado-ekiti.html",
  jobs=["Doors, windows, wardrobes and cabinets","Roofing wood and ceiling work","Furniture repair and custom furniture","Shop shelves and counters"],
  intro="Good carpentry lasts for years, and bad carpentry shows up in a few months. The difference is the person you hire.",
  tips=["Ask who buys the wood, and agree the quality and quantity.","Look at photos of earlier work before you decide.","Agree the delivery date, and pay in stages tied to progress."],
  faq=[("How do I find a good carpenter in Ado-Ekiti?","Look for a verified carpenter with a portfolio and real reviews. VettedHands is being built so you can compare and agree the price in the app."),("Should I pay a carpenter before they start?","A deposit for materials is common, but paying everything upfront is risky. VettedHands holds your payment until you confirm the work is done.")]),
 dict(slug="generator repairer", trade="Generator Repairer", plural="generator repairers", file="generator-repair-ado-ekiti.html",
  jobs=["Servicing and tuning petrol generators","Fixing hard starting and fuel problems","Replacing plugs, filters and carburettors","Diagnosing noise, smoke and power faults"],
  intro="When the light is out, a generator that will not start costs you money every hour. A skilled repairer finds the real fault fast.",
  tips=["Ask what is wrong and which part needs replacing before you agree a price.","Keep the old parts to confirm they were changed.","Test the generator under load before you pay."],
  faq=[("Where can I find a generator repairer in Ado-Ekiti?","Look for a verified repairer with reviews from real customers. VettedHands is being built to make that easy and safe."),("How do I avoid paying for repairs that were not done?","Agree the work and the price first, keep payment until it runs properly, and keep the old parts. VettedHands holds your payment until you confirm.")]),
 dict(slug="hairdresser", trade="Hairdresser", plural="hairdressers", file="hairdresser-ado-ekiti.html",
  jobs=["Braids, weaves and wig installation","Relaxing, washing and styling","Natural hair care and treatments","Bridal and event hair"],
  intro="A good hairdresser is on time, keeps their word on the price, and does not leave you waiting all day.",
  tips=["Show a picture of the style and ask how long it will take.","Agree the price, including hair and extensions, before you start.","Book ahead for events and confirm the day before."],
  faq=[("How can I find a good hairdresser in Ado-Ekiti?","Choose a verified hairdresser with real reviews and photos of their work. VettedHands is being built so you can compare and book safely."),("Can I book a hairdresser to come to my home?","Some do home service. Ask when you send your request and agree the price first.")]),
 dict(slug="ac technician", trade="AC Technician", plural="AC technicians", file="ac-repair-ado-ekiti.html",
  jobs=["Air conditioner and fridge repair","Installing split units","Gas refilling and servicing","Fixing cooling problems and leaks"],
  intro="A cooling fault gets worse the longer you wait. A trained technician can tell you whether it is a quick fix or a bigger problem.",
  tips=["Ask what the fault is and which parts are needed.","Agree the price before the work, including gas and parts.","Ask for a short warranty on the repair."],
  faq=[("Where can I find an AC technician in Ado-Ekiti?","Look for a verified technician with real reviews. VettedHands is being built to help you compare and book safely."),("How much does AC repair cost?","It depends on the fault and the parts. Always agree the price before work starts.")]),
 dict(slug="painter", trade="Painter", plural="painters", file="painter-ado-ekiti.html",
  jobs=["Painting rooms, houses and shops","Ceiling and POP finishing","Gate and fence painting","Repainting and touch-ups"],
  intro="A fresh coat of paint changes how a place looks, but poor preparation and cheap paint show quickly. Choose someone who cares about the finish.",
  tips=["Agree the brand and number of coats before you start.","Ask who buys the paint and who supplies the tools.","Check one wall before the painter moves on."],
  faq=[("How do I find a reliable painter in Ado-Ekiti?","Choose a verified painter with photos of past work and real reviews. VettedHands is being built to help you compare and book safely."),("Should I pay before a painter starts?","A small deposit for materials is normal, but not the full amount. VettedHands holds your payment until you confirm.")]),
]
# More services live in services.json, so adding one is a few lines of data, not code.
def _generic(e):
    t, pl = e["trade"], e["plural"]
    return dict(slug=t.lower(), trade=t, plural=pl, file=e["file"], jobs=e["jobs"],
      intro=f"Hiring a {t.lower()} should not be a gamble. The right person turns up, does the job properly and keeps their word on the price.",
      tips=["Ask to see examples of earlier work, or read reviews from real customers.","Agree what the price covers, including parts or materials, before work starts.","Keep the payment until you have checked that the job is done properly."],
      faq=[(f"How do I find a trusted {t.lower()} in Ado-Ekiti?", f"Look for a verified {t.lower()} with reviews from real customers. VettedHands is being built so you can compare {pl}, agree the price in the app and pay safely."),
           (f"Is it safe to pay a {t.lower()} upfront?", "Paying everything before the work is risky. On VettedHands your payment is held safely and only released when you confirm the job is done.")])
import os
if os.path.exists("services.json"):
    PAGES += [_generic(e) for e in json.load(open("services.json", encoding="utf-8"))]
CSS = """:root{--g:#0F4D3A;--g2:#14604A;--cream:#F5F0E4;--gold:#E9B872;--ink:#16221d}*{box-sizing:border-box}body{margin:0;font-family:'Figtree',system-ui,-apple-system,Segoe UI,Roboto,sans-serif;background:var(--cream);color:var(--ink);line-height:1.6}header{background:var(--g);color:var(--cream);padding:14px 20px}header a{color:var(--cream);text-decoration:none;font-weight:800;letter-spacing:.04em}main{max-width:720px;margin:0 auto;padding:28px 20px 60px}h1{font-family:'Bricolage Grotesque','Figtree',sans-serif;font-size:2rem;line-height:1.15;margin:.2em 0 .5em;color:var(--g)}h2{font-family:'Bricolage Grotesque','Figtree',sans-serif;color:var(--g);margin-top:1.8em}ul{padding-left:1.2em}.cta{display:inline-block;background:var(--g);color:var(--cream);padding:14px 22px;border-radius:12px;text-decoration:none;font-weight:700;margin:12px 0}.box{background:#fff;border-radius:14px;padding:16px 18px;margin:12px 0}.links a{display:inline-block;margin:4px 10px 4px 0;color:var(--g2)}footer{text-align:center;color:#556;padding:20px;font-size:.9rem}footer a{color:var(--g2)}"""
FONT = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600..800&family=Figtree:wght@400;600;700&display=swap">'
def head(title, desc, url, extra=""):
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0F4D3A">
<link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website"><meta property="og:site_name" content="VettedHands"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/og-image.png">
<meta name="twitter:card" content="summary_large_image">
{FONT}<style>{CSS}</style>{extra}</head><body>
<header><a href="{SITE}/waitlist.html">VETTEDHANDS</a></header><main>'''
FOOT = '</main><footer>VettedHands · Starting in Ado-Ekiti, Ekiti State · <a href="find-artisans-ado-ekiti.html">All services</a> · <a href="how-it-works.html">How it works</a> · <a href="about.html">About</a></footer></body></html>'
def page(p):
    url = f"{SITE}/{p['file']}"
    t = p["trade"]; pl = p["plural"]
    title = f"Find a Trusted {t} in Ado-Ekiti | VettedHands"
    desc = f"Looking for a reliable {t.lower()} in Ado-Ekiti? VettedHands is building a way to book verified {pl} and pay safely. Join the waitlist."
    faq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p["faq"]]}
    crumbs = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"VettedHands","item":SITE+"/"},{"@type":"ListItem","position":2,"name":"Services in Ado-Ekiti","item":SITE+"/find-artisans-ado-ekiti.html"},{"@type":"ListItem","position":3,"name":t+" in Ado-Ekiti","item":url}]}
    extra = f'<script type="application/ld+json">{json.dumps(faq)}</script><script type="application/ld+json">{json.dumps(crumbs)}</script>'
    others = "".join(f'<a href="{o["file"]}">{o["trade"]}s</a>' for o in PAGES if o["file"] != p["file"])
    b = head(title, desc, url, extra)
    b += f'<h1>How to find a trusted {t.lower()} in Ado-Ekiti</h1><p>{html.escape(p["intro"])}</p>'
    b += f'<h2>What a {t.lower()} can help with</h2><ul>' + "".join(f"<li>{html.escape(j)}</li>" for j in p["jobs"]) + "</ul>"
    b += f'<h2>Before you hire anyone</h2><ul>' + "".join(f"<li>{html.escape(x)}</li>" for x in p["tips"]) + "</ul>"
    b += f'<div class="box"><b>How VettedHands will help.</b> You compare verified {pl}, chat to agree the price, and pay through the app. Your payment is held safely and only goes to the {t.lower()} when you confirm the job is done. If something goes wrong, our team reviews it. We are starting in Ado-Ekiti and the waitlist is open.</div>'
    b += '<a class="cta" href="waitlist.html">Join the waitlist</a>'
    b += '<h2>Common questions</h2>' + "".join(f"<p><b>{html.escape(q)}</b><br>{html.escape(a)}</p>" for q,a in p["faq"])
    b += f'<h2>Other services</h2><p class="links">{others}</p>' + FOOT
    open(p["file"], "w", encoding="utf-8").write(b)
def hub():
    url = f"{SITE}/find-artisans-ado-ekiti.html"
    title = "Find Trusted Artisans in Ado-Ekiti | VettedHands"
    desc = "Electricians, plumbers, tailors, barbers and phone repairers in Ado-Ekiti. VettedHands is building a safer way to book verified artisans. Join the waitlist."
    b = head(title, desc, url)
    b += '<h1>Find trusted artisans in Ado-Ekiti</h1><p>VettedHands connects you with verified artisans and holds your payment safely until the job is done. We are starting in Ado-Ekiti, and the waitlist is open.</p><div class="box links">'
    b += "".join(f'<a href="{o["file"]}"><b>{o["trade"]}s in Ado-Ekiti</b></a><br>' for o in PAGES) + '</div><a class="cta" href="waitlist.html">Join the waitlist</a>' + FOOT
    open("find-artisans-ado-ekiti.html", "w", encoding="utf-8").write(b)
for p in PAGES: page(p)
hub()
def simple(file, title, desc, h1, body, extra=""):
    url = f"{SITE}/{file}"
    open(file, "w", encoding="utf-8").write(head(title, desc, url, extra) + f"<h1>{h1}</h1>" + body + '<a class="cta" href="waitlist.html">Join the waitlist</a>' + FOOT)
org = '<script type="application/ld+json">' + json.dumps({"@context":"https://schema.org","@type":"WebSite","name":"VettedHands","url":SITE+"/","inLanguage":"en-NG"}) + '</script>'
org += '<script type="application/ld+json">' + json.dumps({"@context":"https://schema.org","@type":"Organization","name":"VettedHands","url":SITE+"/","logo":SITE+"/icon-512.png","sameAs":["https://instagram.com/vettedhands.ng", "https://tiktok.com/@vettedhands.ng", "https://x.com/Vettedhands"]}) + '</script>'
simple("online-artisan-marketplace-nigeria.html",
 "Online Marketplace for Verified Artisans in Nigeria | VettedHands Nigeria",
 "VettedHands is an online marketplace in Nigeria where you find verified artisans, agree the price in the app, and pay safely. Starting in Ado-Ekiti. Join the waitlist.",
 "An online marketplace for verified artisans in Nigeria",
 "<p>Finding a good artisan in Nigeria usually means asking around and hoping. VettedHands is an online marketplace that makes it simpler and safer: electricians, plumbers, tailors, barbers, phone repairers and more, all in one place.</p><h2>How the marketplace works</h2><ul><li><b>Find:</b> browse verified artisans with profiles, photos and reviews.</li><li><b>Agree:</b> chat in the app and agree the price before any work starts.</li><li><b>Pay safely:</b> your payment is made through the app and held safely until you confirm the job is done.</li><li><b>Review:</b> rate the work, so the next customer knows who to trust.</li></ul><h2>For artisans</h2><p>Get verified, build your profile and reviews, and get paid for finished work without chasing customers.</p><p>We are starting in Ado-Ekiti, Ekiti State, and the waitlist is open.</p>",
 org)
simple("about.html",
 "About VettedHands Nigeria | Verified Artisans, Safe Payments",
 "VettedHands is a Nigerian marketplace that connects customers with verified artisans and holds payments safely until the job is done. Founded by Oyindamola Lawal (Damola) in Ado-Ekiti.",
 "About VettedHands",
 "<p>Everybody in Nigeria has a story about hiring an artisan: paying upfront and getting ghosted, or half-done work. Artisans have their own story: finishing the job and not getting paid. VettedHands is being built to fix both sides.</p><h2>What we do</h2><p>We verify artisans, let customers agree the price in the app, and hold the payment safely until the customer confirms the job is done. If there is a problem, our team reviews it and decides fairly.</p><h2>Who is behind it</h2><p>VettedHands was founded by Oyindamola Lawal (Damola) in Ado-Ekiti, Ekiti State, and is starting with customers and artisans around Ekiti State University.</p>",
 org)
simple("how-it-works.html",
 "How VettedHands Nigeria Works | Book Verified Artisans Safely",
 "How to book a verified artisan on VettedHands: send a request, chat and agree the price, pay safely through the app, and confirm when the job is done.",
 "How VettedHands works",
 "<h2>For customers</h2><ol><li>Search for the service you need and compare verified artisans.</li><li>Send a request and chat once they accept.</li><li>Agree the price in the app and pay securely.</li><li>The artisan does the job and sends a photo as proof.</li><li>You confirm, and the payment is released to the artisan.</li></ol><p>If something goes wrong, report it. Our team reviews the case and can release, refund or split the payment.</p><h2>For artisans</h2><ol><li>Apply and get verified.</li><li>Receive requests and accept the jobs you want.</li><li>The customer pays first, so you start with confidence.</li><li>Finish, send proof, and get paid once the customer confirms.</li></ol>",
 org)
urls = ["/", "/waitlist.html", "/find-artisans-ado-ekiti.html", "/online-artisan-marketplace-nigeria.html", "/about.html", "/how-it-works.html"] + ["/" + p["file"] for p in PAGES]
open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{SITE}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
print("pages:", len(PAGES) + 1)
