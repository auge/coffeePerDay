#!/usr/bin/env bash

find "$1" -type f -name "*.csv" | parallel -j 8 --bar ./$2 -k -f {} | ./summarizeFile.py

