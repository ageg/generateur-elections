from collections import namedtuple

SurveyConfig = namedtuple("SurveyConfig",
                          ["admin", "expiry", "expiry_text", "session", "type", "title", "comity", "comity_session",
                           "groups"])
GroupConfig = namedtuple("GroupConfig", ["type", "input", "session", "unused_posts"])

config = SurveyConfig(
    admin="Yves-Alexandre Beebe",
    expiry="2021-07-16 23:59:59",  # format to respect -> year-month-day hour:minute:second
    expiry_text="vendredi le 16 juillet 2021 à minuit",
    type="l'AGEG",
    session="été 2021",
    title="Élection AGEG E21",
    comity="le comité exécutif et le conseil d'administration",
    comity_session="automne 2021 et l'hiver 2022",
    groups=[GroupConfig("exec", "exec_a21_2.csv", "A21", ["VPAU","VPDD"]),  # deja comble VPEX, VPAX, VPIC, VPAS, VPDD
            GroupConfig("exec", "exec_h22.csv", "H22", []),
            GroupConfig("admin", "admin_a21_2.csv", "A21", []),
            GroupConfig("admin", "admin_h22.csv", "H22", []), ]
            # GroupConfig("admin", "admin_annuel.csv", "Annuel", []), ]
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
