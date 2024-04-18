#!/usr/bin/env bash

docker compose run --rm \
    --entrypoint "/bin/sh -c" app \
    "
    flake8 . --exclude=venv
    "
