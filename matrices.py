#slice if you need only three starting stats or four
substat_distribution = [
    [5,0,0,0],
    [4,1,0,0],
    [3,2,0,0],
    [3,1,1,0],
    [2,2,1,0],
    [2,1,1,1],
    [4,0,0,0],
    [3,1,0,0],
    [2,2,0,0],
    [2,1,1,0],
    [1,1,1,1],
    [4,0,0,0],
    [3,1,0,0],
    [2,2,0,0],
    [2,1,1,0],
    [1,1,1,1],
    [4,0,0,0],
    [3,1,0,0],
    [2,2,0,0],
    [2,1,1,0],
    [1,1,1,1],
]

#get cartesian product of itself in a 5-D format
substat_dist = {
    "HP_f": [209.13, 239.00, 268.88, 298.75],
    "AK_f": [13.62, 15.56, 17.51, 19.45],
    "DF_f": [16.20, 18.52, 20.83, 23.15],
    "HP_p": [4.08, 4.66, 5.25, 5.83],
    "AK_p": [4.08, 4.66, 5.25, 5.83],
    "DF_p": [5.10, 5.83, 6.56, 7.29],
    "ER_p": [4.53, 5.18, 5.83, 6.48],
    "CR_p": [2.72, 3.11, 3.50, 3.89],
    "CD_p": [5.44, 6.22, 6.99, 7.77],
    "EM_f": [16.32, 18.65, 20.98, 23.31]
}
import csv
for item in substat_dist:
    for i in range(len(substat_dist[item])):
        print(i)
        
