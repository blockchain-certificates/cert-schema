#!/usr/bin/env bash

cd npm
npm ci
npm run copy:schemas
npm publish
pwd
ls
'if [ "$TRAVIS_PULL_REQUEST" = "false" ]; then sh ../scripts/automated-update-blockcerts.org.sh; fi' # if no changes (aka npm release), no commit then no PR
cd ..
