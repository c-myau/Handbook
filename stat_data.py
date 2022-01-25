import pandas as pd

hp_circlet_sub = {
    "HP_f":15.00,
    "AK_f":15.00,
    "DF_f":15.00,
    "HP_p":0,
    "AK_p":10.00,
    "DF_p":10.00,
    "ER_p":10.00,
    "EM_f":10.00,
    "CR_p":7.50,
    "CD_p":7.50
}

ak_circlet_sub = {
    "HP_f":15.00,
    "AK_f":15.00,
    "DF_f":15.00,
    "HP_p":10.00,
    "AK_p":0,
    "DF_p":10.00,
    "ER_p":10.00,
    "EM_f":10.00,
    "CR_p":7.50,
    "CD_p":7.50
}

df_circlet_sub = {
    "HP_f":15.00,
    "AK_f":15.00,
    "DF_f":15.00,
    "HP_p":10.00,
    "AK_p":10.00,
    "DF_p":0,
    "ER_p":10.00,
    "EM_f":10.00,
    "CR_p":7.50,
    "CD_p":7.50
}

em_circlet_sub = {
    "HP_f":15.00,
    "AK_f":15.00,
    "DF_f":15.00,
    "HP_p":10.00,
    "AK_p":10.00,
    "DF_p":10.00,
    "ER_p":10.00,
    "EM_f":0,
    "CR_p":7.50,
    "CD_p":7.50
}

cr_circlet_sub = {
    "HP_f":14.63,
    "AK_f":14.63,
    "DF_f":14.63,
    "HP_p":9.76,
    "AK_p":9.76,
    "DF_p":9.76,
    "ER_p":9.76,
    "EM_f":9.76,
    "CR_p":0,
    "CD_p":7.32
}

cd_circlet_sub = {
    "HP_f":14.63,
    "AK_f":14.63,
    "DF_f":14.63,
    "HP_p":9.76,
    "AK_p":9.76,
    "DF_p":9.76,
    "ER_p":9.76,
    "EM_f":9.76,
    "CR_p":7.32,
    "CD_p":0
}

hb_circlet_sub = {
    "HP_f":13.64,
    "AK_f":13.64,
    "DF_p":13.64,
    "HP_p":9.09,
    "AK_p":9.09,
    "DF_p":9.09,
    "ER_p":9.09,
    "EM_f":9.09,
    "CR_p":6.82,
    "CD_p":6.82
}


hp_timepiece_sub = {
    "HP_f":15.00,
    "AK_f":15.00,
    "DF_f":15.00,
    "HP_p":0,
    "AK_p":10.00,
    "DF_p":10.00,
    "ER_p":10.00,
    "EM_f":10.00,
    "CR_p":7.50,
    "CD_p":7.50
}

ak_timepiece_sub = {
    "HP_f":15.00,
    "AK_f":15.00,
    "DF_f":15.00,
    "HP_p":10.00,
    "AK_p":0,
    "DF_p":10.00,
    "ER_p":10.00,
    "EM_f":10.00,
    "CR_p":7.50,
    "CD_p":7.50
}

df_timepiece_sub = {
    "HP_f":15.00,
    "AK_f":15.00,
    "DF_f":15.00,
    "HP_p":10.00,
    "AK_p":10.00,
    "DF_p":0,
    "ER_p":10.00,
    "EM_f":10.00,
    "CR_p":7.50,
    "CD_p":7.50
}

er_timepiece_sub = {
    "HP_f":15.00,
    "AK_f":15.00,
    "DF_f":15.00,
    "HP_p":10.00,
    "AK_p":10.00,
    "DF_p":10.00,
    "ER_p":0,
    "EM_f":10.00,
    "CR_p":7.50,
    "CD_p":7.50
}

em_timepiece_sub = {
    "HP_f":15.00,
    "AK_f":15.00,
    "DF_f":15.00,
    "HP_p":10.00,
    "AK_p":10.00,
    "DF_p":10.00,
    "ER_p":10.00,
    "EM_f":0,
    "CR_p":7.50,
    "CD_p":7.50
}

hp_goblet_sub = {
    "HP_f":15.00,
    "AK_f":15.00,
    "DF_f":15.00,
    "HP_p":0,
    "AK_p":10.00,
    "DF_p":10.00,
    "ER_p":10.00,
    "EM_f":10.00,
    "CR_p":7.50,
    "CD_p":7.50
}

ak_goblet_sub = {
    "HP_f":15.00,
    "AK_f":15.00,
    "DF_f":15.00,
    "HP_p":10.00,
    "AK_p":0,
    "DF_p":10.00,
    "ER_p":10.00,
    "EM_f":10.00,
    "CR_p":7.50,
    "CD_p":7.50
}

df_goblet_sub = {
    "HP_f":15.00,
    "AK_f":15.00,
    "DF_f":15.00,
    "HP_p":10.00,
    "AK_p":10.00,
    "DF_p":0,
    "ER_p":10.00,
    "EM_f":10.00,
    "CR_p":7.50,
    "CD_p":7.50
}

