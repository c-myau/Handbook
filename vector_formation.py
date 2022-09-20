import numpy as np
import sys
import artifact_enums

def main():
    whitelist = set('abcdefghijklmnopqrstuvwxyz')
    v = artifact_enums.valid_arguments
    artifact_info = {param:None for param in ["type", "mainstat", "substats", "dist"]}
    arguments = [''.join(filter(whitelist.__contains__, x.lower())) for x in sys.argv[1:]]

    for a in arguments:
        if v[a] in artifact_enums.ArtifactType:
            artifact_info["type"] = v[a]
        elif v[a] in artifact_enums.ArtifactMain:
            artifact_info["mainstat"] = v[a]
            first_main = False
        elif v[a] in artifact_enums.ArtifactType:
            artifact_info["substats"] = v[a]

    print(artifact_info)

    #TODO add CLA list support
    #TODO add substat filling-in
    #TODO add reverse map of main stat to substat distribution
    #For list of arguments, produce the limited vector of potential stats


    if artifact_info["type"] in artifact_enums.artifact_total_map:
        if artifact_info["mainstat"] in artifact_enums.artifact_total_map[artifact_info["type"]]:
            print(artifact_enums.artifact_total_map[artifact_info["type"]][artifact_info["mainstat"]])
        else:
            print(artifact_enums.artifact_total_map[artifact_info["type"]])

if __name__ == '__main__':
    main()
