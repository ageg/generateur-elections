text_elements = [
    "welcome_text",
    "email_invite_subject",
    "email_invite_content",
    "email_reminder_subject",
    "email_reminder_content"
]
CONCENTRATION = 'Concentration'
PROMOTION = 'Promotion'
NOM_USUEL = 'Nom usuel' #NOM_USUEL = 'Nom Complet'
PHOTO = 'Photo'
TEXTE_DESCRIPTIF = 'Texte descriptif'
POSTE_VISE = 'Poste visé '
POSTES_VISES = [
    'Poste Visé #1',
    'Poste visé #2',
    'Poste visé #3'
]

file_columns = {
    "exec": [
        CONCENTRATION,
        PROMOTION,
        NOM_USUEL,
        PHOTO,
        TEXTE_DESCRIPTIF,
        POSTE_VISE
    ],

    "admin": [
        CONCENTRATION,
        PROMOTION,
        NOM_USUEL,
        PHOTO,
        TEXTE_DESCRIPTIF
    ],

    "finissante": [
        CONCENTRATION,
        NOM_USUEL,
        PHOTO,
        TEXTE_DESCRIPTIF,
        POSTES_VISES[0],
        POSTES_VISES[1],
        POSTES_VISES[2]
    ]
}
