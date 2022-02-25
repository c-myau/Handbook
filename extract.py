import csv
import pandas as pd

def extract_artifact(csvname):
	return pd.read_csv(csvname,index_col=False)

