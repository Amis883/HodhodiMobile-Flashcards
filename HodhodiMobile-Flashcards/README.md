# 🐦 Hodhodi Mobile Flashcards

A free spaced-repetition flashcard app for your phone. It installs like a normal app on **iPhone and Android**, works **offline**, needs **no account**, and keeps all your cards on your own device.

**Open the app:** [https://amis883.github.com/HodhodiMobile-Flashcards/](https://github.com/Amis883/HodhodiMobile-Flashcards)

> Hodhodi is an independent project. It is not affiliated with or endorsed by Anki.

---

## How to use it on your phone

### iPhone (iOS)
1. Open the link above in **Safari** (not Chrome, not Telegram's built-in browser).
2. Tap the **Share** button (square with an arrow).
3. Tap **Add to Home Screen**, then **Add**.
4. Open **Hodhodi** from your Home Screen. It runs full-screen like an app.

### Android
1. Open the link above in **Chrome**.
2. Tap the **⋮ menu** → **Install app** (or **Add to Home screen**).
3. Open **Hodhodi** from your app drawer or Home Screen.

If the link was sent in Telegram, WhatsApp or Instagram, tap the menu there and choose **Open in Safari / Open in Chrome** first. Installing only works from a real browser.

### First steps
- Tap **+** to add a card (front, back, tags). Use `{{c1::word}}` for fill-in-the-blank cards.
- Tap a deck to study. Tap the card to show the answer, then rate it **Again / Hard / Good / Easy**.
- Open **More → Preferences** for the scheduler, audio, appearance and backups.

Each person has a private copy. Nothing is shared between users and nothing is uploaded anywhere.

---

## Features

- Decks, cards, tags, cloze deletions
- Images and voice recordings on cards, auto-play, read-aloud (text-to-speech)
- Anki-style screens: deck list, study screen with tools overlay, Browse, Stats, Preferences
- **FSRS scheduler** (FSRS-4.5 and FSRS-5 default parameters), desired retention, same-day reviews (FSRS-5), interval fuzz, a **parameter optimizer** trained on your own review log, Card Info with stability, difficulty and retrievability
- Classic SM-2 style scheduler as an option
- **Import:** Anki "Notes in Plain Text" exports, `.apkg` packages (needs internet while importing), tab-separated or `;` text, backups
- **Export:** text, CSV, full backup including images and audio, plus automatic local backups
- Night mode, adjustable UI size, keyboard shortcuts, offline use

### Moving cards from Anki
In Anki on your computer: **File → Export → Notes in Plain Text (.txt)** (or an `.apkg` package). Put the file on your phone (AirDrop, Files, email), then in Hodhodi tap **Import File** on the Decks screen. Images and audio come across only from older-format `.apkg` exports.

---

## How this app is made

Hodhodi is a **Progressive Web App (PWA)**: a normal web page that can be installed on a phone. There is **no server, no database and no build step**.

| File | What it is |
| --- | --- |
| `index.html` | The whole app: HTML, CSS and JavaScript in one file |
| `manifest.webmanifest` | Name, colours and icons so phones can install it |
| `sw.js` | Service worker that lets the app work offline |
| `apple-touch-icon.png`, `icon-192.png`, `icon-512.png` | App icons (an original hoopoe drawing) |
| `tools/make_icons.py` | Script that draws the icons (Python, Pillow, NumPy) |
| `publish.sh` | Helper that uploads this folder to GitHub and turns on Pages |
| `LICENSE` | MIT licence |

How it works inside:
- Cards and settings are stored in the browser's `localStorage`; images and audio in `IndexedDB`.
- Scheduling is plain JavaScript in `index.html` (`nxtF`, `stepR`, `optimize`).
- To change the app, edit `index.html` and reload. When you ship an update, change the cache name `C` in `sw.js` (for example `hodhodi-v3`) so phones fetch the new version.
- To redraw the icons: `pip install pillow numpy` then `python3 tools/make_icons.py`.

---

## Publish your own copy (GitHub Pages, free)

**Option A: one command (needs `git` and the GitHub CLI, `gh`)**

```bash
cd HodhodiMobile-Flashcards
bash publish.sh
```

It creates the repository `amis883/HodhodiMobile-Flashcards`, pushes the files and switches on GitHub Pages. `gh` will ask you to log in the first time.

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

**Option C: no tools at all**
1. On github.com create a **public** repository named `HodhodiMobile-Flashcards`.
2. Click **Add file → Upload files**, drop in everything from this folder, and commit.
3. Turn on Pages as above.

After about a minute the app is live at `[https://amis883.github.io/HodhodiMobile-Flashcards/](https://github.com/Amis883/HodhodiMobile-Flashcards)`.
GitHub does not allow spaces in repository names, so "HodhodiMobile Flashcards" becomes `HodhodiMobile-Flashcards`.

### Share it
Send the link. Example message:

> Free flashcard app 🐦 Open this in Safari (iPhone) or Chrome (Android) and add it to your Home Screen: https://amis883.github.io/HodhodiMobile-Flashcards/

---

## Optional: App Store / Play Store packages

The PWA is the easiest route. If you want store packages, [PWABuilder](https://www.pwabuilder.com) can wrap the live link for Android and iOS. The App Store needs an Apple developer account (about 99 EUR per year) and a Mac with Xcode. Store packaging has not been tested for this project.

---

## Notes and limits

- No cloud sync. Move data with **Create Backup / Revert to Backup** or **Export / Import**.
- `.apkg` import loads JSZip, sql.js and fzstd from the jsDelivr CDN while you import.
- FSRS-6 is not included. The optimizer is a lightweight search, not the official trainer, and needs about 200 spaced reviews.
- Browser storage can be cleared by the phone if the app is unused for a long time. Installing to the Home Screen helps; backups protect you fully.

## License

MIT. See `LICENSE`.
