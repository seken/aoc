#!/usr/bin/env python

import sys
import hashlib

door_id = sys.stdin.read().strip()

index = 0

password = ''
while len(password) != 8:
    h = hashlib.md5()
    h.update(door_id + str(index))
    index += 1
    output = h.hexdigest()[:6]
    if output[:5] == '00000':
        password += output[5]
        print(password)

print(password)
    
