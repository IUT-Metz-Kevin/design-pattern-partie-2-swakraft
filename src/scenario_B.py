import abc
from typing import Optional

class TourDeControle(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def demander_atterrissage(self, avion: 'Avion'):
        pass

    @abc.abstractmethod
    def demander_decollage(self, avion: 'Avion'):
        pass

class Tour(TourDeControle):
    __slots__ = ('_pistes',)
    def __init__(self, pistes: Optional[list[str]] = None) -> None:
        self.pistes = pistes or []
    
    @property
    def pistes(self) -> Optional[list[str]]:
        return self._pistes

    @pistes.setter
    def pistes(self, pistes: list[str]):
        self._pistes = pistes
    
    def demander_atterrissage(self, avion):
        ...

    def demander_decollage(self, avion):
        ...

class Avion:
    __slots__ = ('_nom', '_tour',)
    def __init__(self, nom: str, tour: TourDeControle) -> None:
        self.nom = nom
        self.tour = tour

    @property
    def tour(self) -> TourDeControle:
        return self._tour

    @tour.setter
    def tour(self, tour: TourDeControle):
        self._tour = tour

    @property
    def nom(self) -> str:
        return self._nom

    @nom.setter
    def nom(self, nom: str):
        self._nom = nom

    def demander_atterrissage(self):
        return self.tour.demander_atterrissage(self)
    
    def demander_decollage(self):
        return self.tour.demander_decollage(self)