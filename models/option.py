class Option:
    def __init__(self, value, code, order, description, image):
        self.value = value
        self.code = code
        self.order = order
        self.description = description
        self.image = image

    def set_order(self, order):
        self.order = order
        self.code = f"A{order+1}"
        
    def set_description(self, description):
        self.description = f"<p><strong>{self.value}</strong></p>"
        for line in description.split('\n'):
            self.description += f"<p>{line}</p>\n"

    def __repr__(self):
        return f"<Candidat name={self.value} concentration={self.code}>"
