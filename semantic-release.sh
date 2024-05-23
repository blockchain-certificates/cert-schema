#!/usr/bin/env bash

pip install python-semantic-release twine==5.0.0
git config user.name botcerts
git config user.email botcerts@learningmachine.com
git checkout master
semantic-release version
