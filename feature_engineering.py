import stat_data as sd

rows = [
    "NumRuns",
    "ArtAType",
    "ArtAMainstat",
    "HP_f_A",
    "AK_f_A",
    "DF_f_A",
    "HP_p_A",
    "AK_p_A",
    "DF_p_A",
    "ER_p_A",
    "EM_f_A",
    "CR_p_A",
    "CD_p_A"
]

def main_sub_sum(row):
    mainstat_name = row[2]
    row[mainstat_name + "_A"] = sd.mainstat_value[mainstat_name]
    return row

def fe_artifacts(artifacts):

    #dimensionality reduction
    artifacts = artifacts[rows]
    all_stats = [item + "_A" for item in sd.stat_name_map.keys()]
    all_cols = rows[:3] + all_stats

    #reindex dataframe for pure scoring mode
    artifacts = artifacts.reindex(columns=all_cols, fill_value = 0)

    #add mainstat value to stat columns
    artifacts = artifacts.apply(main_sub_sum, axis = 1)
    #drop more rows on the way out
    return artifacts[[rows[0]] + all_stats]
