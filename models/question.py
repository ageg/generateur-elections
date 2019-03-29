from .attribute import Attribute

class Question:
    def __init__(self, id, code, gid, title, attributes):
        self.qid = id + 300
        self.gid = gid
        self.code = code
        self.options = []
        self.title = title
        self.attributes = attributes

    def add_option(self, option):
        self.options.append(option)

    def option_count(self):
        return len(self.options)
    
    def __repr__(self):
        return "<Question qid={qid} gid={gid} title={title} name={name} options={options}>".format(qid=self.qid, gid=self.gid, title=self.title,
        name = self.name, options=self.options)
