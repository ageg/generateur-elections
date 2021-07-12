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

CONCENTRATION = 'Concentration'
NOM_USUEL = 'Nom Complet'
PHOTO = 'Photo'
TEXTE_DESCRIPTIF = 'Texte descriptif'
POSTES_VISES = [
    'Poste Visé #1',
    'Poste visé #2',
    'Poste visé #3'
]


def generate_questions(conf):
    file = read_csv(f'input/{conf.input}')
    description = "Pour cette section, seulement une personne peut-être élue par poste."

    columns = {
        CONCENTRATION: -1,
        NOM_USUEL: -1,
        PHOTO: -1,
        TEXTE_DESCRIPTIF: -1,
        POSTES_VISES[0]: -1,
        POSTES_VISES[1]: -1,
        POSTES_VISES[2]: -1
    }

    for col in columns.keys():
        if col not in file.columns:
            print(f"Column \"{col}\" not in Candidatures.csv")
            exit()

    groups = []
    questions = []
    questions_map = {}

    for i, poste in enumerate(postes):
        question_code = f"Q{i + 1:02}"
        question_name = f"Qui voulez-vous au poste de {poste}?"
        attributes = [
            Attribute("max_answers", "3"),
            Attribute("max_subquestions", "3"),
            Attribute("min_answers", "0")
        ]

        group = Group(name=poste, description=description)
        question = Question(code=question_code, gid=group.gid, title=question_name, attributes=attributes)

        groups.append(group)
        questions.append(question)
        questions_map[poste] = question

    for _, candidat in file.iterrows():
        for POSTE in POSTES_VISES:
            poste = candidat[POSTE]
            if isinstance(poste, str):
                nom = candidat[NOM_USUEL]
                order = questions_map[poste].answer_count()
                code = f"A{order+1}"
                concentration = candidat[CONCENTRATION]

                description = f"<p><strong>{nom} ({concentration})</strong></p>"
                for line in candidat[TEXTE_DESCRIPTIF].split('\n'):
                    description += f"<p>{line}</p>\n"

                option = Option(
                    value=nom,
                    code=code,
                    order=order,
                    description=description,
                    image=candidat[PHOTO]
                )
                questions_map[poste].add_option(option)
                questions_map[poste].add_answer(option)

    for poste in questions_map:
        order = questions_map[poste].answer_count()
        lachaise = Option(
            value="La chaise",
            code=f"A{order + 1}",
            order=order,
            description=(
                "<p><strong>La chaise (Whatever)</strong></p><p>La chaise ne vous laisseras pas tomber. Elle offre un "
                "bon support et connait bien son dossier. Elle connait sa place et ne s'exprime pas quand ce n'est pas "
                "son tour.</p>"
            ),
            image="https://vote.ageg.ca/images/chaise.jpg"
        )
        questions_map[poste].add_option(lachaise)
        questions_map[poste].add_answer(lachaise)

    return groups, questions
