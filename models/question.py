import itertools


class Question:
    uid = itertools.count()

    def __init__(self, code, gid, title, attributes=None, qtype='R', order=0):
        if attributes is None:
            attributes = []
        self.qid = next(Question.uid) + 400
        self.gid = gid
        self.code = code
        self.answers = []
        self.options = []
        self.title = title
        self.attributes = attributes
        self.type = qtype
        self.order = order
        if qtype == "F":
            self.help = 'Veuillez voter "Oui", "Non", "Non confiance" ou "Sans réponse" pour chaque candidat.'
        elif qtype == 'L':
            self.help = 'Pour ce poste, veuillez voter pour un des candidats ou "Sans réponse".'
        elif qtype == 'R':
            self.help = 'Pour ce poste, veuillez placer les candidats dans l\'ordre de préférence.'
        else:
            self.help = ""

    def add_option(self, option):
        self.options.append(option)

    def option_count(self):
        return len(self.options)
    
    def add_answer(self, answer):
        self.answers.append(answer)

    def answer_count(self):
        return len(self.answers)
    
    def __repr__(self):
        return f"<Question qid={self.qid} gid={self.gid} title={self.title} name={self.code} options={self.options}>"
