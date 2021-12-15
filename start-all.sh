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

pushd web/the-loggers/
docker-compose up -d
popd

pushd web/swag/
docker-compose up -d
popd

pushd web/h0h0h0-js/
docker-compose up -d
popd
