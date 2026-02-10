#!/usr/bin/env bash
# start.sh
set -o errexit

# Run Gunicorn with Uvicorn worker
python -m gunicorn grocerymate.asgi:application -k uvicorn.workers.UvicornWorker
