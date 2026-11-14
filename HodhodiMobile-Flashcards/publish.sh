#!/usr/bin/env bash
# Uploads this folder to GitHub as amis883/HodhodiMobile-Flashcards and turns on GitHub Pages.
# Needs: git and the GitHub CLI (https://cli.github.com).  Run:  bash publish.sh
set -e
USER_NAME="amis883"
REPO="HodhodiMobile-Flashcards"

command -v git >/dev/null || { echo "Please install git first."; exit 1; }
command -v gh  >/dev/null || { echo "Please install the GitHub CLI (https://cli.github.com) or follow Option B in README.md."; exit 1; }

gh auth status >/dev/null 2>&1 || gh auth login

[ -d .git ] || git init -q
git add .
git commit -q -m "Hodhodi Mobile Flashcards" || true
git branch -M main

if gh repo view "$USER_NAME/$REPO" >/dev/null 2>&1; then
  git remote get-url origin >/dev/null 2>&1 || git remote add origin "https://github.com/$USER_NAME/$REPO.git"
  git push -u origin main
else
  gh repo create "$USER_NAME/$REPO" --public --source=. --remote=origin --push \
    --description "Free spaced-repetition flashcards (FSRS) that installs on iPhone and Android"
fi

gh api -X POST "repos/$USER_NAME/$REPO/pages" -f "source[branch]=main" -f "source[path]=/" >/dev/null 2>&1 || true

echo
echo "Done. Your app will be live in about a minute at:"
echo "  https://$USER_NAME.github.io/$REPO/"
