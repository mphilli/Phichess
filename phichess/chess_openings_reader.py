# for converting chess openings database into useable lists

import re

file = open("chess_openings.txt", "r+")
new_file = open("chess_openings_list.txt", "w+")
lines = file.readlines()
dictionary = {}
opening_names = []
sequences = []
hasVariation = True
code = ""; opening = ""
variation = ""
sequence = ""

for line in lines:
    if "[ECO" in line:
        code = line.replace('[ECO "', '')
        code = code.replace('"]', '')
        hasVariation = False
    elif "[Opening" in line:
        opening = line.replace('[Opening "', '')
        opening = opening.replace('"]', '')
        hasVariation = False #unknown
    elif "[Variation" in line:
        variation = line.replace('[Variation "', '')
        variation = variation.replace('"]', '')
        hasVariation = True
    else:
        if line.startswith("1."):
            sequence = re.sub('\d\.', '', line)
            sequence = sequence.replace("\n", "")
            sequence = sequence.replace("  ", " ")
            sequence = sequence.replace("*", "")
            if hasVariation == True:
                title = code + variation
                hasVariation = False
            else:
                title = code + opening
            title = title.replace("\n", " ")
            opening_names.append(title)
            sequences.append(sequence)
            hasVariation = False

for item in opening_names:
    #print(item + sequences[opening_names.index(item)])
    new_file.write(item + " - " + sequences[opening_names.index(item)] + "\n")
new_file.close()


        
