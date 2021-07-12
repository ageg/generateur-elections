from pandas import read_csv

from models.group import Group
from models.option import Option
from models.question import Question

CONCENTRATION = 'Concentration'
PROMOTION = 'Promotion'
NOM_USUEL = 'Nom usuel'
PHOTO = 'Photo'
TEXTE_DESCRIPTIF = 'Texte descriptif'
POSTE_VISE = 'Poste visé '

postes = {
    "Présidence": "PREZ",
    "Vice-Présidence aux Affaires Légales": "VPAL",
    "Vice-Présidence aux Affaires Internes": "VPAI",
    "Vice-Présidence aux Affaires Financières": "VPAF",
    "Vice-Présidence aux Affaires Pédagogiques": "VPAP",
    "Vice-Présidence aux Affaires Sociales": "VPAS",
    "Vice-Présidence aux Affaires Universitaires": "VPAU",
    "Vice-Présidence aux Activités Extracurriculaires": "VPAX",
    "Vice-Présidence à l'Image et aux Communications": "VPIC",
    "Vice-Présidence au Développement Durable": "VPDD",
    "Vice-Présidence aux Affaires Externes": "VPEX",
    "Vice-Présidence aux Cycles Supérieurs": "VPCS",
}


def generate_questions(conf):
    file = read_csv(f"input/{conf.input}")
    name = f"Comité exécutif {conf.session}"
    description = "Pour cette section, seulement une personne peut-être élue par poste."
    group = Group(name, description)

    columns = {
        CONCENTRATION: -1,
        PROMOTION: -1,
        NOM_USUEL: -1,
        PHOTO: -1,
        TEXTE_DESCRIPTIF: -1,
        POSTE_VISE: -1
    }

    questions = []
    questions_map = {}

    for col in columns.keys():
        if col not in file.columns:
            print(f"Column \"{col}\" not in {conf.input}")
            exit()

    # clean poste vise
    for poste in postes:
        file.loc[file[POSTE_VISE].str.contains(pat=f"(?:^{poste}|{postes[poste]})", regex=True), POSTE_VISE] = poste

    applied_posts = [poste for poste in postes if poste in file[POSTE_VISE].unique().tolist()]

    for i, poste in enumerate(applied_posts):
        question_code = postes[poste] + conf.session
        question_name = f"Qui voulez-vous au poste de {poste}?"
        question = Question(code=question_code, gid=group.gid, title=question_name, qtype='L', order=i)

        questions.append(question)
        questions_map[poste] = question

    for poste in postes:
        if poste not in applied_posts:
            conf.unused_posts.append(poste)

    for _, candidat in file.iterrows():
        poste = candidat[POSTE_VISE]
        nom = candidat[NOM_USUEL]
        order = questions_map[poste].answer_count()
        code = f"A{order + 1}"
        concentration = candidat[CONCENTRATION]
        promotion = candidat[PROMOTION]

        description = f"<p><strong>{nom} ({concentration}, {promotion})</strong></p>"
        for line in candidat[TEXTE_DESCRIPTIF].split('\n'):
            description += f"<p>{line}</p>\n"

        option = Option(value=nom, code=code, order=order, description=description, image=candidat[PHOTO])
        questions_map[poste].add_answer(option)
        questions_map[poste].add_option(option)

    for poste in questions_map:
        order = questions_map[poste].answer_count()
        lachaise = Option(
            value="La chaise",
            code=f"A{order + 1}",
            order=order,
            description=(
                "<p><strong>La chaise</strong></p><p>La chaise ne vous laisseras pas tomber. Elle offre un bon support "
                "et connait bien son dossier. Elle connait sa place et ne s'exprime pas quand ce n'est pas son tour"
                ".</p>"
            ),
            image="https://vote.ageg.ca/images/chaise.jpg"
        )
        questions_map[poste].add_answer(lachaise)
        questions_map[poste].add_option(lachaise)

    return group, questions
