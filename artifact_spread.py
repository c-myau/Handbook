import sys
import csv
import artifact

substat_names = ["HP_f","AK_f","DF_f","HP_p","AK_p","DF_p","ER_p","EM_f","CR_p","CD_p"]
CRIT_PROFILE = {"CR_p":4, "CD_p":2, "AK_p":1}
MAX_TESTS = 1000
TOTAL_RUNS = 1000
DEBUG = False

def eval_artifact(input_artifact, eval_profile):
    #return the sum of all of the substat values within the input profile, multiplied by the profile's weight for that substat
    return sum([value * eval_profile[key] if key in eval_profile else 0 for key, value in input_artifact.get_substats().items()])

#TODO change string format to just returning a list
def artifact_to_csv(a):
    substat_dict = dict.fromkeys(substat_names, 0)
    for key in a.get_substats():
        substat_dict[key] = a.get_substats()[key]

    return "{type},{mainstat},{hp_f},{ak_f},{df_f},{hp_p},{ak_p},{df_p},{er_p},{em_f},{cr_p},{cd_p}".format(
        type=a.get_type(),
        mainstat=a.get_mainstat(),
        hp_f=substat_dict["HP_f"],
        ak_f=substat_dict["AK_f"],
        df_f=substat_dict["DF_f"],
        hp_p=substat_dict["HP_p"],
        ak_p=substat_dict["AK_p"],
        df_p=substat_dict["DF_p"],
        er_p=substat_dict["ER_p"],
        em_f=substat_dict["EM_f"],
        cr_p=substat_dict["CR_p"],
        cd_p=substat_dict["CD_p"]
    )

def generative_model():
    a = artifact.Artifact()
    for i in range( MAX_TESTS):
        b = artifact.Artifact()
        if a.get_type() == b.get_type():
            if eval_artifact(a, CRIT_PROFILE) < eval_artifact(b, CRIT_PROFILE):
                break
    if i == MAX_TESTS:
        i = None
    if DEBUG:
        if i == MAX_TESTS:
            print("None Found")
        else:
            print("Runs Taken: {i}".format(i=i))
            print("Artifact A\n---------\n{a} ".format(a=a))
            print("Artifact B\n---------\n{b} ".format(b=b))
    return (a, b, i)

def main():
    with open('artifact_data.csv', 'w', newline='') as csvfile:
        artist = csv.writer(csvfile, delimiter=' ', quotechar="'")
        a = generative_model()[0]
        a_txt = artifact_to_csv(a)
        print(a)
        print(a_txt)
        artist.writerow([a_txt])



if __name__ == "__main__":
    sys.exit(main())
