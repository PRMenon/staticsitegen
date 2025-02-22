#!/bin/bash

COMMIT=${1:-"Fixes and changes"}

git add .

git commit -m "$COMMIT"

## Assumes no branches
git push