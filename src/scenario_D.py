import abc

class Vetement:
    __slots__ = ('couleur', 'tissu', 'salete')
    def __init__ (self, couleur: str, tissu: str, salete: int):
        self.couleur = couleur
        self.tissu = tissu
        self.salete = salete

class TriStrategy(abc.ABC):
    @abc.abstractmethod
    def trier(self, liste_vetements: list[Vetement]):
        raise NotImplementedError

class TriParCouleur(TriStrategy):
    def trier(self, liste_vetements: list[Vetement]):
        return sorted(liste_vetements, key=lambda x: x.couleur)

class TriParTissu(TriStrategy):
    def trier(self, liste_vetements: list[Vetement]):
        return sorted(liste_vetements, key=lambda x: x.tissu)

class TriParSalete(TriStrategy):
    def trier(self, liste_vetements: list[Vetement]):
        return sorted(liste_vetements, key=lambda x: x.salete)

class Lavomatique:
    def __init__(self, strategy: TriStrategy):
        self.strategy = strategy

    def trier_vetements(self, liste_vetements: list[Vetement]) -> list[Vetement]:
        return self.strategy.trier(liste_vetements)