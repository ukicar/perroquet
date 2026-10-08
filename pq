#!/bin/sh
# Perroquet command-line tool. Usage: ./pq <command>   (./pq -h for the list)
ROOT="$(cd "$(dirname "$0")" && pwd)"
PY="$ROOT/.venv/bin/python"
[ -x "$PY" ] || PY=python3
PYTHONPATH="$ROOT/tools${PYTHONPATH:+:$PYTHONPATH}" exec "$PY" -m pq "$@"
