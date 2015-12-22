"""
whitney champion
advent of code
"""

import sys
import re
from collections import defaultdict

# day 20: infinite elves and infinite houses

def day20part1():

	num = 29000000

	houses = defaultdict(int)

	for elf in xrange(1,num):
		for house in xrange(elf, 10000000, elf):
			houses[house] += elf * 10

		if houses[elf] >= num:
			return elf

def day20part2():

	num = 29000000

	houses = defaultdict(int)

	for elf in xrange(1,num):
		for house in xrange(elf, min(elf*50+1,10000000), elf):
			houses[house] += elf * 11

		if houses[elf] >= num:
			return elf

#print(day20part1())
print(day20part2())
