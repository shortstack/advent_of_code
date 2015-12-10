"""
whitney champion
advent of code
"""

import sys
import hashlib
import re

# day 4: the ideal stocking stuffer

def day4part1():

	key = "ckczppom"
	matching = False

	# start at 1
	num = 1

	while not matching:

		# get hash of key and number
		hash = hashlib.md5(key + str(num)).hexdigest()

		# regex check for '00000'
		match = re.match(r'00000',hash, re.M|re.I)

		# if it's a match, make matching True to stop loop
		if str(match) != "None":
			matching = True

		# increment num
		num += 1

	# return correct number
	return num-1

def day4part2():

	key = "ckczppom"
	matching = False

	# start at 1
	num = 1

	while not matching:

		# get hash of key and number
		hash = hashlib.md5(key + str(num)).hexdigest()

		# regex check for '000000'
		match = re.match(r'000000',hash, re.M|re.I)

		# if it's a match, make matching True to stop loop
		if str(match) != "None":
			matching = True

		# increment num
		num += 1

	# return correct number
	return num-1

print(day4part1())
print(day4part2())
