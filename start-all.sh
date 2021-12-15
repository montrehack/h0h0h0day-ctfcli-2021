#!/bin/bash

pushd web/santacheck/
docker-compose up -d
popd

pushd web/h0h0hopa/
docker-compose up -d
popd

pushd pwn/ho-ho-hosh-infra/
docker-compose up -d
popd
