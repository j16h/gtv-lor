#!/usr/bin/env bash
# Link every gtv-lor skill into Claude Code's personal skills folder.
# Usage: ./install.sh            (all skills)
#        ./install.sh recommender (only the recommender workflow)
set -euo pipefail

root="$(cd "$(dirname "$0")" && pwd)"
target="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
mkdir -p "$target"

if [[ "${1:-}" == "recommender" ]]; then
  skills=(gtv-lor gtv-lor-eval gtv-lor-improve gtv-lor-polish gtv-lor-final)
else
  skills=()
  for d in "$root"/skills/*/; do skills+=("$(basename "$d")"); done
fi

for s in "${skills[@]}"; do
  ln -sfn "$root/skills/$s" "$target/$s"
  echo "linked /$s"
done
echo "Restart Claude Code, then type /gtv-lor to start."
