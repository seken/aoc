#/usr/bin/env python

import sys

offsets = {
        'U': -5,
        'D': 5,
        'L': -1,
        'R': 1
}

position = 9

m = [
    0, 0, 1, 0, 0,
    0, 2, 3, 4, 0,
    5, 6, 7, 8, 9,
    0, 'A', 'B', 'C', 0,
    0, 0, 'D', 0, 0
]

for line in sys.stdin.read().split('\n'):
    if len(line) == 0:
        continue

    for command in line:
        new_position = position + offsets[command]
        if new_position < 0 or new_position >= len(m):
            continue
        elif m[new_position] == 0:
            continue

        position+= offsets[command]

        if command == 'U' and position < 0:
            position += 5
        elif command == 'D' and position >= len(m):
            position -= 5
        elif command == 'L' and position % 5 == 4:
            position += 1
        elif command == 'R' and position % 5 == 0:
            position -= 1

    print(m[position])
