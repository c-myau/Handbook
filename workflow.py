from os.path import exists #TODO add "exists" functionality to cut down on iteration time
import sys
import stat_data
import data_gen
import threading

#Gridsearch data creation
artifact_type = [
    "Circlet",
    "Timepiece",
    "Goblet",
    "Flower",
    "Feather"
]

ELECTRO_CRIT_PROFILE = {
    "EL_p":8,
    "CR_p":4,
    "CD_p":2,
    "AK_p":1
}

EM_PROFILE = {
    "EM_f":3,
    "ER_p":1,
}

HP_PROFILE = {
    "HP_p":2,
    "HP_f":1
}

profiles = {"elemental_crit":ELECTRO_CRIT_PROFILE, "elemental_mastery":EM_PROFILE}

threads = []

#TODO finish hooking up the data gen pipelines to the workflow file
#TODO send all data to a diff folder lol
#TODO add fill versus replace

for i in artifact_type:
    for j in profiles:
        threads.append(threading.Thread(target=data_gen.data_pipe, args=(i, profiles[j], j)))
k = 1
for j in threads:
    print("Starting Thread {k}".format(k=k))
    j.start()
    k+=1
print("Ending threads")
