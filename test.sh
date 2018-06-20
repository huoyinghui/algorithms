#!/usr/bin/env bash

# pip install when-changed
 when-changed -v -r -1 -s ./    "py.test -s $1"
