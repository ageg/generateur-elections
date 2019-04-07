from math import isnan
from pandas import read_csv

results = read_csv("example/results.csv")

l = len(results.values)
ponderation = [4, 2, 1]

from functools import cmp_to_key

def cmp_scores(a, b):
    if a[1]["points"] > b[1]["points"]:
        return 1
    if a[1]["positions"][0] > b[1]["positions"][0]:
        return 1
    
    return -1

def cmp_print(a, b):
    print(a[1], b[1])
    return 0

for x in range(0, 19):
    score = {}
    
    c = 4 + (x*3)
    end = results.columns[c].find('?')
    poste = results.columns[c][28:end]

    for reponse in results.values:
        for z in range(0, 3):
            personne = reponse[c+z]
            if isinstance(personne, str): 
                if not personne in score:
                    score[personne] = { "points": 0, "positions": [0, 0, 0] }
                    
                score[personne]["positions"][z] += 1
                score[personne]["points"]  += ponderation[z]

    scoreTuples = sorted(score.items(), key=cmp_to_key(cmp_scores), reverse=True)
    print(poste)
    for key, value in scoreTuples:
        print("{key}: {points} ({p0}, {p1}, {p2})".format(key=key, points=value["points"], p0=value["positions"][0], p1=value["positions"][1], p2=value["positions"][2]))
    
    print()
