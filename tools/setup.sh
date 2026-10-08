#!/bin/sh
# One-time setup on a new machine: creates .venv with the dependencies, then
# downloads the large files that can be fetched automatically.
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
python3 -m venv .venv
.venv/bin/pip install -q -r requirements.txt
./pq adapters
./pq fetch
./pq build
echo "Prêt. Ouvrir le site : ./pq view"
