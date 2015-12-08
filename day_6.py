"""
whitney champion
advent of code
"""

import sys
import numpy
import re

# day 6: probably a fire hazard

def day6part1():

	lights = [[False]*1000 for i in range(1000)]

	with open('day_6') as f:
	    for line in f:

			# get directions
			direction = re.findall(r'turn on|turn off|toggle', line)[0]

			# get start/end coordinates
			coordinates = re.findall(r'\d+', line)
			startx = int(coordinates[0])
			starty = int(coordinates[1])
			endx = int(coordinates[2])
			endy = int(coordinates[3])

			# turn lights on or off
			for x in range(startx, endx + 1):
				for y in range(starty, endy + 1):

					# get current status of light
					status = lights[x][y]

					# toggle
					if direction == "toggle":
						if status is True:
							lights[x][y] = False
						else:
							lights[x][y] = True

					# or turn on or off
					elif direction == "turn on":
						lights[x][y] = True
					elif direction == "turn off":
						lights[x][y] = False

	lit = 0
	x = 0
	y = 0

	# count lit stars
	for x in range(0, 1000):
		for y in range(0, 1000):
			status = lights[x][y]
			if status is True:
				lit += 1

	return lit

print(day6part1())