elemental_goblet_sub = {
    "HP_f":13.64,
    "AK_f":13.64,
    "DF_f":13.64,
    "HP_p":9.09,
    "AK_p":9.09,
    "DF_p":9.09,
    "ER_p":9.09,
    "EM_f":9.09,
    "CR_p":6.82,
    "CD_p":6.82
}

em_goblet_sub = {
    "HP_f":15.00,
    "AK_f":15.00,
    "DF_f":15.00,
    "HP_p":10.00,
    "AK_p":10.00,
    "DF_p":10.00,
    "ER_p":10.00,
    "EM_f":0,
    "CR_p":7.50,
    "CD_p":7.50
}

flower_sub = {
    "HP_f":0,
    "AK_f":15.79,
    "DF_f":15.79,
    "HP_p":10.53,
    "AK_p":10.53,
    "DF_p":10.53,
    "ER_p":10.53,
    "EM_f":10.53,
    "CR_p":7.89,
    "CD_p":7.88
}


feather_sub = {
    "HP_f":15.79,
    "AK_f":0,
    "DF_f":15.79,
    "HP_p":10.53,
    "AK_p":10.53,
    "DF_p":10.53,
    "ER_p":10.53,
    "EM_f":10.53,
    "CR_p":7.89,
    "CD_p":7.88
}

circlet_stats_dict = {
    "HP_p":(22.00, hp_circlet_sub),
    "AK_p":(22.00, ak_circlet_sub),
    "DF_p":(22.00, df_circlet_sub),
    "CR_p":(10.00, cr_circlet_sub),
    "CD_p":(10.00, cd_circlet_sub),
    "HB_p":(10.00, hb_circlet_sub),
    "EM_p":(4.00, em_circlet_sub)
}

timepiece_stats_dict = {
    "HP_p":(26.66, hp_timepiece_sub),
    "AK_p":(26.66, ak_timepiece_sub),
    "DF_p":(26.68, df_timepiece_sub),
    "ER_p":(10.00, er_timepiece_sub),
    "EM_p":(20.00, em_timepiece_sub)
}


goblet_stats_dict = {
    "HP_p":(21.25, hp_goblet_sub),
    "AK_p":(21.25, ak_goblet_sub),
    "DF_p":(20.68, df_goblet_sub),
    "PY_p":(5.00, elemental_goblet_sub),
    "EL_p":(5.00, elemental_goblet_sub),
    "CY_p":(5.00, elemental_goblet_sub),
    "HY_p":(5.00, elemental_goblet_sub),
    "AN_p":(5.00, elemental_goblet_sub),
    "GE_p":(5.00, elemental_goblet_sub),
    "PH_p":(5.00, elemental_goblet_sub),
    "EM_p":(2.50, em_goblet_sub)
}

flower_stats_dict = {
    "HP_p":(100, flower_sub),
}

feather_stats_dict = {
    "HP_p":(100, feather_sub),
}

substat_dist = {
    "HP_f": [209.13, 239.00, 268.88, 298.75],
    "AK_f": [13.62, 15.56, 17.51, 19.45],
    "DF_f": [16.20, 18.52, 20.83, 23.15],
    "HP_p": [4.08, 4.66, 5.25, 5.83],
    "AK_p": [4.08, 4.66, 5.25, 5.83],
    "DF_p": [5.10, 5.83, 6.56, 7.29],
    "ER_p": [4.53, 5.18, 5.83, 6.48],
    "CR_p": [2.72, 3.11, 3.50, 3.89],
    "CD_p": [5.44, 6.22, 6.99, 7.77]
}

main_circlet = pd.DataFrame.from_dict({'attr':["HP_p", "AK_p", "DF_p", "CR_p", "CD_p", "HB_p", "EM_f"], 'chnc':[22.00,22.00,22.00,10.00,10.00,10.00,4.00]})
main_timepiece = pd.DataFrame.from_dict({'attr':["HP_p", "AK_p", "DF_p", "ER_p", "EM_f"], 'chnc':[26.68,26.66,26.66,10.00,10.00]})
main_goblet = pd.DataFrame.from_dict({'attr':["HP_p", "AK_p", "DF_p", "PY_p", "EL_p","CY_p", "HY_p","AN_p", "GE_p","PH_p", "EM_f"], 'chnc':[21.25,21.25,20.00,5.00,5.00,5.00,5.00,5.00,5.00,5.00,2.50]})
main_flower = pd.DataFrame.from_dict({'attr':["HP_f"], 'chnc':[100]})
main_feather = pd.DataFrame.from_dict({'attr':["AK_f"], 'chnc':[100]})

artifact_type = {
    "Circlet" : main_circlet,
    "Timepiece" : main_timepiece,
    "Goblet" : main_goblet,
    "Flower" : main_flower,
    "Feather" : main_feather
}