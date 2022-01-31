import sys
import random
import datetime
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
        txt = "{stat} {artifact}"
        print(txt.format(stat=stat, artifact=artifact))
    artifact = roll_substats(substat_dict)
    print(artifact)

def roll_substats(substat_dict):
    num_rolls = random.choices([3,4], weights=(75, 25), k=1)[0]
    substat_names = np.random.choice(list(substat_dict.keys()), 4, replace=False, p=[float(x)/sum(list(substat_dict.values())) for x in list(substat_dict.values())])
    substat_rolls = random.choices(substat_names, k=num_rolls + 5)
    substat_power = list(np.random.choice(indexes, 4, replace=False)) + random.choices(indexes, k=num_rolls+1)
        
    artifact_dict = {key:0 for key in substat_names}
    for substat, power in zip(substat_rolls, substat_power):
        artifact_dict[substat] += stat_data.substat_dist[substat][power]

    return artifact_dict

def assign_mainstat():
    main_type = random.choice(list(stat_data.artifact_type.items()))
    return (main_type[0], np.random.choice(main_type[1]['attr'], 1, replace=False, p = [x/100 for x in main_type[1]['chnc']])[0])

#check for profile focus
# if len([value for value in choice_dict.keys() if value in profile_focus]) == 0:
#     if debug:
#         print("No Focus")
#     return 0


def main():
    begin = datetime.datetime.now()
    for i in range(0, 1):
        generate_artifact()
    print(datetime.datetime.now() - begin)


if __name__ == "__main__":
    sys.exit(main())