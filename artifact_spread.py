import sys
import artifact

#check for profile focus
# if len([value for value in choice_dict.keys() if value in profile_focus]) == 0:
#     if debug:
#         print("No Focus")
#     return 0

crit_profile = {"CR_p":2, "CD_p":1}
MAX_TESTS = 10000

def eval_artifact(input_artifact, eval_profile):
    if len([value for value in input_artifact.get_substats().keys() if value in eval_profile]) == 0:
        return False
    return True
    #TODO add scoring methodology

def main():
    a = artifact.Artifact("Flower")

    for i in range(1, MAX_TESTS):
        b = artifact.Artifact("Flower")
        if eval_artifact(b, crit_profile):
            break

    if i == MAX_TESTS:
        print("None Found")
    else:
        print("Runs Taken: {i}".format(i=i))
        print("Artifact A\n---------\n{a} ".format(a=a))
        print("Artifact B\n---------\n{b} ".format(b=b))

if __name__ == "__main__":
    sys.exit(main())
