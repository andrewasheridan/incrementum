#!/bin/bash

# - starts Litestar application

set -o errexit
set -o pipefail
set -o nounset

echo Starting Litestar App...
gunicorn app.incrementum_api.main:app --config app/incrementum_api/settings/_gunicorn_config.py
