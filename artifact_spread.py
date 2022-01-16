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

profile_focus = ["EM_f"]
EM_stats = [0, 16.32, 18.65, 20.98, 23.31]
EM_spread = []
EM_dist = {}

def num_ss():
    if random.randint(1,4) == 4:
        substats(4)
    else: 
        substats(3)

def substats(num_initial_stats):
    assign_rolls = 4
    max_rolls = 9
    for i in range(0, assign_rolls):
        choice_list = assign_substat()
        if len([value for value in choice_list if value in profile_focus]) == 0:
            print("blank")
            return 0 #TODO remove this terminating returns
        else:
            return 1
    for i in range(assign_rolls, max_rolls + num_initial_stats - assign_rolls):
        roll_substat()

def assign_substat():
    choice_list = np.random.choice(list(flower_sub), 4, replace=True, p = [x/100 for x in list(flower_sub.values())])
    print(choice_list)
    return choice_list

def roll_substat():

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
