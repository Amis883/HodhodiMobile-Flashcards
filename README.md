<p align="center">
  <img src="docs/banner.png" alt="Hodhodi Mobile Flashcards" width="100%">
</p>

<h1 align="center">Hodhodi Mobile Flashcards</h1>

<p align="center"><b>Remember what you learn. Study a little each day, and the app decides what to review next.</b></p>

<p align="center">
  <a href="https://amis883.github.io/HodhodiMobile-Flashcards/"><b>▶ Open the app</b></a> ·
  <a href="#install-in-30-seconds">Install</a> ·
  <a href="#how-studying-works">How it works</a> ·
  <a href="#features">Features</a> ·
  <a href="#publish-your-own-copy">Publish your own</a>
</p>

<p align="center">
  <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-green">
  <img alt="Works on iPhone and Android" src="https://img.shields.io/badge/iPhone%20%7C%20Android-installable-blue">
  <img alt="Works offline" src="https://img.shields.io/badge/offline-yes-teal">
  <img alt="No account" src="https://img.shields.io/badge/account-not%20needed-lightgrey">
  <img alt="FSRS scheduler" src="https://img.shields.io/badge/scheduler-FSRS-orange">
</p>

---

## What is Hodhodi?

Hodhodi Mobile Flashcards is a **free flashcard app for your phone**. You write cards (words, facts, formulas, interview answers, anything), study them, and tell the app how well you remembered each one. It then schedules every card for the moment you are about to forget it, so you spend your time on what needs practice instead of re-reading what you already know.

- **Nothing to download from a store.** Open one link, add it to your Home Screen, done.
- **Works on iPhone and Android**, and keeps working without internet.
- **Private.** No account, no server, no tracking. Your cards stay on your phone.
- **Free and open source** (MIT licence).

The name comes from *hodhod* (هدهد), the hoopoe, the bird of Persian poetry.

## Who is it for?

Students, language learners, people preparing for exams or job interviews, and anyone who wants to remember things for the long term. If you already use Anki, you can bring your cards with you.

## Screenshots

<p align="center">
  <img src="docs/study.png" alt="Studying a card" width="270">
  &nbsp;&nbsp;&nbsp;
  <img src="docs/edit-card.png" alt="Editing a card with image and voice buttons" width="270">
</p>
<p align="center"><i>Study a card and rate it · Add text, images and voice to a card</i></p>

## Install in 30 seconds

**Open this link on your phone:** https://amis883.github.io/HodhodiMobile-Flashcards/

| iPhone | Android |
| --- | --- |
| 1. Open the link in **Safari**<br>2. Tap **Share** (square with an arrow)<br>3. Tap **Add to Home Screen** → **Add**<br>4. Open **Hodhodi** from your Home Screen | 1. Open the link in **Chrome**<br>2. Tap the **⋮ menu**<br>3. Tap **Install app** (or **Add to Home screen**)<br>4. Open **Hodhodi** from your app list |

> If someone sent you the link in Telegram, WhatsApp or Instagram, first choose **Open in Safari** or **Open in Chrome**. Installing only works from a normal browser.

## How studying works

1. **Add cards.** Tap **+**. Write the front and the back, add tags if you like. Want a fill-in-the-blank card? Write `{{c1::the answer}}` in the front.
2. **Study.** Tap a deck, read the front, tap the card to see the back.
3. **Rate yourself:** **Again** (forgot), **Hard**, **Good** or **Easy**. The button shows when the card will come back.
4. **Come back tomorrow.** Cards you know well return after days or weeks; cards you struggle with return sooner.

Tap the ⚙︎ button while studying for Undo, Card Info, Night Mode and more. Everything else lives under **More → Preferences**.

## Features

| | |
| --- | --- |
| 🧠 **Smart scheduling** | FSRS (versions 4.5 and 5) with adjustable target retention, interval fuzz, and an optimizer that learns from your own reviews. Classic SM-2 style scheduling is also available. |
| 🖼️ **Rich cards** | Add images, record your voice, or attach audio files. Cards can read themselves aloud. |
| 📥 **Bring your Anki cards** | Import Anki text exports and `.apkg` packages, or paste lines of `front;back`. |
| 📤 **Your data is yours** | Export to text or CSV, or make a full backup with images and audio. Automatic local backups too. |
| 📊 **Know your progress** | Card counts, cards studied today, and a 30-day forecast of upcoming reviews. |
| 🌙 **Comfortable to use** | Night mode, adjustable text size, keyboard shortcuts, offline use. |

