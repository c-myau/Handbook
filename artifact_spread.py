import sys
import artifact

#check for profile focus
# if len([value for value in choice_dict.keys() if value in profile_focus]) == 0:
#     if debug:
#         print("No Focus")
#     return 0


#TODO: write the substat rolling code
def main():
    a = artifact.Artifact("Circlet")
    print(a)

if __name__ == "__main__":
    sys.exit(main())
