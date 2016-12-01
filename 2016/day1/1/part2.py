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

visited = set()
visited.add(position)

for command in commands:
	if command[0] == 'R':
		direction = (-direction[1], direction[0])
	else:
		direction = (direction[1], -direction[0])

	distance = int(command[1:])
	for i in range(distance):
		position = (position[0] + direction[0], position[1] + direction[1])
		if position in visited:
			print(position)
			print abs(position[0]) + abs(position[1])
		visited.add(position)

print direction
print position
print abs(position[0]) + abs(position[1])
