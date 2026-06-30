#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PORT="${QUARTO_PREVIEW_PORT:-4200}"
export XDG_CACHE_HOME="${ROOT_DIR}/.cache"

if command -v quarto >/dev/null 2>&1; then
  QUARTO_BIN="quarto"
elif [ -x "/home/apex/snap/code/235/.local/bin/quarto" ]; then
  QUARTO_BIN="/home/apex/snap/code/235/.local/bin/quarto"
else
  QUARTO_BIN="$(find /home/apex/snap/code -path '*/.local/share/uv/tools/quarto-cli/lib/python*/site-packages/quarto_cli/bin/quarto' -type f -perm -111 2>/dev/null | sort -V | tail -n 1 || true)"
  if [ -z "${QUARTO_BIN}" ]; then
    echo "Could not find quarto. Run: uv tool install quarto-cli" >&2
    exit 1
  fi
fi

cd "${ROOT_DIR}"

if command -v ss >/dev/null 2>&1; then
  if ss -ltn "sport = :${PORT}" 2>/dev/null | grep -q LISTEN; then
    echo "Port ${PORT} is already in use."
    echo "If this is your Quarto preview, open: http://localhost:${PORT}/"
    echo "To use a different port: QUARTO_PREVIEW_PORT=4201 scripts/preview.sh"
    exit 0
  fi
fi

"${QUARTO_BIN}" preview --render all --port "${PORT}"
