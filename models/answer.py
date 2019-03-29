class Answer:
    def __init__(self, qid, value, code, order=1):
        self.qid = qid
        self.value = value
        self.code = code
        self.order = order

    def __repr__(self):
        return "<Answer qid={qid} value={value} code={code} order={order}>".format(qid=self.qid, value=self.value, code=self.code, order=self.order)
