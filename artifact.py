import random
import numpy as np
import stat_data

#TOD0 fix 0 substat bug. Again
class Artifact:
    def __init__(self, artifact_type=None, artifact_mainstat=None, artifact_substats=None):
        [
            self.__type,
            self.__mainstat,
            self.__substats
        ] = self.generate_artifact(artifact_type, artifact_mainstat)

    def get_type(self):
        return self.__type

    def get_substats(self):
        return self.__substats

    def get_mainstat(self):
        return self.__mainstat

    def generate_artifact(self, artifact_type=None, artifact_mainstat=None):
        #TODO: add substat declaration functionality
        artifact = self._assign_maintype(artifact_type)
        mainstat = self._assign_mainstat(artifact, artifact_mainstat)
        substat_dict = stat_data.artifact_to_substat_map[artifact][mainstat]

        return [artifact, mainstat, self._roll_substats(substat_dict)]

    def _assign_maintype(self, override_artifact_type):
        if override_artifact_type is None:
            #roll main type
            return random.choice(list(stat_data.artifact_type))
        return override_artifact_type

    def _assign_mainstat(self, main_type, override_mainstat=None):
        if override_mainstat is None:
            #normalize mainstat weights
            main_weights = [
                float(x)/sum(stat_data.artifact_type[main_type].values())
                for x in stat_data.artifact_type[main_type].values()
            ]

            #roll mainstat
            return np.random.choice(
                list(stat_data.artifact_type[main_type].keys()),
                1,
                p=main_weights
            )[0]
        return override_mainstat

    def _roll_substats(self, substat_dict, override_substat_dict=None):
        if override_substat_dict is None:
            #set up parameters, normalize input data to 1
            data_weights = [
                float(x)/sum(substat_dict.values())
                for x in substat_dict.values()
            ]
            data_keys = list(substat_dict.keys())
            num_rolls = random.choices([3, 4], weights=(75, 25), k=1)[0]

            #roll for substat values
            substat_names = np.random.choice(data_keys, 4, replace=False, p=data_weights)
            substat_rolls = (
                list(np.random.choice(substat_names, 4, replace=False)) +
                random.choices(substat_names, k=num_rolls+1)
            )
            substat_power = (
                list(np.random.choice([0, 1, 2, 3], 4, replace=False)) +
                random.choices([0, 1, 2, 3], k=num_rolls+1)
            )
            #write artifact and output
            artifact_dict = dict.fromkeys(substat_names, 0)
            for substat, power in zip(substat_rolls, substat_power):
                artifact_dict[substat] += stat_data.substat_dist[substat][power]

            return {key: round(value) for key, value in artifact_dict.items()}
        return override_substat_dict

    def __repr__(self):
        substat_names = [stat_data.stat_name_map[x] for x in list(self.get_substats().keys())]
        substat_values = list(self.get_substats().values())
        substat_txt = ' '.join(
            '{}: {}\n'.format(first, second)
            for first, second
            in zip(substat_names, substat_values)
        )
        return "{main} {type}\n".format(
            type=self.get_type(),
            main=stat_data.stat_name_map[self.get_mainstat()]) + " "+ substat_txt
