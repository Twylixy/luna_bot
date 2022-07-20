#!/bin/sh

echo "Starting app..."
python3 -m app

exec "$@"