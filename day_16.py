"""
whitney champion
advent of code
"""

import sys
import re

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

print(day16(1))
print(day16(2))
