import sys
import random
import pandas as pd
import statistics
from urllib.request import urlretrieve
from os.path import exists

EM_stats = [0, 16.32, 18.65, 20.98, 23.31]
EM_spread = {}

def main():
    for i in range(0,1000):
        s = 0
        for j in range(0, 5):
            s += EM_stats[random.randint(0, 4)]
        EM_spread[round(s)] = 0
    print(EM_spread)



if __name__ == "__main__":
    sys.exit(main())