## Moving your cards from Anki

In Anki on your computer: **File → Export → Notes in Plain Text (.txt)**, or export an `.apkg` package. Put the file on your phone (AirDrop, Files, email), then in Hodhodi tap **Import File** on the Decks screen. Images and audio come across only from older-format `.apkg` exports, and `.apkg` import needs internet while it runs.

## Your privacy

Hodhodi has **no backend**. Cards, settings and media are stored in your phone's browser storage. Nothing is sent to anyone. Because there is no cloud sync, **make a backup now and then** (More → File → Create Backup) and keep it somewhere safe.

## FAQ

**Do I need an account?** No.
**Does it cost anything?** No.
**Does it work offline?** Yes, after the first time you open it.
**Can I use it on two devices?** Yes, but cards do not sync automatically. Move them with a backup or an export.
**Why did my cards disappear?** Phones can clear browser storage if an app is unused for a long time. Adding the app to your Home Screen helps, and backups protect you completely.
**Is this the official Anki app?** No. Hodhodi is independent and not affiliated with or endorsed by Anki.

---

## For developers

Hodhodi is a **Progressive Web App**: one web page, no server, no database and no build step.

| File | What it is |
| --- | --- |
| `index.html` | The whole app: HTML, CSS and JavaScript in one file |
| `manifest.webmanifest` | Name, colours and icons so phones can install it |
| `sw.js` | Service worker for offline use |
| `apple-touch-icon.png`, `icon-192.png`, `icon-512.png` | App icons (an original hoopoe drawing) |
| `docs/` | Banner and screenshots used in this README |
| `tools/make_icons.py` | Draws the icons (Python, Pillow, NumPy) |
| `publish.sh` | Uploads this folder to GitHub and turns on Pages |

Cards and settings live in `localStorage`; images and audio in `IndexedDB`. Scheduling code is plain JavaScript in `index.html` (`nxtF`, `stepR`, `optimize`). To change the app, edit `index.html` and reload. When you ship an update, change the cache name `C` in `sw.js` so phones fetch the new version.

## Publish your own copy

**Option A: one command** (needs `git` and the [GitHub CLI](https://cli.github.com))

```bash
cd HodhodiMobile-Flashcards
bash publish.sh
```

**Option B: plain git**

```bash
git init
git add .
git commit -m "Hodhodi Mobile Flashcards"
git branch -M main
git remote add origin https://github.com/amis883/HodhodiMobile-Flashcards.git
git push -u origin main
```

Then on GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch `main`, folder `/ (root)` → Save.**

**Option C: no tools.** Create a public repository named `HodhodiMobile-Flashcards`, click **Add file → Upload files**, drop in everything from this folder, commit, and switch on Pages as above.

Your app is then live at `https://amis883.github.io/HodhodiMobile-Flashcards/`. GitHub does not allow spaces in repository names, so "HodhodiMobile Flashcards" becomes `HodhodiMobile-Flashcards`.

**Share it:**

> Free flashcard app 🐦 Open this in Safari (iPhone) or Chrome (Android) and add it to your Home Screen: https://amis883.github.io/HodhodiMobile-Flashcards/

### App Store / Play Store

The web app is the easiest route. [PWABuilder](https://www.pwabuilder.com) can wrap the live link for Android and iOS. The App Store needs an Apple developer account (about 99 EUR per year) and a Mac with Xcode. Store packaging has not been tested for this project.

## Known limits

- No cloud sync; use backups or export and import.
- FSRS-6 is not included. The optimizer is a lightweight search, not the official trainer, and needs about 200 spaced reviews.
- `.apkg` import loads JSZip, sql.js and fzstd from the jsDelivr CDN while you import.

## Contributing

Ideas and bug reports are welcome: open an **Issue**. Pull requests are welcome too, since the whole app is one readable file.

## License

MIT. See [`LICENSE`](LICENSE).
