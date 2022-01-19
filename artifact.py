import sys
import random
import pandas as pd
import numpy as np
import statistics
from urllib.request import urlretrieve
from os.path import exists

debug = True

profile_focus = ["EM_f"]

def generate_artifact():
    stats_dict = {key:0 for key in main_type() + assign_substats()}
    roll_substats(choice_list, random.choices([3,4], weights=(75, 25), k=1) + 5)

def roll_substats(choice_list, num_rolls):
    return True

def assign_mainstat():


def assign_substats():
    #check for profile focus
    # if len([value for value in choice_dict.keys() if value in profile_focus]) == 0:
    #     if debug:
    #         print("No Focus")
    #     return 0
    choice_list = np.random.choice(list(flower_sub), 4, replace=False, p = [x/100 for x in list(flower_sub.values())])
    return choice_list


def main():
    generate_artifact()

if __name__ == "__main__":
    sys.exit(main())