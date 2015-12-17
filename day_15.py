"""
whitney champion
advent of code
"""

import sys
import re

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

print(day15(1))
print(day15(2))
