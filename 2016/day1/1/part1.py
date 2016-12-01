#!/usr/bin/env python

import sys

commands = sys.stdin.read().split(', ')

d = [
	(1, 0),
	(0, 1),
	(-1, 0),
	(0, -1)
]
direction = (1, 0)

position = (0, 0)

for command in commands:
	if command[0] == 'R':
		direction = (-direction[1], direction[0])
	else:
		direction = (direction[1], -direction[0])

	distance = int(command[1:])
	position = (position[0] + direction[0]*distance, position[1] + direction[1]*distance)

print direction
print position
print abs(position[0]) + abs(position[1])
