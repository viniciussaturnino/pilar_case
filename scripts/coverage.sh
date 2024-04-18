#!/usr/bin/env bash

docker compose run --rm \
    --entrypoint "/bin/sh -c" web \
    "
    coverage erase && \
    coverage run -m pytest && \
    coverage combine && \
    coverage report -m && \
    coverage xml && \
    coverage html
    "
