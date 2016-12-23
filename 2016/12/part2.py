#!/usr/bin/env python

import sys

ref = {
        'a': 0,
        'b': 0,
        'c': 1,
        'd': 0
}

pc = 0

def is_reg(s):
    return s in ref.keys()

def reg_or_val(s):
    if is_reg(s):
        return ref[s]
    return int(s)

lines = sys.stdin.read().split('\n')

while pc < len(lines):
    line = lines[pc]

    if len(line) == 0:
        pc += 1
        continue

    s = line.split(' ')
    opcode = s[0]

    if opcode == 'cpy':
        x = s[1]
        y = s[2]
        ref[y] = reg_or_val(x)
    elif opcode =='inc':
        reg = s[1]
        ref[reg] += 1
    elif opcode == 'dec':
        reg = s[1]
        ref[reg] -= 1
    elif opcode == 'jnz':
        x = reg_or_val(s[1])
        y = reg_or_val(s[2])
        if x != 0:
            pc += y
            continue
    pc += 1


print(ref['a'])
