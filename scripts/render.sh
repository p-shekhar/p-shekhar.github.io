#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
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
"${QUARTO_BIN}" render --cache-refresh
