from os.path import exists #TODO add "exists" functionality to cut down on iteration time
import sys
import pandas as pd
import feature_engineering as fe
import extract as ex
import training as tr

training_file_path = "./Circlet_artifact_data.csv"
export_file_path = "./Circlet_postprocessed_data.csv"
    #Extraction and feature_engineering, manual one-hot encoding essentially
artifacts = ex.extract_artifacts(training_file_path)
artifacts = fe.fe_artifacts(artifacts)
# artifacts = pd.read_csv(export_file_path)

    #Training
artifact_model = tr.model_selection_func(artifacts, "rft")
