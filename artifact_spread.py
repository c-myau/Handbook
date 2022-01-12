import sys
import random
import pandas as pd
import statistics
from urllib.request import urlretrieve
from os.path import exists

#96: 0, 58: 0, 82: 0, 61: 0, 93: 0, 100: 0, 91: 0, 79: 0, 84: 0, 65: 0, 98: 0, 68: 0, 35: 0, 86: 0, 77: 0, 75: 0, 54: 0, 89: 0, 105: 0, 42: 0, 72: 0, 103: 0, 51: 0, 63: 0, 70: 0, 21: 0, 44: 0, 56: 0, 37: 0, 33: 0, 107: 0, 110: 0, 114: 0, 47: 0, 112: 0, 40: 0, 49: 0, 19: 0, 16: 0

EM_stats = [0, 16.32, 18.65, 20.98, 23.31]
EM_spread = []

def main():
    for i in range(0,100000):
        s = 0
        for j in range(0, 5):
            s += EM_stats[random.randint(0, 4)]

        if round(s) not in EM_spread:
            EM_spread.append(round(s))
    EM_spread.sort()
    print(EM_spread)



if __name__ == "__main__":
    sys.exit(main())
