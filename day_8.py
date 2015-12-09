"""
whitney champion
advent of code
"""

import sys
import re

# day 8: matchsticks

def day8part1():

	literal_count = 0
	mem_count = 0

	with open('day_8') as f:
		for line in f:

			# number of characters of code for string literals
			literal_count += len(line[:-1])

			# number of characters in memory for the values of the strings
			mem_count += len(eval(line))

	return literal_count - mem_count

def day8part2():

	new_count = 0

	with open('day_8') as f:
		for line in f:

			# get difference in escape count
			newline = line[:-1]
			slashes = newline.count("\\")
			quotes = newline.count("\"")
			new_count += slashes + quotes + 2

	return new_count

print(day8part1())
print(day8part2())
