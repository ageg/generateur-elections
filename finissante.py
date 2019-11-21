from math import isnan
from sys import exit
import os

from mako.template import Template
from mako.lookup import TemplateLookup

from pandas import read_csv

from models.attribute import Attribute
from models.group import Group
from models.option import Option
from models.question import Question

if os.path.isfile('example/Candidatures.csv'):
    print("JOB START ! Starting generation for finissante !")

    postes = [
        "Présidence",
        "Vice-Présidence",
        "Trésorerie",
        "Secrétariat",
        "Webmestre",
        "Direction 5@8",
        "Direction Affaires Sociales",
        "Direction Bal / Voyage",
        "Direction Souvenirs",
        "Direction Casino / Jonc",
        "Direction Journée Carrière",
        "Sous-Direction Bière",
        "Sous-Direction Fort",
        "Sous-Direction Caisse",
        "Sous-Direction Repas",
        "Sous-Direction Radio",
        "Sous-Direction Animation",
        "Sous-Direction Sécurité",
        "Sous-Direction Photographie"
    ]

    fc = read_csv('example/Candidatures.csv', sep=';')

    CONCENTRATION = 'Concentration'
    NOM_USUEL = 'Nom Complet'
    PHOTO = 'Photo'
    TEXTE_DESCRIPTIF = 'Texte descriptif'
    POSTES_VISES = [
        'Poste visé #1',
        'Poste visé #2',
        'Poste visé #3'
    ]

    colonnes = {
        CONCENTRATION: -1,
        NOM_USUEL: -1,
        PHOTO: -1,
        TEXTE_DESCRIPTIF: -1,
        POSTES_VISES[0]: -1,
        POSTES_VISES[1]: -1,
        POSTES_VISES[2]: -1
    }

    for col in colonnes.keys():
        try:
            colonnes[col] = fc.columns.get_loc(col)
        except KeyError:
            print(f"Colonne \"{col}\" manquante")
            exit()

    groups = []
    questions = []
    questions_map = {}

    def zeroPad(value):
        return "0" + str(value) if value < 10 else str(value)

    for i in range(0, len(postes)):
        question_code = "Q{numeral}".format(numeral=zeroPad(i+1))
        question_name = "Qui voulez-vous au poste de {poste}?".format(poste=postes[i])
        attributes = [
            Attribute("max_answers", "3"),
            Attribute("max_subquestions", "3"),
            Attribute("min_answers", "0")
        ]

        group = Group(id=i, name=postes[i])
        question = Question(id=i, code=question_code, gid=group.gid, title=question_name, attributes=attributes)

        groups.append(group)
        questions.append(question)
        questions_map[postes[i]] = question

    for candidat in fc.values:
        for POSTE in POSTES_VISES:
            poste = candidat[colonnes[POSTE]]
            if isinstance(poste, str):
                nom = candidat[colonnes[NOM_USUEL]]
                order = questions_map[poste].answer_count()
                code = "A{numeral}".format(numeral=order+1)
                concentration = candidat[colonnes[CONCENTRATION]]

                description = "<p><strong>{name} ({concentration})</strong></p>".format(name=nom, concentration=concentration)
                for line in candidat[colonnes[TEXTE_DESCRIPTIF]].split('\n'):
                    description += "<p>{line}</p>\n".format(line=line)

                option = Option(value=nom, code=code, order=order, description=description, image=candidat[colonnes[PHOTO]])
                questions_map[poste].add_option(option)
                questions_map[poste].add_answer(option)

    for poste in questions_map:
        order = questions_map[poste].answer_count()
        lachaise = Option(value="La chaise", code="A{numeral}".format(numeral=order+1), order=order,
            description="<p><strong>La chaise (Whatever)</strong></p><p>La chaise ne vous laisseras pas tomber. Elle offre un bon support et connait bien son dossier. Elle connait sa place et ne s'exprime pas quand ce n'est pas son tour.</p>",
            image = "https://vote.ageg.ca/images/chaise.jpg"
        )
        questions_map[poste].add_option(lachaise)
        questions_map[poste].add_answer(lachaise)

    mylookup = TemplateLookup(directories=['.'], input_encoding="utf-8", output_encoding="utf-8")
    mytemplate = Template(filename='templates/base.mako', lookup=mylookup, input_encoding="utf-8", output_encoding="utf-8")

    survey = mytemplate.render(groups=groups,questions=questions, subquestions=None, withAttributes=True)

    mypath = "result"
    if not os.path.isdir(mypath):
        os.makedirs(mypath)
    survey_file = open("result/finissante-survey.lss", "w+b")
    survey_file.write(survey)
    survey_file.close()

    print("JOB DONE ! You can find your result in result/finissante-survey.lss")
