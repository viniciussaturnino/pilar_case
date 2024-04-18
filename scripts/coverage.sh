#!/usr/bin/env bash

docker compose run --rm \
    --entrypoint "/bin/sh -c" app \
    "
    coverage erase && \
    coverage run -m pytest && \
    coverage xml && \
    coverage html
    "
