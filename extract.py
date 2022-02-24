import csv
import pandas as pd

def extract_artifact(csvname):
	return pd.read_csv(csvname)[["ArtAType","ArtAMainstat","HP_f_A","AK_f_A","DF_f_A","HP_p_A","AK_p_A","DF_p_A","ER_p_A","EM_f_A","CR_p_A","CD_p_A"]]

