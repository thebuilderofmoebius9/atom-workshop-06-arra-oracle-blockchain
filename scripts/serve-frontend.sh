#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../frontend"
exec python3 -m http.server 8719 --bind 0.0.0.0
