from pandas import read_csv

from models.group import Group
from models.option import Option
from models.question import Question
from models.subquestion import Subquestion
from models.answer import Answer

CONCENTRATION = 'Concentration'
PROMOTION = 'Promotion'
NOM_USUEL = 'Nom usuel'
PHOTO = 'Photo'
TEXTE_DESCRIPTIF = 'Texte descriptif'


def generate_questions(conf):
    file = read_csv(f"input/{conf.input}")

    name = f"Conseil d'administration {conf.session}"
    description = "Vote de confiance pour les postes saisonniers au conseil d'administration de l'AGEG."
    group = Group(name, description)

    columns = {
        CONCENTRATION: -1,
        PROMOTION: -1,
        NOM_USUEL: -1,
        PHOTO: -1,
        TEXTE_DESCRIPTIF: -1
    }

    for col in columns.keys():
        if col not in file.columns:
            print(f"Column \"{col}\" not in {conf.input}")
            exit()

    question_admin = Question(code="CAS" + conf.session, gid=group.gid,
                              title="Qui voulez-vous comme administrateurs saisonniers de l'AGEG?", qtype='F')

    question_admin.add_answer(Answer(qid=question_admin.qid, value="Oui", code="A1", order=1))
    question_admin.add_answer(Answer(qid=question_admin.qid, value="Non", code="A2", order=2))
    question_admin.add_answer(Answer(qid=question_admin.qid, value="Non confiance", code="A3", order=3))

    sous_questions = []
    for index, candidat in file.iterrows():
        code = f"SQ{index + 1:02}"
        subquestion = Subquestion(parent=question_admin.qid, gid=question_admin.gid,
                                  code=code,
                                  value=candidat[NOM_USUEL], order=index, qtype='T')
        sous_questions.append(subquestion)

    options = []

    for index, candidat in file.iterrows():
        nom = candidat[NOM_USUEL]
        concentration = candidat[CONCENTRATION]
        promotion = candidat[PROMOTION]

        description = f"<p><strong>{nom} ({concentration}, {promotion})</strong></p>"
        for line in candidat[TEXTE_DESCRIPTIF].split('\n'):
            description += f"<p>{line}</p>\n"

        options.append(Option(value=candidat[NOM_USUEL], code=f"A{index + 1}", order=index,
                              description=description, image=candidat[PHOTO])
                       )

    # return options

    for option in options:
        question_admin.add_option(option)

    return group, question_admin, sous_questions
