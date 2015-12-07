"""
whitney champion
advent of code
"""

import sys
import re

# day 5: doesn't he have intern-elves for this?

def day5part1():

	total = 0

	vowels = set("AEIOUaeiou")
	bad_strings = ("ab", "cd", "pq", "xy")

	with open('day_5') as f:
	    for line in f:

			nice = True

			# match double char
			match_double = re.search(r'(.)\1', line)
			if str(match_double) == "None":
				nice = False

			# count vowels
			num_vowels = len(filter(lambda x: x in vowels, line))
			if num_vowels < 3:
				nice = False

			# check for bad strings
			if any(substring in line for substring in bad_strings):
				nice = False

			if nice is True:
				total += 1

	# print total
	return total

def day5part2():

	total = 0

	with open('day_5') as f:
	    for line in f:

			test_one = False
			test_two = False

			# matching set
			for substring in range(0, len(line), 1):

				# get first pair of letters
				pair = line[substring:substring+2]

				# check if pair exists elsewhere in string
				match_substring = re.search(r"%s(.*)%s" % (pair, pair), line)

				# if there's a match, break loop, string is nice
				if str(match_substring) != "None":
					test_one = True
					break

			# match between characters
			for char in line:

				# check each line for character in between matching characters
				match_between = re.search(r"%s[a-zA-Z0-9_]%s" % (char, char), line)

				# if letter is sandwiched, break loop, string is nice
				if str(match_between) != "None":
					test_two = True
					break

			# if both tests pass, string is nice, increment total number of nice strings
			if test_one is True and test_two is True:
				total += 1

	# print total
	return total

print(day5part1())
print(day5part2())
