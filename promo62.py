from math import isnan

from mako.template import Template
from mako.lookup import TemplateLookup

from pandas import read_csv

from models.attribute import Attribute
from models.group import Group
from models.option import Option
from models.question import Question

postes = [
    "Présidence",
    "Vice-Présidence",
    "Trésorerie",
    "Secrétariat",
    "Webmestre",
    "Direction 5@8",
    "Direction Affaires Sociales",
    "Direction Bal / Voyages",
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

fc = read_csv('example/Candidatures.csv')

CONCENTRATION = fc.columns.get_loc('Concentration')
NOM_USUEL = fc.columns.get_loc('Nom usuel')
PHOTO = fc.columns.get_loc('Photo')
TEXTE_DESCRIPTION = fc.columns.get_loc('Texte descriptif')
POSTE_VISES = [
    fc.columns.get_loc('Poste visé #1'),
    fc.columns.get_loc('Poste visé #2'),
    fc.columns.get_loc('Poste visé #3')
]

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
    for x in POSTE_VISES:
        poste = candidat[x]
        if isinstance(poste, str):
            nom = candidat[NOM_USUEL]
            order = questions_map[poste].option_count()
            code = "A{numeral}".format(numeral=order+1)
            concentration = candidat[CONCENTRATION]

            description = "<p><strong>{name} ({concentration})</strong></p>".format(name=nom, concentration=concentration)
            for line in candidat[9].split('\n'):
                description += "<p>{line}</p>\n".format(line=line)

            option = Option(value=nom, code=code, order=order, description=description, image=candidat[PHOTO])
            questions_map[poste].add_option(option)

for poste in questions_map:
    order = questions_map[poste].option_count()
    lachaise = Option(value="La chaise", code="A{numeral}".format(numeral=order+1), order=order,
        description="<p><strong>La chaise (Whatever)</strong></p><p>La chaise ne vous laisseras pas tomber. Elle offre un bon support et connait bien son dossier. Elle connait sa place et ne s'exprime pas quand ce n'est pas son tour.</p>",
        image = "/upload/surveys/893586/images/markus_1.jpgd2fe39c4-d929-477e-ae08-ca0ec8e8a9e7Original.jpg"
    )
    questions_map[poste].add_option(lachaise)

mylookup = TemplateLookup(directories=['.'], input_encoding="utf-8", output_encoding="utf-8")
mytemplate = Template(filename='templates/promo62/base.mako', lookup=mylookup, input_encoding="utf-8", output_encoding="utf-8")

survey = mytemplate.render(groups=groups,questions=questions)

survey_file = open("result/survey.lss", "w+b")
survey_file.write(survey)
survey_file.close()