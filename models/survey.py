class Survey:
    def __init__(self, conf):
        self.admin = conf['admin']
        self.expires = conf['expiry']
        self.title = conf['title']
        self.description = conf['description']
        self.welcome_text = conf['welcome_text']
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
        self.email_invite_subject = conf['email_invite_subject']
        self.email_invite_content = conf['email_invite_content']
        self.email_reminder_subject = conf['email_reminder_subject']
        self.email_reminder_content = conf['email_reminder_content']

    # def __repr__(self): #TODO implement debug text
    #     return f"<Question qid={self.qid} gid={self.gid} title={self.title} name={self.code} options={self.options}>"
