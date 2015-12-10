"""
whitney champion
advent of code
"""

import sys
import re
import itertools
from itertools import groupby

# day 10: elves look, elves say

def day10(repeat):

    input = "1321131112"

    for i in range(repeat):

        new_input = ""
        for num, count in groupby(input):
            new_input += str(len(list(count))) + str(num)

        input = new_input

    return len(input)

print(day10(40))
print(day10(50))
