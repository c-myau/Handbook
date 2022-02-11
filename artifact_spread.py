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

def artifact_to_csv(a):
    substat_dict = dict.fromkeys(substat_names, 0)
    substat_dict.update(a.get_substats())

    return [a.get_type(), a.get_mainstat()] + list(substat_dict.values())

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
        artist = csv.writer(csvfile, delimiter=',', quotechar="'")
        (a, b, i) = generative_model()
        a_row = artifact_to_csv(a)
        b_row = artifact_to_csv(b)
        artist.writerow([i] + a_row + b_row)



if __name__ == "__main__":
    sys.exit(main())
