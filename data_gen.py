import sys
import csv
import artifact
import datetime
import stat_data
import pathlib


MAX_TESTS = 1000
TOTAL_RUNS = 1000
DEBUG = False

substat_names = ["HP_f","AK_f","DF_f","HP_p","AK_p","DF_p","ER_p","EM_f","CR_p","CD_p"]

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

def generative_model(artifact_type, stat_profile):
    a = artifact.Artifact(artifact_type)
    for i in range(MAX_TESTS):
        b = artifact.Artifact()
        if a.get_type() == b.get_type():
            a_score = eval_artifact(a, stat_profile)
            b_score = eval_artifact(b, stat_profile)
            if a_score < b_score: #what if I do this but factoring in mainstat into the scoring?
                break
    if i == MAX_TESTS - 1:
        i = MAX_TESTS
        b = None
    if DEBUG:
        if i == MAX_TESTS:
            print("None Found")
        else:
            print("Runs Taken: {i}".format(i=i))
            print("Artifact A\n---------\n{a} ".format(a=a))
            print("Artifact B\n---------\n{b} ".format(b=b))
    return (a, b, i, a_score, b_score)

def data_pipe(artifact_type, stat_profile, stat):
    j = 0

    with open("./Data/" + artifact_type + "_" + stat + '.csv', 'w', newline='') as csvfile:
        artist = csv.writer(csvfile, delimiter=',', quotechar="'")
        artist.writerow([
            "NumRuns",
            "ArtAType",
            "ArtAMainstat",
            "HP_f_A",
            "AK_f_A",
            "DF_f_A",
            "HP_p_A",
            "AK_p_A",
            "DF_p_A",
            "ER_p_A",
            "EM_f_A",
            "CR_p_A",
            "CD_p_A",
            "ArtBType",
            "ArtBMainstat",
            "HP_f_B",
            "AK_f_B",
            "DF_f_B",
            "HP_p_B",
            "AK_p_B",
            "DF_p_B",
            "ER_p_B",
            "EM_f_B",
            "CR_p_B",
            "CD_p_B"])
        for i in range(TOTAL_RUNS):
            (a, b, i, a_score, b_score) = generative_model(artifact_type, stat_profile)
            artist.writerow([i] + artifact_to_csv(a) + artifact_to_csv(b))
            j += i
