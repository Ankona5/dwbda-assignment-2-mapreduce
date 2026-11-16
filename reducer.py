#!/usr/bin/env python3
"""Reduce step: input is sorted by key; sum the counts per '<subject>|<grade>'."""
import sys

current, total = None, 0
for line in sys.stdin:
    key, value = line.rstrip("\n").split("\t")
    if key == current:
        total += int(value)
    else:
        if current is not None:
            print(f"{current}\t{total}")
        current, total = key, int(value)
if current is not None:
    print(f"{current}\t{total}")
