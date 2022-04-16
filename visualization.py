import sys
import csv
import artifact
import datetime
import stat_data
import numpy as np
from matplotlib import pyplot as plt

art_array= []
with open("Circlet_artifact_single_test.csv", newline="") as csvfile:
    artifact_reader = csv.reader(csvfile, delimiter=',')
    next(artifact_reader)
    for row in artifact_reader:
        art_array.append(int(row[0]))
a = np.array(art_array)
bins = [x for x in range(0, 100)]
plt.hist(a, bins)
plt.title("histogram")
plt.show()
print("Average: {avg}".format(avg = np.average(a)))
print("Standard Deviation: {std}".format(std = np.std(a)))
