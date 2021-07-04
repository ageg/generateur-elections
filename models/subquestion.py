from models.question import Question


class Subquestion:
    def __init__(self, parent, gid, code, value, order, qtype='T'):
        self.qid = next(Question.uid) + 400
        self.parent = parent
        self.gid = gid
        self.code = code
        self.value = value
        self.order = order
        self.qtype = qtype
        self.answers = []
    
    def add_answer(self, answer):
        self.answers.append(answer)

    def answer_count(self):
        return len(self.answers)

    def __repr__(self):
        return (f"<Subquestion qid={self.qid}, parent={self.parent}, gid={self.gid}, code={self.code},"
                f" value={self.value}, order={self.order}, type={self.qtype}>")
