class Option:
    def __init__(self, nom, order, description, image, promotion="", concentration=""):
        self.nom = nom
        self.promotion = promotion
        self.concentration = concentration
        self.order = order
        self.code = f"A{self.order + 1}"
        self.image = image
        self.description = ""
        self.set_description(description)

    def set_order(self, order):
        self.order = order
        self.code = f"A{order+1}"
        
    def set_description(self, description):
        if self.concentration and self.promotion:
            self.description = f"<p><strong>{self.nom} ({self.concentration}, {self.promotion})</strong></p>"
        elif self.concentration:
            self.description = f"<p><strong>{self.nom} ({self.concentration})</strong></p>"
        else:
            self.description = f"<p><strong>{self.nom}</strong></p>"
        for line in description.split('\n'):
            self.description += f"<p>{line}</p>\n"

    @staticmethod
    def add_chaise(order):
        return Option(
            nom="La chaise",
            order=order,
            description=(
                "La chaise ne vous laisseras pas tomber. Elle offre un bon support et connait bien son dossier. "
                "Elle connait sa place et ne s'exprime pas quand ce n'est pas son tour."
            ),
            image="https://vote.ageg.ca/images/chaise.jpg"
        )


    def __repr__(self):
        return f"<Candidat name={self.nom} concentration={self.code}>"
