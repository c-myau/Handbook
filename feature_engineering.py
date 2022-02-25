import pandas as pd
import stat_data as sd


def main_sub_sum(mainstat_name):
	return sd.mainstat_value[mainstat_name]

def fe_artifacts(artifacts):
	print(artifacts)
	return artifacts.apply(lambda row: main_sub_sum(row[2]), axis = 1)
	