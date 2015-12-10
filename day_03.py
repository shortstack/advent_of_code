"""
whitney champion
advent of code
"""

import sys

# day 3: perfectly spherical houses in a vacuum

def day3part1():

	x = 0
	y = 0

	# create list
	houses = []
	houses.append((0,0))

	f = open('day_3', 'r')
	while True:
		ch = f.read(1)

		# increment/decrement position
		if ch == '^':
			y += 1
		elif ch == 'v':
			y -= 1
		elif ch == '<':
			x -= 1
		elif ch == '>':
			x += 1

		# update list
		houses.append((x,y))

		if not ch:
			break

	# return totals
	return len(set(houses))

def day3part2():

	x0 = 0
	y0 = 0
	x1 = 0
	y1 = 0

	# create santa's list
	houses_santa = []
	houses_santa.append((0,0))

	# create robo-santa's list
	houses_robo = []
	houses_robo.append((0,0))

	# counter
	count = 0

	f = open('day_3', 'r')
	while True:
		ch = f.read(1)

		if count is 0:

			# increment/decrement position
			if ch == '^':
				y0 += 1
			elif ch == 'v':
				y0 -= 1
			elif ch == '<':
				x0 -= 1
			elif ch == '>':
				x0 += 1

			# update list for santa or robo-santa
			houses_santa.append((x0,y0))

			# increment counter
			count += 1

		else:

			# increment/decrement position
			if ch == '^':
				y1 += 1
			elif ch == 'v':
				y1 -= 1
			elif ch == '<':
				x1 -= 1
			elif ch == '>':
				x1 += 1

			# update list for santa or robo-santa
			houses_robo.append((x1,y1))

			# decrement counter
			count -= 1

		if not ch:
			break

	# get totals
	houses_all = houses_santa + houses_robo
	return len(set(houses_all))

print(day3part1())
print(day3part2())
