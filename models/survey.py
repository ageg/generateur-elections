class Survey:
    def __init__(self, conf):
        self.admin = conf['admin']
        self.admin_email = conf['admin_email']
        self.expires = conf['expiry']
        self.title = conf['title']
        self.description = conf['description']
        self.welcome_text = conf['welcome_text']
        self.empty_groups = {}
        if any(group['unused_posts'] for group in conf['groups'] if group['type'] == "exec" or group['type'] == "promo" ):
            for group in conf['groups']:
                if group['type'] == "exec" and group['unused_posts']:
                    self.empty_groups[group['semester']] = []
                    for post in conf['postes_exec'].keys():
                        if post in group['unused_posts']:
                            self.empty_groups[group['semester']].append(conf['postes_exec'][post])
                if group['type'] == "promo" and group['unused_posts']:
                    self.empty_groups[group['semester']] = []
                    for post in conf['postes_promo'].keys():
                        if post in group['unused_posts']:
                            self.empty_groups[group['semester']].append(conf['postes_promo'][post])
        self.empty_end_text = conf['empty_end_text']
        self.filled_end_text = conf['filled_end_text']
        self.email_invite_subject = conf['email_invite_subject']
        self.email_invite_content = conf['email_invite_content']
        self.email_reminder_subject = conf['email_reminder_subject']
        self.email_reminder_content = conf['email_reminder_content']

    # def __repr__(self): #TODO implement debug text
    #     return f"<Question qid={self.qid} gid={self.gid} title={self.title} name={self.code} options={self.options}>"
