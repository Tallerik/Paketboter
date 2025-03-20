#!/bin/bash
DIRECTORY=".venv"

if [ -d "$DIRECTORY" ]; then
  echo "Already exists. Enable with source .venv/bin/activate"
else
  echo "$DIRECTORY does not exist."
  python3 -m venv --system-site-packages .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  echo "Created. Enable with source .venv/bin/activate"
fi