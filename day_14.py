"""
whitney champion
advent of code
"""

import sys
import re
import collections
import itertools

# day 14: reindeer olympics

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

print(day14part1(2503))
print(day14part2(2503))
