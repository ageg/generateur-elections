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

    @staticmethod
    def add_salade(order):
        return Option(
            nom="La salade de patates",
            order=order,
            description=(
                "La salade de patates est énergique. "
                "Elle te soutient. "
                "Elle comble les besoins des membres et elle est toujours bonne en lendemain de veille."
            ),
            image="https://vote.ageg.ca/images/salade-de-patate.jpg"
        )

    @staticmethod
    def add_pilon(order):
        return Option(
            nom="Le pilon de poulet",
            order=order,
            description=(
                "Tel un porteur du bandana, le pilon de dinde ne manque jamais l'Oktoberfest. "
                "Il est fort et sais comment soutenir les membres. "
                "Avec sa haute teneur en protéines, il aura toujours l'énergie nécessaire pour mener à bien les projets. "
                "Plein de surprises, il connait sa place et ne s'exprime pas quand ce n'est pas son tour. "
                "Le pilon de dinde de l'Oktoberfest est l'option de choix afin de laisser un poste inoccupé."
                ""
            ),
            image="https://vote.ageg.ca/images/pilon-poulet.jpg"
        )

    def __repr__(self):
        return f"<Candidat name={self.value} concentration={self.code}>"
