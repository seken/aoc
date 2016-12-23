#!/usr/bin/env python

import sys

discs = []
lowest = -1
low = 0
off_by = 0

num = -1

for d in sys.stdin.read().split('\n'):
    if len(d) == 0:
        continue

    d = d.split(' ')
    number = int(d[1][1:])
    positions = int(d[3])
    time = int(d[6].split('=')[1][:-1])
    position = int(d[11][:-1])

    if positions > low:
        lowest = number
        low = positions
        off_by = positions - ((number + position) % positions)

    num = max(num, number)
    discs.append((number, positions, time, position))

discs.append((num+1, 11, 0, 0))

def aligned(discs):
    aligned = True
    for disc in discs:
        number, positions, time, position = disc
        if (position + number) % positions != 0:
            aligned = False
            break
    return aligned

t = 0

def increment(discs, i):
    return [(number, positions, time+i, (position+i) % positions) for number, positions, time, position in discs]

print(lowest, off_by)

if not aligned(discs):
    discs = increment(discs, off_by)
print(discs)

while not aligned(discs):
    discs = increment(discs, low)
    t+= 1

print(discs)
