#!/usr/bin/env python

import sys
import hashlib

door_id = sys.stdin.read().strip()

index = 0
found = 0

password = ['?', '?', '?', '?', '?', '?','?','?']
while found != 8:
    h = hashlib.md5()
    h.update(door_id + str(index))
    index += 1
    output = h.hexdigest()[:7]
    if output[:5] == '00000':
        position = int(output[5], 16)
        if position < len(password) and password[position] == '?':
            password[position] = output[6]
            found += 1
            print(''.join(password))

print(''.join(password))

