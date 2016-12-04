#!/usr/bin/env python

import re
import sys

possible = 0

for line in sys.stdin.read().split('\n'):
    if len(line) == 0:
        continue

    sides = [int(side) for side in re.split(r' *', line) if len(side) > 0]

    if sum(sides) > max(sides)*2:
        possible += 1

print(possible)
