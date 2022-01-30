import sys
import random
import pandas as pd
import numpy as np
import statistics
import stat_data
from urllib.request import urlretrieve
from os.path import exists

debug = True
profile_focus = ["EM_f"]
indexes = [0,1,2,3]

def generate_artifact():
    artifact, stat = assign_mainstat()
    substat_dict = stat_data.artifact_to_substat_map[artifact][stat]
    if debug:
        print(artifact)
    roll_substats(substat_dict)

def roll_substats(substat_dict):
    num_rolls = random.choices([3,4], weights=(75, 25), k=1)[0] + 5
    substat_names = np.random.choice(list(substat_dict.keys()), 4, replace=False, p=[x/100 for x in list(substat_dict.values())])
    substat_distribution = [stat_data.substat_dist[key] for key in substat_names]
    substat_rolls = random.choices(substat_names, k=num_rolls)
    substat_power = random.choices(indexes, k=num_rolls)
    
        
    artifact_dict = {key:0 for key in substat_names}
    for substat, power in zip(substat_rolls, substat_power):
        artifact_dict[substat] += stat_data.substat_dist[substat][power]
    if debug:
        print(substat_distribution)
        print(substat_rolls)
        print(substat_power)
        print(artifact_dict)

    #TODO next list comprehension to add substats
    #TODO check matrix sums
    #TODO each stat gets at least 1 hit
    return True

def assign_mainstat():
    main_type = random.choice(list(stat_data.artifact_type.items()))
    return (main_type[0], np.random.choice(main_type[1]['attr'], 1, replace=False, p = [x/100 for x in main_type[1]['chnc']])[0])

#check for profile focus
# if len([value for value in choice_dict.keys() if value in profile_focus]) == 0:
#     if debug:
#         print("No Focus")
#     return 0


def main():
    generate_artifact()

if __name__ == "__main__":
    sys.exit(main())