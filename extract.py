import pandas as pd

def extract_artifacts(csvname):
    return pd.read_csv(csvname,index_col=False)

def export_artifacts(csvpath, dataframe):
    dataframe.to_csv(csvpath)

def load_csv(csvpath):
    return pd.read_csv(csvpath)
