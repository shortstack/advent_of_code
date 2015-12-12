"""
whitney champion
advent of code
"""

import sys
import re

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

print(day11("hepxcrrq"))
print(day11(day11("hepxcrrq")))
