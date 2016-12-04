#!/usr/bin/env python

import re
import sys
import string
from string import ascii_lowercase as lc, ascii_uppercase as uc

def rot_alpha(n):
    lookup = string.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)

for line in sys.stdin.read().split('\n'):
    if len(line) == 0:
        continue

    d = {}

    segments = line.split('-')
    sector = segments[-1].split('[')[0]
    checksum = segments[-1].split('[')[1].split(']')[0]

    segments = ''.join(segments[:-1])

    for piece in segments:
        if piece in d:
            d[piece] += 1
        else:
            d[piece] = 1

    actual = ''.join([i[0] for i in sorted(list(d.iteritems()), key=lambda x : x[1]*1000 + 500 - ord(x[0]), reverse=True)])
    actual = actual[:5]

    if checksum == actual:
        print(rot_alpha(int(sector)%26)(segments))
        print(sector)

