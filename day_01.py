"""
whitney champion
advent of code
"""

import sys

# day 1: not quite lisp

def day1part1():
	f = open('day_1', 'r')
	count = 0
	while True:
		ch = f.read(1)
		if ch == ')':
			count -= 1
		elif ch == '(':
			count += 1
		if not ch:
			break
	return str(count)

def day1part2():
	f = open('day_1', 'r')
	count = 0
	position = 0
	while True:
		ch = f.read(1)
		position += 1
		if ch == ')':
			count -= 1
		elif ch == '(':
			count += 1
		if count < 0:
			break
	return str(position)

print(day1part1())
print(day1part2())
