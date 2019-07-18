from math import isnan

from pandas import read_csv

from models.option import Option
from models.question import Question

SESSION = "A19"

CONCENTRATION = 'Concentration'
PROMOTION = 'Promotion'
NOM_USUEL = 'Nom usuel'
PHOTO = 'Photo'
TEXTE_DESCRIPTIF = 'Texte descriptif'
POSTE_VISE = 'Poste visé'

postes = [
    "Présidence",
    "Vice-Présidence aux Affaires Légales",
    "Vice-Présidence aux Affaires Internes",
    "Vice-Présidence aux Affaires Financières",
    "Vice-Présidence aux Affaires Pédagogiques",
    "Vice-Présidence aux Affaires Sociales",
    "Vice-Présidence aux Affaires Universitaires",
    "Vice-Présidence aux Activités Extracurriculaires",
    "Vice-Présidence aux Employés et Communications",
    "Vice-Présidence au Développement Durable"
]

abbreviations = {
    "Présidence": "PREZ",
    "Vice-Présidence aux Affaires Légales": "VPAL",
    "Vice-Présidence aux Affaires Internes": "VPAI",
    "Vice-Présidence aux Affaires Financières": "VPAF",
    "Vice-Présidence aux Affaires Pédagogiques": "VPAP",
    "Vice-Présidence aux Affaires Sociales": "VPAS",
    "Vice-Présidence aux Affaires Universitaires": "VPAU",
    "Vice-Présidence aux Activités Extracurriculaires": "VPAX",
    "Vice-Présidence aux Employés et Communications": "VPEC",
    "Vice-Présidence au Développement Durable": "VPDD"
}

def zeroPad(value):
    return "0" + str(value) if value < 10 else str(value)

def generer_questions_exec(gid):
    questions = []
    questions_map = {}

    fichier_exec = read_csv('example/executif.csv')

    colonnes = {
        CONCENTRATION: -1,
        PROMOTION: -1,
        NOM_USUEL: -1,
        PHOTO: -1,
        TEXTE_DESCRIPTIF: -1,
        POSTE_VISE: -1   
    }

    for col in colonnes.keys():
        try:
            colonnes[col] = fichier_exec.columns.get_loc(col)
        except KeyError:
            print(f"Colonne \"{col}\" manquante")
            exit()

    for i in range(0, len(postes)):
        question_code = abbreviations[postes[i]] + SESSION
        question_name = "Qui voulez-vous au poste de {poste}?".format(poste=postes[i])
        question = Question(id=i, code=question_code, gid=gid, title=question_name, type='L', order=i)

        questions.append(question)
        questions_map[postes[i]] = question

    for candidat in fichier_exec.values:
        poste = candidat[colonnes[POSTE_VISE]]
        nom = candidat[colonnes[NOM_USUEL]]
        order = questions_map[poste].answer_count()
        code = "A{numeral}".format(numeral=order+1)
        concentration = candidat[colonnes[CONCENTRATION]]
        promotion = candidat[colonnes[PROMOTION]]

        description = "<p><strong>{name} ({concentration}, {promotion})</strong></p>".format(name=nom, concentration=concentration, promotion=promotion)
        for line in candidat[colonnes[TEXTE_DESCRIPTIF]].split('\n'):
            description += "<p>{line}</p>\n".format(line=line)

        option = Option(value=nom, code=code, order=order, description=description, image=candidat[colonnes[PHOTO]])
        questions_map[poste].add_answer(option)
        questions_map[poste].add_option(option)

    for poste in questions_map:
        order = questions_map[poste].answer_count()
        lachaise = Option(value="La chaise", code="A{numeral}".format(numeral=order+1), order=order,
            description="<p><strong>La chaise</strong></p><p>La chaise ne vous laisseras pas tomber. Elle offre un bon support et connait bien son dossier. Elle connait sa place et ne s'exprime pas quand ce n'est pas son tour.</p>",
            image = "/upload/surveys/893586/images/markus_1.jpgd2fe39c4-d929-477e-ae08-ca0ec8e8a9e7Original.jpg"
        )
        questions_map[poste].add_answer(lachaise)
        questions_map[poste].add_option(lachaise)

    return questions
