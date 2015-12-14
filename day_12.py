"""
whitney champion
advent of code
"""

import sys
import re
import json

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

print(day12(1))
print(day12(2))
