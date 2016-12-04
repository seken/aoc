#!/usr/bin/env python

import re
import sys

possible = 0

def gen(i):
    a = []
    b = []
    c = []
    for line in i:
        num =  [int(side) for side in re.split(r' *', line) if len(side) > 0]
        if len(num) == 0:
            continue
        a.append(num[0])
        b.append(num[1])
        c.append(num[2])

        if len(a) == 3:
            yield a
            yield b
            yield c
            a = []
            b = []
            c = []

for sides in gen(sys.stdin.read().split('\n')):
    if sum(sides) > max(sides)*2:
        possible += 1

print(possible)
