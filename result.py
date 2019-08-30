from math import isnan
from pandas import read_csv

results = read_csv("example/results.csv")

res = {}

l = len(results.values)
ponderation = [4, 2, 1]

from functools import cmp_to_key

def cmp_scores(a, b):
    if a[1]["points"] > b[1]["points"]:
        return 1
    elif a[1]["points"] < b[1]["points"]:
        return -1
    elif a[1]["positions"][1] > b[1]["positions"][1]:
        return 1
    elif a[1]["positions"][1] < b[1]["positions"][1]:
        return -1
    
    return -1

def cmp_print(a, b):
    print(a[1], b[1])
    return 0

cols = len(results.columns)

for c in range(7, cols):
    end = results.columns[c].find('?')
    poste = results.columns[c][28:end]
    cl = results.columns[c].find('Classement')
    classement = int(results.columns[c][cl+11])
    points = ponderation[classement-1]

    for reponse in results.values:
        value = reponse[c]

        if isinstance (value, float):
            continue
        
        if(not poste in res):
            res[poste] = {}
        
        if not value in res[poste]:
            res[poste][value] = {
                "points": 0,
                "positions": {1: 0, 2: 0, 3: 0}
            }
        
        res[poste][value]["points"] += points
        res[poste][value]["positions"][classement] += 1       

for poste in res:
    print(poste)
    scoreTuples = sorted(res[poste].items(), key=cmp_to_key(cmp_scores), reverse=True)
    for score in scoreTuples:
        print(score)