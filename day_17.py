"""
whitney champion
advent of code
"""

import sys
import re
import itertools

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

print(day17(1))
print(day17(2))
