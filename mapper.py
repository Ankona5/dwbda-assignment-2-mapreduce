#!/usr/bin/env python3
"""Map step: read 'subject,grade' lines, emit '<subject>|<grade>\t1'."""
import sys

VALID = {"S", "A", "B", "C", "D", "E", "F"}

for line in sys.stdin:
    parts = line.strip().split(",")
    if len(parts) != 2 or parts[0] == "subject":
        continue
    subject, grade = parts[0].strip(), parts[1].strip().upper()
    if grade in VALID:          # 'I' (absent) is not a grade category
        print(f"{subject}|{grade}\t1")
