from pandas import read_csv

from models.group import Group
from models.option import Option
from models.question import Question
from constants import CONCENTRATION,PROMOTION,NOM_USUEL,PHOTO, TEXTE_DESCRIPTIF, POSTE_VISE


def generate_questions(conf, group_conf):
    df = group_conf['df']
    name = f"Comité exécutif {group_conf['semester']}"
    description = "Pour cette section, seulement une personne peut-être élue par poste."
    group = Group(name, description)
    postes = conf['postes_exec']

    questions = []
    questions_map = {}

    # clean poste vise
    for poste in postes:
        df.loc[df[POSTE_VISE].str.contains(pat=f"(?:^{postes[poste]}|{poste})", regex=True), POSTE_VISE] = poste

    applied_posts = [poste for poste in postes if poste in df[POSTE_VISE].unique().tolist()]

    for i, poste in enumerate(applied_posts):
        question = Question(
            code=poste + group_conf['semester'],
            gid=group.gid,
            title=f"Qui voulez-vous au poste de {postes[poste]}?",
            qtype='L',
            order=i
        )

        questions.append(question)
        questions_map[poste] = question

    if 'unused_posts' not in group_conf.keys():
        group_conf['unused_posts'] = []

    for poste in postes:
        if poste not in applied_posts:
            group_conf['unused_posts'].append(poste)

    for _, candidat in df.iterrows():
        poste = candidat[POSTE_VISE]
        option = Option(
            nom=candidat[NOM_USUEL],
            promotion=candidat[PROMOTION],
            concentration=candidat[CONCENTRATION],
            order=questions_map[poste].answer_count(),
            description=candidat[TEXTE_DESCRIPTIF],
            image=candidat[PHOTO]
        )

        questions_map[poste].add_answer(option)
        questions_map[poste].add_option(option)

    for poste in questions_map:
        lachaise = Option.add_chaise(questions_map[poste].answer_count())
        questions_map[poste].add_answer(lachaise)
        questions_map[poste].add_option(lachaise)

    return group, questions
