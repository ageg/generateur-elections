from pandas import isna
from constants import CONCENTRATION, NOM_USUEL, PHOTO, TEXTES_DESCRIPTIFS, POSTES_VISES
from models.attribute import Attribute
from models.group import Group
from models.option import Option
from models.question import Question

def generate_questions(conf,group_conf):
    df = group_conf['df']
    description = "Pour cette section, seulement une personne peut-être élue par poste."
    postes = conf['postes_finissante']

    groups = []
    questions = []
    questions_map = {}

    for i, poste in enumerate(postes):
        group = Group(name=poste, description=description)
        question = Question(
            code=f"Q{i + 1:02}",
            gid=group.gid,
            title=f"Qui voulez-vous au poste de {poste}?",
            attributes=[
                Attribute("max_answers", "3"),
                Attribute("max_subquestions", "3"),
                Attribute("min_answers", "0")
            ]
        )

        groups.append(group)
        questions.append(question)
        questions_map[poste] = question

    for _, candidat in df.iterrows():
        for i,POSTE in enumerate(POSTES_VISES):
            poste = candidat[POSTE]
            if isna(candidat[TEXTES_DESCRIPTIFS[i]]):
                candidat[TEXTES_DESCRIPTIFS[i]] = ""
            if isinstance(poste, str):
                option = Option(
                    nom=candidat[NOM_USUEL],
                    concentration=candidat[CONCENTRATION],
                    order=questions_map[poste].answer_count(),
                    description=candidat[TEXTES_DESCRIPTIFS[i]],
                    image=candidat[PHOTO]
                )
                questions_map[poste].add_option(option)
                questions_map[poste].add_answer(option)

    for poste in questions_map:
        lachaise = Option.add_chaise(questions_map[poste].answer_count())
        questions_map[poste].add_option(lachaise)
        questions_map[poste].add_answer(lachaise)

    return groups, questions
