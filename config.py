from collections import namedtuple

SurveyConfig = namedtuple("SurveyConfig",
                          ["admin", "expiry", "expiry_text", "session", "type", "title", "comity", "comity_session",
                           "groups"])
GroupConfig = namedtuple("GroupConfig", ["type", "input", "session", "unused_posts"])

config = SurveyConfig(
    admin="Yves-Alexandre Beebe",
    expiry="2021-04-07 23:59:59",  # format to respect -> year-month-day hour:minute:second
    expiry_text="mercredi le 7 avril 2021 à minuit",
    type="l'AGEG",
    session="hiver 2021",
    title="Élection AGEG H21",
    comity="le comité exécutif et le conseil d'administration",
    comity_session="été et l'automne 2021",
    groups=[GroupConfig("exec", "exec_e21.csv", "E21", []), # deja comble VPEX, VPAX, VPIC, VPAS, VPDD
            GroupConfig("exec", "exec_a21.csv", "A21", []),
            GroupConfig("admin", "admin_E21.csv", "E21", []),
            GroupConfig("admin", "admin_A21.csv", "A21", []),
            GroupConfig("admin", "admin_annuel.csv", "Annuel", []),]
)

# config = SurveyConfig(
#     admin="Yves-Alexandre Beebe",
#     expiry="2021-04-07 23:59:59",  # format to respect -> year-month-day hour:minute:second
#     expiry_text="mercredi le 7 avril 2021 à minuit",
#     type="la finissante",
#     session="hiver 2021",
#     title="Élection finissante H21",
#     comity="le comité exécutif",
#     comity_session="été 2021",
#     groups=[GroupConfig("finissante", "finissante_e21.csv", "E21", [])]
# )
