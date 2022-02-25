import extract as extract
import feature_engineering as fe

#Extraction
artifacts = extract.extract_artifact("Circlet_artifact_data.csv")
print(artifacts)
artifacts = fe.fe_artifacts(artifacts)
#Training