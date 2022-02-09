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
    #return the sum of all of the substat values within the input profile, multiplied by the profile's weight for that substat
    return sum([value * eval_profile[key] if key in eval_profile else 0 for key, value in input_artifact.get_substats().items()])

def main():
    a = artifact.Artifact()

    for i in range(1, MAX_TESTS):
        b = artifact.Artifact()
        if a.get_type() == b.get_type():
            if eval_artifact(a, crit_profile) < eval_artifact(b, crit_profile):
                break

    if i == MAX_TESTS:
        print("None Found")
    else:
        print("Runs Taken: {i}".format(i=i))
        print("Artifact A\n---------\n{a} ".format(a=a))
        print("Artifact B\n---------\n{b} ".format(b=b))

if __name__ == "__main__":
    sys.exit(main())
