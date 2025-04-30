import abc
from datetime import datetime
from typing import Literal

class Iterator(metaclass=abc.ABCMeta):
    __slots__ = 'livres', 'index'

    def __init__(self):
        self.index = 0

    def has_next(self) -> bool:
        raise NotImplementedError

    def __iter__(self):
        return self

    def __next__(self) -> 'Livre':
        if self.index < len(self.livres):
            livre = self.livres[self.index]
            self.index += 1
            return livre
        
        raise StopIteration
    
class Collection:
    def __init__(self, livres: list['Livre']):
        self.livres = livres

    def get_iterator(self, mode: Literal["nom", "auteur", "genre", "date"]) -> Iterator:
        match mode:
            case "nom":
                return IteratorParNom(self.livres)
            
            case "auteur":
                return IteratorParAuteur(self.livres)
            
            case "genre":
                return IteratorParGenreLitteraire(self.livres)
            
            case "date":
                return IteratorParDate(self.livres)
            
            case _:
                raise ValueError("Mode de tri inconnu")

class IteratorParNom(Iterator):
    def __init__(self, livres: list['Livre']):
        super().__init__()
        self.livres = sorted(livres, key=lambda l: l.titre)

class IteratorParAuteur(Iterator):
    def __init__(self, livres: list['Livre']):
        super().__init__()
        self.livres = sorted(livres, key=lambda l: l.auteur)

class IteratorParGenreLitteraire(Iterator):
     def __init__(self, livres: list['Livre']):
        super().__init__()
        self.livres = sorted(livres, key=lambda l: l.genre)

class IteratorParDate(Iterator):
     def __init__(self, livres: list['Livre']):
        super().__init__()
        self.livres = sorted(livres, key=lambda l: l.date)

class Livre:
    __slots__ = ('titre', 'auteur', 'genre', 'date')

    def __init__(self, titre: str, auteur: str, genre: str, date: datetime):
        self.titre = titre
        self.auteur = auteur
        self.genre = genre
        self.date = date