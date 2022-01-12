import sys
import random
import pandas as pd
import statistics
from urllib.request import urlretrieve
from os.path import exists

#96: 0, 58: 0, 82: 0, 61: 0, 93: 0, 100: 0, 91: 0, 79: 0, 84: 0, 65: 0, 98: 0, 68: 0, 35: 0, 86: 0, 77: 0, 75: 0, 54: 0, 89: 0, 105: 0, 42: 0, 72: 0, 103: 0, 51: 0, 63: 0, 70: 0, 21: 0, 44: 0, 56: 0, 37: 0, 33: 0, 107: 0, 110: 0, 114: 0, 47: 0, 112: 0, 40: 0, 49: 0, 19: 0, 16: 0

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
        if not assign_substat():
            return 0
    for i in range(assign_rolls, max_rolls + num_initial_stats - assign_rolls):
        roll_substat()

def assign_substat():
    #return true if any desired stats are present
    return True

def roll_substat():
    return True

#TODO: write the substat rolling code
def main():
    for i in range(0,1000000):
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
