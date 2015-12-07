"""
whitney champion
advent of code
"""

import sys

# day 2: i was told there would be no math

def day2part1():

	total = 0

	with open('day_2') as f:
	    for line in f:

			# get dimensions
			l = int(line.split('x')[0])
			w = int(line.split('x')[1])
			h = int(line.split('x')[2])

			# get smallest side
			sides = [l*w,w*h,h*l]
			smallest = min(sides)

			# get area
			a = 2*l*w + 2*w*h + 2*h*l

			# get surface area
			sa = a + smallest

			# add to total
			total += sa

	# print total
	return total

def day2part2():

	total = 0

	with open('day_2') as f:
	    for line in f:

			# get dimensions
			l = int(line.split('x')[0])
			w = int(line.split('x')[1])
			h = int(line.split('x')[2])

			# get smallest side
			sides = [l,w,h]
			one = sorted(sides)[0]
			two = sorted(sides)[1]

			# get bow
			bow = l*w*h

			# get area
			a = one+one+two+two+bow

			# get total
			total += a

	# print area
	return total

print(day2part1())
print(day2part2())
