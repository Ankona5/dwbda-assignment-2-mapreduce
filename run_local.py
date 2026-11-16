#!/usr/bin/env python3
"""Run the MapReduce job locally: map -> shuffle/sort -> reduce, for every CSV in data/."""
import glob
import subprocess
import sys
from collections import defaultdict

GRADES = ["S", "A", "B", "C", "D", "E", "F"]

mapped = ""
for path in sorted(glob.glob("data/*.csv")):
    with open(path) as f:
        mapped += subprocess.run([sys.executable, "mapper.py"], stdin=f,
                                 capture_output=True, text=True, check=True).stdout
shuffled = "".join(sorted(mapped.splitlines(keepends=True)))   # the shuffle/sort phase
reduced = subprocess.run([sys.executable, "reducer.py"], input=shuffled,
                         capture_output=True, text=True, check=True).stdout

table = defaultdict(dict)
for line in reduced.splitlines():
    key, count = line.split("\t")
    subject, grade = key.split("|")
    table[subject][grade] = int(count)

print(f"{'Subject':<10}" + "".join(f"{g:>5}" for g in GRADES) + f"{'Total':>7}")
for subject, counts in sorted(table.items()):
    row = [counts.get(g, 0) for g in GRADES]
    print(f"{subject:<10}" + "".join(f"{c:>5}" for c in row) + f"{sum(row):>7}")
