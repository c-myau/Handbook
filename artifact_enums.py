from enum import Enum
import stat_data

class ArtifactType(Enum):
    CIRCLET = 1
    TIMEPIECE = 2
    FLOWER = 3
    FEATHER = 4
    GOBLET = 5

class ArtifactMain(Enum):
    HP = 1
    ATK = 2
    DEF = 3
    ELEMENTAL_MASTERY = 4
    ENERGY_RECHARGE = 5
    CRIT_RATE = 6
    CRIT_DMG = 7
    PYRO = 8
    ELECTRO = 9
    CRYO = 10
    HYDRO = 11
    DENDRO = 12
    ANEMO = 13
    GEO = 14
    PHYSICAL = 15
    HEALING_BONUS = 16
    HP_FLAT = 17
    ATK_FLAT = 18

class ArtifactSubDist(Enum):
    LOW = 1
    MID = 2
    HIGH = 3
    TOP = 4

valid_arguments = {
    "circlet":ArtifactType.CIRCLET,
    "timepiece":ArtifactType.TIMEPIECE,
    "flower":ArtifactType.FLOWER,
    "feather":ArtifactType.FEATHER,
    "goblet":ArtifactType.GOBLET,
    "hp":ArtifactMain.HP,
    "atk":ArtifactMain.ATK,
    "def":ArtifactMain.DEF,
    "em":ArtifactMain.ELEMENTAL_MASTERY,
    "er":ArtifactMain.ENERGY_RECHARGE,
    "cr":ArtifactMain.CRIT_RATE,
    "cd":ArtifactMain.CRIT_DMG,
    "pyro":ArtifactMain.PYRO,
    "electro":ArtifactMain.ELECTRO,
    "cryo":ArtifactMain.CRYO,
    "hydro":ArtifactMain.HYDRO,
    "dendro":ArtifactMain.DENDRO,
    "anemo":ArtifactMain.ANEMO,
    "geo":ArtifactMain.GEO,
    "phys":ArtifactMain.PHYSICAL,
}

artifact_total_map = {
    ArtifactType.CIRCLET:{
        ArtifactMain.ATK:stat_data.ak_sub,
        ArtifactMain.CRIT_RATE:stat_data.cr_sub,
        ArtifactMain.CRIT_DMG:stat_data.cd_sub,
        ArtifactMain.ELEMENTAL_MASTERY:stat_data.em_sub,
        ArtifactMain.HEALING_BONUS:stat_data.hb_sub
    },
    ArtifactType.TIMEPIECE:{
        ArtifactMain.ATK:stat_data.ak_sub,
        ArtifactMain.ELEMENTAL_MASTERY:stat_data.em_sub,
        ArtifactMain.ENERGY_RECHARGE:stat_data.er_sub,
        ArtifactMain.DEF:stat_data.df_sub,
        ArtifactMain.HP:stat_data.hp_sub
    },
    ArtifactType.FLOWER:{
        ArtifactMain.HP_FLAT:stat_data.hp_f_sub
    },
    ArtifactType.FEATHER:{
        ArtifactMain.HP_FLAT:stat_data.hp_f_sub
    },
    ArtifactType.GOBLET:
    {
        ArtifactMain.ATK:stat_data.ak_sub,
        ArtifactMain.ELEMENTAL_MASTERY:stat_data.em_sub,
        ArtifactMain.DEF:stat_data.df_sub,
        ArtifactMain.HP:stat_data.hp_sub,
        ArtifactMain.PYRO:stat_data.elemental_sub,
        ArtifactMain.ELECTRO:stat_data.elemental_sub,
        ArtifactMain.HYDRO:stat_data.elemental_sub,
        ArtifactMain.DENDRO:stat_data.elemental_sub,
        ArtifactMain.ANEMO:stat_data.elemental_sub,
        ArtifactMain.GEO:stat_data.elemental_sub,
        ArtifactMain.PHYSICAL:stat_data.elemental_sub,
    },
}
