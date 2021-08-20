class Option:
    def __init__(self, nom, order, description, image, promotion="", concentration=""):
        self.value = nom
        self.promotion = promotion
        self.concentration = concentration
        self.order = order
        self.code = f"A{self.order + 1}"
        self.image = image
        self.description = description

    def set_order(self, order):
        self.order = order
        self.code = f"A{order+1}"


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
        return f"<Candidat name={self.value} concentration={self.code}>"
