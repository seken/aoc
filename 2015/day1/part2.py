#!/usr/bin/env python

import sys

commands = sys.stdin.read()

level = 0

for i, command in enumerate(commands):
	if command == '(':
		level += 1
	else:
		level -= 1

	if level == -1:
		print(i+1)
		sys.exit(0)

