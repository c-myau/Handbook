import sys
import random
import pandas as pd
import numpy as np
import statistics
import artifact
from urllib.request import urlretrieve
from os.path import exists

debug = True

#check for profile focus
# if len([value for value in choice_dict.keys() if value in profile_focus]) == 0:
#     if debug:
#         print("No Focus")
#     return 0


#TODO: write the substat rolling code
def main():
    artifact.generate_artifact()

if __name__ == "__main__":
    sys.exit(main())
