#!/usr/bin/env bash
# Link the gtv-lor skills into Claude Code or Codex.
#
#   ./install.sh                     all skills, Claude Code (~/.claude/skills)
#   ./install.sh recommender         only the referee path (A)
#   ./install.sh codex               all skills, Codex (~/.codex/skills)
#   ./install.sh codex recommender   only path A, Codex
set -euo pipefail

root="$(cd "$(dirname "$0")" && pwd)"
target="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
app="Claude Code"
set_only=""
for arg in "$@"; do
  case "$arg" in
    codex) target="${CODEX_HOME:-$HOME/.codex}/skills"; app="Codex" ;;
    claude) ;;
    recommender) set_only="recommender" ;;
    *) echo "unknown option: $arg" >&2; exit 1 ;;
  esac
done
mkdir -p "$target"

if [[ "$set_only" == "recommender" ]]; then
  skills=(gtv-lor gtv-lor-eval gtv-lor-improve gtv-lor-polish gtv-lor-final)
else
  skills=()
  for d in "$root"/skills/*/; do skills+=("$(basename "$d")"); done
fi

for s in "${skills[@]}"; do
  ln -sfn "$root/skills/$s" "$target/$s"
  echo "linked $s -> $target/$s"
done
if [[ "$app" == "Codex" ]]; then hint='$gtv-lor'; else hint='/gtv-lor'; fi
echo "Done. Restart $app, then type $hint to start."
