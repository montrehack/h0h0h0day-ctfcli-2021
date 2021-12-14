#!/bin/bash

DIR=`basename "$PWD"`
cd .. && \
  tar --exclude='node_modules' \
    --exclude='dist' \
    --exclude='.git' \
    -zcv "$DIR" \
    -f "$DIR/$DIR.tgz"
