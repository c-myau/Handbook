import sys
import csv
import artifact
import datetime
import stat_data


MAX_TESTS = 1000
TOTAL_RUNS = 100000
DEBUG = False
ARTIFACT_TYPE = sys.argv[1]

substat_names = ["HP_f","AK_f","DF_f","HP_p","AK_p","DF_p","ER_p","EM_f","CR_p","CD_p"]

ELECTRO_CRIT_PROFILE = {
    "EL_p":8,
    "CR_p":4,
    "CD_p":2,
    "AK_p":1
}

def eval_artifact(input_artifact, eval_profile):
    #Apply profile scaling to substat artifact value
    substat_score = sum([
                            value * eval_profile[key]
                                if key in eval_profile
                                else 0
                            for key, value in input_artifact.get_substats().items()
                        ])
    if input_artifact.get_mainstat() in eval_profile:
        #Apply profile scaling to mainstat artifact value
        mainstat_score = stat_data.mainstat_value[input_artifact.get_mainstat()] * eval_profile[input_artifact.get_mainstat()]
    else:
        mainstat_score = 0
    return substat_score + mainstat_score

def artifact_to_csv(a):
    if a is None:
        return []
    substat_dict = dict.fromkeys(substat_names, 0)
    substat_dict.update(a.get_substats())

    return [a.get_type(), a.get_mainstat()] + list(substat_dict.values())

def generative_model(a):
    for i in range(MAX_TESTS):
        b = artifact.Artifact()
        if a.get_type() == b.get_type():
            a_score = eval_artifact(a, ELECTRO_CRIT_PROFILE)
            b_score = eval_artifact(b, ELECTRO_CRIT_PROFILE)
            if a_score < b_score: #what if I do this but factoring in mainstat into the scoring?
                break
    return i

def main():
    begin = datetime.datetime.now()
    j = 0
    with open(ARTIFACT_TYPE + '_artifact_single_test.csv', 'w', newline='') as csvfile:
        artist = csv.writer(csvfile, delimiter=',', quotechar="'")
        artist.writerow([
            "NumRuns"])
        original_artifact = artifact.Artifact(ARTIFACT_TYPE)
        for i in range(TOTAL_RUNS):
            i = generative_model(original_artifact)
            artist.writerow([i])
            j += i

    print(datetime.datetime.now() - begin)
    print("Number of total runs: {i}".format(i=j))



if __name__ == "__main__":
    sys.exit(main())
