"""
whitney champion
advent of code
"""

import sys
import re
import hashlib

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

def day6part2():

	lights = [[0]*1000 for i in range(1000)]

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
						lights[x][y] += 2

					# or turn on or off
					elif direction == "turn on":
						lights[x][y] += 1
					elif direction == "turn off":
						if lights[x][y] > 0:
							lights[x][y] -= 1

	lit = 0
	x = 0
	y = 0

	# count lit stars
	for x in range(0, 1000):
		for y in range(0, 1000):
			lit += lights[x][y]

	return lit

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

print(day1part1())
print(day1part2())
print(day2part1())
print(day2part2())
print(day3part1())
print(day3part2())
print(day4part1())
print(day4part2())
print(day5part1())
print(day5part2())
print(day6part1())
print(day6part2())
print(day8part1())
print(day8part2())
