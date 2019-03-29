class Group:
    def __init__(self, id, name, description=""):
        self.gid = id + 420
        self.order = id
        self.name = name
        self.description = description
    
    def __repr__(self):
        return "<Group gid={gid} name={name} order={order}>".format(gid=self.gid, name=self.name, order=self.order)