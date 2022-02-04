import sys
import random
import numpy as np
import stat_data
from os.path import exists

class Artifact:
    def __init__(self):
        [self.__type, self.__mainstat, self.__substats] = self.generate_artifact()

    def get_type(self):
        return self.__type

    def get_substats(self):
        return self.__substats

    def get_mainstat(self):
        return self.__mainstat

    def generate_artifact(self):
        artifact, stat = self._assign_mainstat()
        substat_dict = stat_data.artifact_to_substat_map[artifact][stat]
        return [artifact, stat, self._roll_substats(substat_dict)]

    def _roll_substats(self, input_substat_dict):
        #set up parameters, normalize input data to 1
        data_weights = [
            float(x)/sum(input_substat_dict.values()) 
            for x in input_substat_dict.values()
        ]
        data_keys = list(input_substat_dict.keys())
        num_rolls = random.choices([3,4], weights=(75, 25), k=1)[0]

        #roll for substat values
        substat_names = np.random.choice(data_keys, 4, replace=False, p=data_weights)
        substat_rolls = random.choices(substat_names, k=num_rolls + 5)
        substat_power = (
            list(np.random.choice([0,1,2,3], 4, replace=False)) +
            random.choices([0,1,2,3], k=num_rolls+1)
        )

        #write artifact and output
        artifact_dict = dict.fromkeys(substat_names, 0)
        for substat, power in zip(substat_rolls, substat_power):
            artifact_dict[substat] += stat_data.substat_dist[substat][power]

        return {key: round(value) for key, value in artifact_dict.items()}

    def _assign_mainstat(self):
        #choose mainstat
        main_type = random.choice(list(stat_data.artifact_type.items()))

        #normalize mainstat weights
        main_weights = [
            x/sum(main_type[1]['chnc'])
            for x in main_type[1]['chnc']
        ]

        return (main_type[0], np.random.choice(main_type[1]['attr'], 1, replace=False, p = main_weights)[0])

