import pandas as pd
import extract as extract
import feature_engineering as fe

#Extraction
artifacts = extract.extract_artifact("Circlet_artifact_data.csv")
artifacts = fe.fe_artifacts(artifacts)
print(artifacts)
#Training
