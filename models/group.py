import itertools

class Group:
    uid = itertools.count()
    def __init__(self, name, description=""):
        self.order = next(Group.uid)
        self.gid = self.order + 420
        self.name = name
        self.description = description
    
    def __repr__(self):
        return f"<Group gid={self.gid} name={self.name} order={self.order}>"