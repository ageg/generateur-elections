text_elements = [
    "description",
    "welcome_text",
    "email_invite_subject",
    "email_invite_content",
    "email_reminder_subject",
    "email_reminder_content"
]
CONCENTRATION = 'Concentration'
PROMOTION = 'Promotion'
NOM_USUEL = 'Nom usuel'  # NOM_USUEL = 'Nom Complet'
PHOTO = 'Photo'
TEXTE_DESCRIPTIF = 'Texte descriptif'
TEXTES_DESCRIPTIFS = [
    'Texte descriptif (Poste #1)',
    'Texte descriptif (Poste #2)',
    'Texte descriptif (Poste #3)'
]
POSTE_VISE = 'Poste visé '
POSTES_VISES = [
    'Poste visé #1',
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

    "promo": [
        CONCENTRATION,
        NOM_USUEL,
        PHOTO,
        TEXTE_DESCRIPTIF,
        POSTE_VISE
    ],

    "finissante": [
        CONCENTRATION,
        NOM_USUEL,
        PHOTO,
        POSTES_VISES[0],
        TEXTES_DESCRIPTIFS[0],
        POSTES_VISES[1],
        TEXTES_DESCRIPTIFS[1],
        POSTES_VISES[2],
        TEXTES_DESCRIPTIFS[2],
    ]
}
