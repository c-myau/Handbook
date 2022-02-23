import csv
import pandas as pd
def extract_artifact(csvname):
	return pd.read_csv(csvname)
	# with open(csvname, newline=nl) as csvfile:
	# 	artifact_reader = csv.reader(csvfile, delimiter=dl, quotechar=qc)
	# 	header = next(artifact_reader)
	# 	print(header)
	# 	for row in artifact_reader:
	# 	 	print(', '.join(row))
