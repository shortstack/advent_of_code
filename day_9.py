"""
whitney champion
advent of code
"""

import sys
import re
import itertools
from itertools import izip, islice

# day 9: all in a single night

def day9part1():

	distances = {}

	# get all possible routes
	locations = ["Arbre","Tambi","Norrath","Tristram","Straylight","Faerun","AlphaCentauri","Snowdin"]
	routes = list(itertools.permutations(locations))

	# iterate through routes to search for distance
	for route in routes:

		distance = 0

		# get hop and next hop
		for hop, nextHop in izip(route, islice(route, 1, None)):

			# read through file and find distance for that connection
			with open('day_9') as file:
				for num, line in enumerate(file, 1):
					if hop in line and nextHop in line:

						# add distance to total route distance
						distance += int(line.split(" = ")[1].strip())

		# add distance with route to dictionary
		distances[route] = distance

	# find shortest total distance in dictionary
  	return distances[min(distances, key=distances.get)]

print(day9part1())
