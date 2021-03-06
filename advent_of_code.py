"""
whitney champion
advent of code
"""

import sys
import re
import hashlib
import itertools
import json
import collections
from itertools import izip, tee, chain, islice, groupby

# day 1: not quite lisp

def day1part1():
	f = open('day_01', 'r')
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
	f = open('day_01', 'r')
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

	with open('day_02') as f:
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

	with open('day_02') as f:
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

	f = open('day_03', 'r')
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

	f = open('day_03', 'r')
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

	with open('day_05') as f:
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

	with open('day_05') as f:
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

	with open('day_06') as f:
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

	with open('day_06') as f:
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

# day 8: matchsticks

def day8part1():

	literal_count = 0
	mem_count = 0

	with open('day_08') as f:
		for line in f:

			# number of characters of code for string literals
			literal_count += len(line[:-1])

			# number of characters in memory for the values of the strings
			mem_count += len(eval(line))

	return literal_count - mem_count

def day8part2():

	new_count = 0

	with open('day_08') as f:
		for line in f:

			# get difference in escape count
			newline = line[:-1]
			slashes = newline.count("\\")
			quotes = newline.count("\"")
			new_count += slashes + quotes + 2

	return new_count

# day 9: all in a single night

def day9(option):

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
			with open('day_09') as file:
				for num, line in enumerate(file, 1):
					if hop in line and nextHop in line:

						# add distance to total route distance
						distance += int(line.split(" = ")[1].strip())

		# add distance with route to dictionary
		distances[route] = distance

	# find shortest total distance in dictionary
	if option == "min":
  		return distances[min(distances, key=distances.get)]
	else:
  		return distances[max(distances, key=distances.get)]

# day 10: elves look, elves say

def day10(repeat):

    input = "1321131112"

    for i in range(repeat):

        new_input = ""
        for num, count in groupby(input):
            new_input += str(len(list(count))) + str(num)

        input = new_input

    return len(input)

# day 11: corporate policy

def day11(input):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def increment(password):

        # increment with next letter
        try:
            return password[0:-1] + alphabet[alphabet.index(password[-1]) + 1]
        except IndexError:
            return increment(password[0:-1]) + 'a'

    def validate(password):

        # check for bad characters
        if all(char in password for char in ("i","l","o")):
            return False

        # check for 3-in-a-row
        for x in range(0, len(password)-2):
            if ord(password[x]) == ord(password[x+1]) - 1 and ord(password[x+1]) == ord(password[x+2]) - 1:
                break
        else:
            return False

        # check for repeat characters
        if len(re.findall(r'(.)\1+', password)) < 2:
            return False

        return True

    while True:

        input = increment(input)
        if validate(input):
            break

    return input

# day 12: JSAbacusFramework.io

def day12(day):

    file = open('day_12','r').read()

    # get all the numbers from the file
    numbers = re.findall(r'-?[0-9]+', file)

    # convert strings to ints
    int_numbers = [int(numeric_string) for numeric_string in numbers]

    # get all {} objects without "red" from the file
    def is_red(object):
        if "red" in object.values():
            return {}
        else:
            return object
    objects = str(json.loads(file, object_hook=is_red))

    if day is 2:
        # return sum of objects not containing 'red':
        return sum(map(int, re.findall("-?[0-9]+", objects)))
    # else return total sum
    return sum(int_numbers)

# day 13: knights of the dinner table

def day13(day):

    total_happiness = {}

    # func to get previous and next values in list of attendees
    def previous_and_next(seating):
        prevs, items, nexts = tee(seating, 3)
        prevs = chain([None], prevs)
        nexts = chain(islice(nexts, 1, None), [None])
        return izip(prevs, items, nexts)

    if day is 1:
        # open the file
        the_list = open('day_13', 'r').read().splitlines()

        # get all possible names
        names = ["Alice","Bob","Carol","David","Eric","Frank","George","Mallory"]
    else:
        # open the file
        the_list = open('day_13_whitney', 'r').read().splitlines()

        # get all possible names
        names = ["Alice","Bob","Carol","David","Eric","Frank","George","Mallory","Whitney"]

    # get all possible seating arrangements
    arrangements = list(itertools.permutations(names))

    # iterate through routes to search for distance
    for seating in arrangements:

        happiness = 0

        # get left and right
        for left, person, right in previous_and_next(seating):

            # if at end of seating list, loop around
            if str(left) == "None":
                left = seating[len(seating)-1]
            if str(right) == "None":
                right = seating[0]

            # read through file and find happiness for each seating arrangement
            for line in the_list:

                # only check happiness for that person
                if line.split(" ")[0] == person:
                    if left in line or right in line:

                        # add happiness to total happiness
                        operation = line.split(" ")[2]
                        if operation == "gain":
                          happiness += int(line.split(" ")[3])
                        else:
                          happiness -= int(line.split(" ")[3])

            # add happiness to dictionary
            total_happiness[seating] = happiness

    return total_happiness[max(total_happiness, key=total_happiness.get)]

def day14part1(seconds):

    reindeer = {}

    # open the file
    file = open('day_14', 'r').read().splitlines()

    # get all reindeer & stats
    for i in file:
        name = i.split(" ")[0]
        speed = int(i.split(" ")[3])
        time = int(i.split(" ")[6])
        rest = int(i.split(" ")[13])

        # figure out how many times the reindeer can fly/rest in that time frame
        count = seconds / (time + rest)

        # get leftover seconds
        mod = seconds % (time + rest)

        # get distance for total flying time
        distance = (speed * time) * count

        # get leftover time and figure out of it's rest or flying, get add to final distance
        if mod > time:
            distance += speed * time
        else:
            distance += speed * mod

        reindeer[name] = distance

    return reindeer[max(reindeer, key=reindeer.get)]

