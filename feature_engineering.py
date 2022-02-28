import pandas as pd
import stat_data as sd


def main_sub_sum(row):
	mainstat_name = row[2]
	row[mainstat_name + "_A"] = sd.mainstat_value[mainstat_name]
	return row

def fe_artifacts(artifacts):
	#TODO delete unneccessary rows
	return artifacts.apply(main_sub_sum, axis = 1)
