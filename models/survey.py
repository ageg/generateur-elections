class Survey:
    def __init__(self, conf):
        self.admin = conf['admin']
        self.expires = conf['expiry']
        self.title = conf['title']
        self.description = f"Élections de {conf['type']} pour {conf['comity']}"  # de l'été 2020" #TODO add semester?
        self.welcome_text = (
            "Bonjour,<br />\n"
            "<br />\n"
            "C'est par honneur, par sens du devoir et par plaisir que je suis votre directeur d'élections pour les "
            f"élections des {conf['comity']} de {conf['type']} pour l'{conf['comity_session']}.<br />\n"
            "<br />\n"
            "L'Association générale étudiante en génie est une association qui défend les droits de ses membres et "
            "offre des services à sa communauté par le biais de personnes représentantes issues de ses membres. Tout "
            "au long de leur mandat, ces représentants seront appelés à se prononcer au nom de votre association et "
            "donc en votre nom. Il est donc important que vous fassiez confiance en ces gens et que vous leur "
            "accordiez votre vote seulement si vous leur faites confiance de bien vous représenter.<br />\n"
            "<br />\n"
            "Les réponses aux questions sont anonymes et il n'est pas possible de voter plus d'une fois. Nous vous "
            "invitons donc à voter selon vos valeurs et vos convictions et non par rapport à la réaction de vos amis "
            "ou collègues.<br />\n"
            f"<br />\n"
            f"Le vote sera ouvert jusqu'à {conf['expiry_text']}.<br />\n"
            "<br />\n"
            "Je vous remercie de votre participation et de votre confiance rénouvelée en notre association étudiante,"
            "<br />\n"
            "<strong>{ADMINNAME}<br />\n"
            f"Directeurs d'élections, session d'{conf['session']}</strong>"
        )
        if any(group['unused_posts'] for group in conf['groups'] if group['type'] == "exec"):
            postes_vacant = ""
            for group in conf['groups']:
                if group['type'] == "exec":
                    postes_vacant += f"\nLes postes vacant pour le conseil exécutif {group['session']} sont:\n<br />"
                    for post in group['unused_posts']:
                        postes_vacant += f"La {post}\n<br />"
            self.end_text = (
                "Des postes resteront vacants suite à cette élection régulière.\n<br />"
                f"{postes_vacant}"                
                "Nous vous invitons à venir vous renseigner au local de l'AGEG, C1-2045 de la Faculté de Génie.<br />\n"
                "<br />\n"
                "Merci d'avoir participé et bonne journée"
            )
        else:
            self.end_text = (
                "Tous les postes seront comblés suite à cette élection régulière. Si vous desirer vous impliquer, nous "
                "vous invitons à venir vous renseigner au local de l'AGEG, C1-2045 de la Faculté de Génie.<br />\n"
                "<br />\n"
                "Merci d'avoir participé et bonne journée"
            )
        self.email_invite_subject = f"Élections de {conf['type']} - {conf['comity_session']}"
        self.email_invite_body = (
            "<html>\n"
            "<head>\n"
            "<title></title>\n"
            "</head>\n"
            "<body>\n"
            "<p>Bonjour {FIRSTNAME},<br />\n"
            "<br />\n"
            f"Vous êtes par la présente invité(e) à inscrire votre vote pour {conf['comity']} de {conf['type']}.</p>\n\n"
            "<p>Pour participer, veuillez cliquer sur le lien ci-dessous:<br />\n"
            "{SURVEYURL}<br />\n"
            "<br />\n"
            "Merci de votre temps,<br />\n"
            "{ADMINNAME} ({ADMINEMAIL})</p>\n"
            "</body>\n"
            "</html>\n"
        )
        self.email_reminder_subject = f"Rappel pour les élections de {conf['type']}"
        self.email_reminder_body = (
            "<html>\n"
            "<head>\n"
            "<title></title>\n"
            "</head>\n"
            "<body>\n"
            "<p>Bonjour {FIRSTNAME},<br />\n"
            "<br />\n"
            f"Vous avez été invité(e) à inscrire votre vote pour {conf['comity']} de {conf['type']}."
            "<br />\n"
            "<br />\n"
            f"Nous avons pris en compte que vous n'avez pas encore complété le questionnaire, et nous vous rappelons "
            f"que celui-ci est toujours disponible si vous souhaitez participer. Vous avez jusqu'à {conf['expiry_text']} "
            "pour voter.<br />\n"
            "<br />\n"
            "Pour participer, veuillez cliquer sur le lien ci-dessous:<br />\n"
            "{SURVEYURL}</p>\n\n"
            "<p><br />\n"
            "Merci de votre temps,<br />\n"
            "{ADMINNAME} ({ADMINEMAIL})</p>\n"
            "</body>\n"
            "</html>\n"
        )

    # def __repr__(self): #TODO implement debug text
    #     return f"<Question qid={self.qid} gid={self.gid} title={self.title} name={self.code} options={self.options}>"
