"""
whitney champion
advent of code
"""

import sys
import functools

# day 7: some assembly required

def day7(day):

	circuit = {}

	# open file and get lines
	instructions = open("day_07", "r").read().splitlines()

	# split up values
	for line in instructions:
		command, gate = line.split(" -> ")
		circuit[gate.strip()] = command

	@functools.lru_cache()
	def calc(gate):

		# if already a number, return
		try:
			return int(gate)
		except ValueError:
			pass

		# otherwise, split up operation
		command = circuit[gate].split(" ")

		# get command, apply operation
		if "NOT" in command:
			return ~calc(command[1])
		if "AND" in command:
			return calc(command[0]) & calc(command[2])
		elif "OR" in command:
			return calc(command[0]) | calc(command[2])
		elif "LSHIFT" in command:
			return calc(command[0]) << calc(command[2])
		elif "RSHIFT" in command:
			return calc(command[0]) >> calc(command[2])
		else:
			return calc(command[0])

	if day is 1:
		calc.cache_clear()
		return calc("a")
	else:
		circuit["b"] = str(calc("a"))
		calc.cache_clear()
		return calc("a")

print(day7(1))
print(day7(2))
