import sys
import random
import numpy as np
import stat_data
from os.path import exists

class Artifact:
    def __init__(self, artifact_type=None, artifact_mainstat=None, artifact_substats=None): 
        [self.__type, self.__substats, self.__mainstat] = self.generate_artifact(artifact_type, artifact_mainstat, artifact_substats)

    def get_type(self):
        return self.__type

    def get_substats(self):
        return self.__substats

    def get_mainstat(self):
        return self.__mainstat

    def generate_artifact(self, artifact_type, artifact_mainstat, artifact_substats):
        if artifact_type is None:
            #maybe split main stat and artifact type assignment up?
            artifact, stat = self._assign_mainstat()
            substat_dict = stat_data.artifact_to_substat_map[artifact][stat]
        else:
            if artifact_mainstat is None:
                artifact, stat = self._assign_mainstat(artifact_type)
                substat_dict = stat_data.artifact_to_substat_map[artifact][stat]
            else:
                if artifact_substats is None:
                    artifact, stat = artifact_type, artifact_mainstat
                    substat_dict = stat_data.artifact_to_substat_map[artifact][stat]
                else:
                    [artifact, stat, substat_dict] = artifact_type, artifact_mainstat, artifact_substats

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

    def _assign_mainstat(self, input_artifact_type = None):
        #choose mainstat
        main_type = random.choice(list(stat_data.artifact_type))

        #normalize mainstat weights
        main_weights = [
            float(x)/sum(stat_data.artifact_type[main_type].values())
            for x in stat_data.artifact_type[main_type].values()
        ]

        #choose mainstat 
        mainstat = np.random.choice(list(stat_data.artifact_type[main_type].keys()), 1, p=main_weights)[0]

        return (main_type, mainstat)

    def _set_artifact_type(input_artifact_type):
        self.__type = input_artifact_type

    def _set_mainstat(input_artifact_type, input_mainstat):
        self.__mainstat = input_mainstat
        return True

    def _set_substat_dict():
        return True

