#!/bin/bash

if [ -z "$@" ]; then
  echo "Missing SSH target"
  exit 1
fi

DIR=`basename "$PWD"`
cd .. && \
  tar --exclude='node_modules' \
    --exclude='dist' \
    --exclude='.git' \
    -zcv "$DIR" | ssh "$@" "tar -xz && (cd "$DIR" && docker-compose up --build -d)"