def day14part2(seconds):

    reindeer = {}
    distances = {}
    points = {}
    history = collections.defaultdict(int)

    # open the file
    file = open('day_14', 'r').read().splitlines()

    # get all reindeer and stats
    for i in file:

        name = i.split(" ")[0]
        speed = int(i.split(" ")[3])
        time = int(i.split(" ")[6])
        rest = int(i.split(" ")[13])
        reindeer[name] = (speed,time,rest)

    distance = 0
    points = 0
    x = 0

    for i in reindeer:

        # get distance for each cycle of flying/rest
        distance = itertools.cycle([int(reindeer[i][0])]*int(reindeer[i][1]) + [0]*int(reindeer[i][2]))

        # get distance of all cycles 2503 seconds
        history[i] = list(itertools.accumulate(next(distance) for _ in range(seconds)))

    # get all points per second
    pps = [i for score in zip(*history.values()) for i, v in enumerate(score) if v==max(score)]

    # accumulated points per second per reindeer
    totals = collections.Counter(pps).values()

    # max points
    points = max(totals)

    return points

# day 15: science for hungry people

def day15(day):

    ingredients = []

    file = open('day_15','r').read().splitlines()
    for line in file:
        # get ingredient and properties
        ingredients.append(map(int,re.findall(r'-?[0-9]+', line)))

    scores = []
    score = 0
    total = 0

    for x in range(0,100):
        for y in range(0,100-x):
            for z in range(0,100-x-y):

                # must add up to 100
                r = 100 - x - y - z

                # get values for all properties
                capacity = ingredients[0][0]*x + ingredients[1][0]*y + ingredients[2][0]*z + ingredients[3][0]*r
                durability = ingredients[0][1]*x + ingredients[1][1]*y + ingredients[2][1]*z + ingredients[3][1]*r
                flavor = ingredients[0][2]*x + ingredients[1][2]*y + ingredients[2][2]*z + ingredients[3][2]*r
                texture = ingredients[0][3]*x + ingredients[1][3]*y + ingredients[2][3]*z + ingredients[3][3]*r
                calories = ingredients[0][4]*x + ingredients[1][4]*y + ingredients[2][4]*z + ingredients[3][4]*r

                if day is 1:
                    # calculate score
                    if (capacity <= 0 or durability <= 0 or flavor <= 0 or texture <= 0):
                        score = 0
                    else:
                        score = capacity * durability * flavor * texture
                else:

                    if calories == 500:
                        # calculate score
                        if (capacity <= 0 or durability <= 0 or flavor <= 0 or texture <= 0):
                            score = 0
                        else:
                            score = capacity * durability * flavor * texture

                # add scores to array of scores
                scores.append(score)

    # get highest score
    return max(scores)

# day 16: aunt sue

def day16(day):

    sues = []
    clues = (('children', 3), ('cats', 7), ('samoyeds', 2), ('pomeranians', 3), ('akitas', 0), ('vizslas', 0), ('goldfish', 5), ('trees', 3), ('cars', 2), ('perfumes', 1))

    file = open('day_16','r').read().splitlines()
    for line in file:

        # get all of sue's items
        sue = line.split(" ")
        sue = (sue[1][0:-1], (sue[2][0:-1],int(sue[3][0:-1])), (sue[4][0:-1],int(sue[5][0:-1])), (sue[6][0:-1],int(sue[7])))
        sues.append(sue)

        # skip first array value, just sue's ID number
        itersue = iter(sue)
        next(itersue)

        # iterate through list of sue's items and the clues
        match = 0
        for s in itersue:
            for clue in clues:
                sue_item = s[0]
                sue_count = s[1]
                clue_item = clue[0]
                clue_count = clue[1]

                # find items that match clues
                if day is 2:
                    if clue_item == "cats" or clue_item == "trees":
                        if sue_item == clue_item and sue_count > clue_count:
                            match += 1
                    elif clue_item == "pomeranians" or clue_item == "goldfish":
                        if sue_item == clue_item and sue_count < clue_count:
                            match += 1
                    else:
                        if sue_item == clue_item and sue_count == clue_count:
                            match += 1
                else:
                    if sue_item == clue_item and sue_count == clue_count:
                        match += 1

        # if all 3 match, that's sue
        if match is 3:
            return sue

# day 17: no such thing as too much

def day17(day):

    containers = []
    combinations = []
    combinations_min = []

    file = open('day_17','r').read().splitlines()
    for line in file:

        # get all numbers from puzzle input into array
        containers.append(int(line))

    # iterate through list, find all combinations that sum 150
    count = 0
    for i in range(0, len(containers)+1):
        for subset in itertools.combinations(containers, i):
            if sum(subset) is 150:

                combinations.append(subset)

    # get length of new list
    if day is 1:
        return len(combinations)
    else:
        # iterate through list, find all 4 number combinations that sum 150
        count = 0
        for i in range(0, len(containers)+1):
            for subset in itertools.combinations(containers, i):
                if sum(subset) is 150 and len(subset) is 4:

                    combinations_min.append(subset)

        return len(combinations_min)

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
print(day7(1))
print(day7(2))
print(day8part1())
print(day8part2())
print(day9("min"))
print(day9("max"))
print(day10(40))
print(day10(50))
print(day11("hepxcrrq"))
print(day11(day11("hepxcrrq")))
print(day12(1))
print(day12(2))
print(day13(1))
print(day13(2))
print(day14part1(2503))
print(day14part2(2503))
print(day15(1))
print(day15(2))
print(day16(1))
print(day16(2))
print(day17(1))
print(day17(2))
