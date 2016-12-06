#!/usr/bin/env python

import sys
import hashlib

codes = sys.stdin.read().split('\n')

hist = [dict() for i in range(len(codes[0]))]

for code in codes:
    for pos, letter in enumerate(code):
        if letter in hist[pos]:
            hist[pos][letter] += 1
        else:
            hist[pos][letter] = 1

code = ''

for h in hist:
    code += sorted(list(h.iteritems()), key=lambda x : x[1])[0][0]

print(code)
