#!/usr/bin/env python

import re
import sys

sector_sum = 0

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
        sector_sum += int(sector)

print(sector_sum)
