"""
whitney champion
advent of code
"""

import sys
import re
from collections import defaultdict

# day 21: rpg simulator 20xx

def day21(day):

    '''
    (hit points, damage, armor)
    '''
    boss = [109,8,2]
    if day is 1:
        player = [100,7,4]
    else:
        player = [100,7,3]

    player_turn = True
    while boss[0] > 0 and player[0] > 0:

        # if it's the player's turn
        if player_turn is True:

            # boss's hit points are player's damage minus boss's armor
            if (player[1] - boss[2]) < 0:
                boss[0] -= 1
            else:
                boss[0] -= player[1] - boss[2]

            player_turn = False

        # it's the boss's turn
        else:
            # player's hit points are boss's damage minus player's armor
            if (boss[1] - player[2]) < 0:
                player[0] -= 1
            else:
                player[0] -= boss[1] - player[2]

            player_turn = True

        print "Player: ",player
        print "Boss: ",boss

        '''
        Lowest combo to win is [100,7,4], and lowest amount of coins to get 7 and 4 is 111
        40 - 1 Longsword
        31 - 1 Chainmail
        40 - 1 Defense +2 Ring
        '''

        '''
        Highest combo to still lose is [100,7,3], and highest amount of coins is
        100 - 1 Damage +3 Ring
        8 - 1 Dagger
        80 - 1 Defense +3 Ring
        '''

print(day21(1))
print(day21(2))
