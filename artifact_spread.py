import sys
import random
import pandas as pd
import numpy as np
import statistics
from urllib.request import urlretrieve
from os.path import exists

debug = True

#ATK    15.79%
# DEF 15.79%
# HP% 10.53%
# ATK%    10.53%
# DEF%    10.53%
# Energy Recharge%    10.53%
# Elemental Mastery   10.53%
# CRIT Rate%  7.89%
# CRIT DMG%   7.89%
EM_spread = []
EM_dist = {}

#TODO: write the substat rolling code
def main():
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
