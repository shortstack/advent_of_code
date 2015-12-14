"""
whitney champion
advent of code
"""

import sys
import re
import itertools
from itertools import izip, tee, chain, islice

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

print(day13(1))
print(day13(2))
