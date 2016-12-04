#/usr/bin/env python

import sys

offsets = {
        'U': -3,
        'D': 3,
        'L': -1,
        'R': 1
}

for line in sys.stdin.read().split('\n'):
    if len(line) == 0:
        continue

    position = 5
    for command in line:
        position+= offsets[command]

        if command == 'U' and position < 1:
            position += 3
        elif command == 'D' and position > 9:
            position -= 3
        elif command == 'L' and position % 3 == 0:
            position += 1
        elif command == 'R' and position % 3 == 1:
            position -= 1
    print(position)
