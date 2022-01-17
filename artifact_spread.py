import sys
import random
import pandas as pd
import numpy as np
import statistics
from urllib.request import urlretrieve
from os.path import exists

#ATK    15.79%
# DEF 15.79%
# HP% 10.53%
# ATK%    10.53%
# DEF%    10.53%
# Energy Recharge%    10.53%
# Elemental Mastery   10.53%
# CRIT Rate%  7.89%
# CRIT DMG%   7.89%
flower_sub = {
    "AK_f":15.79,
    "DF_f":15.79,
    "HP_p":10.53,
    "AK_p":10.53,
    "DF_p":10.53,
    "ER_p":10.53,
    "EM_f":10.53,
    "CR_p":7.89,
    "CD_p":7.88
}

feather_sub = {
    "HP_f":15.79,
    "DF_f":15.79,
    "HP_p":10.53,
    "AK_p":10.53,
    "DF_p":10.53,
    "ER_p":10.53,
    "EM_f":10.53,
    "CR_p":7.89,
    "CD_p":7.88
}

substat_dist = {
    "EM_f": [16.32, 18.65, 20.98, 23.31],
    "HP_f": [209.13, 239.00, 268.88, 298.75],
    "AK_f": [13.62, 15.56, 17.51, 19.45],
    "DF_f": [16.20, 18.52, 20.83, 23.15],
    "HP_p": [4.08, 4.66, 5.25, 5.83],
    "AK_p": [4.08, 4.66, 5.25, 5.83],
    "DF_p": [5.10, 5.83, 6.56, 7.29],
    "ER_p": [4.53, 5.18, 5.83, 6.48],
    "CR_p": [2.72, 3.11, 3.50, 3.89],
    "CD_p": [5.44, 6.22, 6.99, 7.77]
}

profile_focus = ["EM_f"]
EM_spread = []
EM_dist = {}

def num_ss():
    if random.randint(1,4) == 4:
        substats(4)
    else: 
        substats(3)

#TODO fix multiple dupe substas
def substats(num_initial_stats):
    assign_rolls = 4
    max_rolls = 9
    choice_list = assign_substat()
    #check for profile focus
    if len([value for value in choice_list if value in profile_focus]) == 0:
        print("No EM")
        return 0
    roll_substats(choice_list, num_initial_stats + 1)

def assign_substat():
    choice_list = np.random.choice(list(flower_sub), 4, replace=True, p = [x/100 for x in list(flower_sub.values())])
    print(choice_list)
    return choice_list

def roll_substats(choice_list, num_rolls):
    for i in range(0, num_rolls):
        print(choice_list[random.randint(0, 3)])
    return True

#TODO: write the substat rolling code
def main():
    num_ss()
    for i in range(0,10000):
        stat = 0
        if round(stat) not in EM_spread:
            EM_spread.append(round(stat))
            EM_dist[round(stat)] = 1
        else:
            EM_dist[round(stat)] += 1
    EM_spread.sort()
    for item in EM_spread:
        txt = "EM {power}: {EM}"
        print(txt.format(power=item, EM=EM_dist[item]))

if __name__ == "__main__":
    sys.exit(main())
