#!/usr/bin/env bash

pip install python-semantic-release==9.12.0 twine keyring==24.3.1
git config user.name botcerts
git config user.email botcerts@learningmachine.com
git checkout master
semantic-release -vv version
source ./release_package.sh
