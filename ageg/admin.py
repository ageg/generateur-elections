from math import isnan

from pandas import read_csv

from models.option import Option
from models.question import Question
from models.subquestion import Subquestion

fichier_admin = read_csv('example/admin.csv')

NOM_USUEL = fichier_admin.columns.get_loc('Nom usuel')
PHOTO = fichier_admin.columns.get_loc('Photo')
TEXTE_DESCRIPTIF = fichier_admin.columns.get_loc('Texte descriptif')
CONCENTRATION = fichier_admin.columns.get_loc('Concentration')
PROMOTION = fichier_admin.columns.get_loc('Promotion')

def zeroPad(value):
    return "0" + str(value) if value < 10 else str(value)

def generer_sousquestion_admin(parent):
    sous_questions = []
    for index, candidat in enumerate(fichier_admin.values):
        code = "SQ" + zeroPad(index+1)
        subquestion = Subquestion(qid=parent.qid+index+1, parent=parent.qid, gid=parent.gid, code=code, value=candidat[NOM_USUEL], order=index, type='T')
        sous_questions.append(subquestion)
    
    return sous_questions
    
def generer_options_admin():
    options = []

    for index, candidat in enumerate(fichier_admin.values):
        nom = candidat[NOM_USUEL]
        concentration = candidat[CONCENTRATION]
        promotion = candidat[PROMOTION]

        description = "<p><strong>{nom} ({concentration}, {promotion})</strong></p>".format(nom=nom, concentration=concentration, promotion=promotion)
        for line in candidat[TEXTE_DESCRIPTIF].split('\n'):
            description += "<p>{line}</p>\n".format(line=line)

        options.append(Option(value=candidat[NOM_USUEL], code="A{numeral}".format(numeral=index+1), order=index,
                description=description, image=candidat[PHOTO])
        )
    
    return options