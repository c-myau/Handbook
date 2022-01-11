import sys
import random
import pandas as pd
import statistics
from urllib.request import urlretrieve
from os.path import exists


# substat_url = 'https://raw.githubusercontent.com/Dimbreath/GenshinData/blob/master/ExcelBinOutput/ReliquaryAffixExcelConfigData.json'
substat_local = 'substat.json'
# mainstat_url = 'https://raw.githubusercontent.com/Dimbreath/GenshinData/master/ExcelBinOutput/ReliquaryMainPropExcelConfigData.jsonn'
mainstat_local = 'mainstat.json'

main_circlet = pd.DataFrame.from_dict({'attr':["HP_p", "AK_p", "DF_p", "CR_p", "CD_p", "HB_p", "EM_f"], 'chnc':[22.00,22.00,22.00,10.00,10.00,10.00,4.00]})
main_timepiece = pd.DataFrame.from_dict({'attr':["HP_p", "AK_p", "DF_p", "ER_p", "EM_f"], 'chnc':[26.68,26.66,26.66,10.00,10.00]})
main_goblet = pd.DataFrame.from_dict({'attr':["HP_p", "AK_p", "DF_p", "PY_p", "EL_p","CY_p", "HY_p","AN_p", "GE_p","PH_p", "EM_f"], 'chnc':[21.25,21.25,20.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00,2.50]})
main_flower = pd.DataFrame.from_dict({'attr':["HP_f"], 'chnc':[100]})
main_feather = pd.DataFrame.from_dict({'attr':["AK_f"], 'chnc':[100]})

carry_profile = {1:["CR_p","CD_p"],2:["AK_p"],3:["EL_p"],4:["HP_f"],5:["AK_f"]}
main_d = {1:main_circlet,2:main_timepiece,3:main_goblet,4:main_flower,5:main_feather}

starting_artifacts = {}

def CalcDistance():
	#something like a parabolic curve of probability?
	#For EM, would also only need half of the curve for the purposes of calculation since the parabola is symetrical
	#Parabolic curve or maybe its more like an upside-down backwards log function
	#Edge would be max roll on EM artifact
	#Dead center would be mid rolls on both
	#only question is what to do... maybe a synthesis of all of the different probabilities of reaching the point?
	#from any point in the curve feels like a tall order though
	#maybe I can do an aggregated build quality metric, then simply count the high-quality artifacts as something easier.
	#Would only have to be a 2-D array
	return True

def ArtifactRoll():
	artifact_set = random.randint(0,1)
	main_type = random.randint(1, 5)
	stat_roll = random.randint(1, 100)
	chance_df = main_d[main_type]
	index = 0
	while True:
		stat_roll -= chance_df.iloc[index]['chnc']
		if stat_roll <= 0:
			break
		index += 1
	if chance_df.iloc[index]['attr'] in carry_profile[main_type] and artifact_set == 1:
		return main_type
	return None

def main():
	count_list = []
	for i in range(0, 1000):
		random.seed()
		count = 0
		found = 0
		distribution = {1:0,2:0,3:0,4:0,5:0}
		artifact_set = {1:False, 2:False, 3:False, 4:False, 5:False}
		while count < 100000:
			a = ArtifactRoll()
			if a:
				distribution[a] += 1
				artifact_set[a] = True
				found += 1
			count += 1
			if all(x for x in artifact_set.values()):
				break
		count_list.append(count)
	print(sum(count_list)/len(count_list))
	print(statistics.pstdev(count_list))
	return True

if __name__ == "__main__":
    sys.exit(main())
