class Subquestion:
    def __init__(self, qid, parent, gid, code, value, order, type='T'):
        self.qid = qid
        self.parent = parent
        self.gid = gid
        self.code = code
        self.value = value
        self.order = order
        self.type = type
        self.answers = []
    
    def add_answer(self, answer):
        self.answers.append(answer)

    def answer_count(self):
        return len(self.answers)

    def __repr__(self):
        return "<Subquestion qid={qid}, parent={parent}, gid={gid}, code={code}, value={value}, order={order}, type={type}>".format(qid=self.qid, parent=self.parent, gid=self.gid, code=self.code, value=self.value, order=self.order, type=self.type)
