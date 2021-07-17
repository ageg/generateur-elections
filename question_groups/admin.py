from pandas import read_csv

from models.group import Group
from models.option import Option
from models.question import Question
from models.subquestion import Subquestion
from models.answer import Answer
from constants import CONCENTRATION, PROMOTION, NOM_USUEL, PHOTO, TEXTE_DESCRIPTIF


def generate_questions(group_conf):
    df = group_conf['df']
    name = f"Conseil d'administration {group_conf['semester']}"
    if group_conf['semester'] == 'Annuel':
        description = "Vote de confiance pour les postes annuels au conseil d'administration de l'AGEG."
        code = f"CA{group_conf['semester']}"
        title = "Qui voulez-vous comme administrateurs annuels de l'AGEG?"
    else:
        description = "Vote de confiance pour les postes saisonniers au conseil d'administration de l'AGEG."
        code = "CAS" + group_conf['semeseter']
        title = "Qui voulez-vous comme administrateurs saisonniers de l'AGEG?"
    group = Group(name, description)

    question_admin = Question(
        code=code,
        gid=group.gid,
        title=title,
        qtype='F'
    )

    question_admin.add_answer(Answer(qid=question_admin.qid, value="Oui", code="A1", order=1))
    question_admin.add_answer(Answer(qid=question_admin.qid, value="Non", code="A2", order=2))
    question_admin.add_answer(Answer(qid=question_admin.qid, value="Non confiance", code="A3", order=3))

    sous_questions = []
    for index, candidat in df.iterrows():
        subquestion = Subquestion(
            parent=question_admin.qid,
            gid=question_admin.gid,
            code=f"SQ{index + 1:02}",
            value=candidat[NOM_USUEL],
            order=index,
            qtype='T'
        )
        sous_questions.append(subquestion)

        question_admin.add_option(
            Option(
                nom=candidat[NOM_USUEL],
                promotion=candidat[PROMOTION],
                concentration=candidat[CONCENTRATION],
                order=index,
                description=candidat[TEXTE_DESCRIPTIF],
                image=candidat[PHOTO]
            )
        )

    return group, question_admin, sous_questions
