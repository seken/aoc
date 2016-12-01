#!/usr/bin/env python

import sys

commands = sys.stdin.read()

level = 0

for command in commands:
	if command == '(':
		level += 1
	else:
		level -= 1

print level
