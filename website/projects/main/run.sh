#!/usr/bin/env bash

set -e # Exit immediately on error
mkdir -p build/binary
cmake -GNinja -S . -B build/binary
cmake --build build/binary
python test.py
