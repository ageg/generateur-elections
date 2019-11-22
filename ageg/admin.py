from math import isnan

from pandas import read_csv

from models.option import Option
from models.question import Question
from models.subquestion import Subquestion

CONCENTRATION = 'Concentration'
PROMOTION = 'Promotion'
NOM_USUEL = 'Nom usuel'
PHOTO = 'Photo'
TEXTE_DESCRIPTIF = 'Texte descriptif'

colonnes = {
    CONCENTRATION: -1,
    PROMOTION: -1,
    NOM_USUEL: -1,
    PHOTO: -1,
    TEXTE_DESCRIPTIF: -1
}

fichier_admin = read_csv('example/admin.csv')

for col in colonnes.keys():
    try:
        colonnes[col] = fichier_admin.columns.get_loc(col)
    except KeyError:
        print(f"Colonne \"{col}\" manquante")
        exit()

def zeroPad(value):
    return "0" + str(value) if value < 10 else str(value)

def generer_sousquestion_admin(parent):
    sous_questions = []
    for index, candidat in enumerate(fichier_admin.values):
        code = "SQ" + zeroPad(index+1)
        subquestion = Subquestion(qid=parent.qid+index+1, parent=parent.qid, gid=parent.gid, code=code, value=candidat[colonnes[NOM_USUEL]], order=index, type='T')
        sous_questions.append(subquestion)

    return sous_questions

def generer_options_admin():
    options = []

    for index, candidat in enumerate(fichier_admin.values):
        nom = candidat[colonnes[NOM_USUEL]]
        concentration = candidat[colonnes[CONCENTRATION]]
        promotion = candidat[colonnes[PROMOTION]]

        description = "<p><strong>{nom} ({concentration}, {promotion})</strong></p>".format(nom=nom, concentration=concentration, promotion=promotion)
        for line in candidat[colonnes[TEXTE_DESCRIPTIF]].split('\n'):
            description += "<p>{line}</p>\n".format(line=line)

        options.append(Option(value=candidat[colonnes[NOM_USUEL]], code="A{numeral}".format(numeral=index+1), order=index,
                description=description, image=candidat[colonnes[PHOTO]])
        )

    return options