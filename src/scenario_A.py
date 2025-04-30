from enum import Enum
import abc

class EtatJoueur(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def attaquer(self):
        raise NotImplementedError

    @abc.abstractmethod
    def sauter(self):
        raise NotImplementedError

    @abc.abstractmethod
    def idle(self):
        raise NotImplementedError

    @abc.abstractmethod
    def deplacer(self):
        raise NotImplementedError

class EtatAttaque(EtatJoueur):
    def attaquer(self):
        print("Attaque")
    
    def sauter(self):
        print("non")
    
    def idle(self):
        print("ne fait plus rien")
    
    def deplacer(self):
        print("non")

class EtatIdle(EtatJoueur):
    def attaquer(self):
        print("Attaque")
    
    def sauter(self):
        print("Saute")
    
    def idle(self):
        print("ne fait plus rien")
    
    def deplacer(self):
        print("Se déplace")

class EtatDeplacement(EtatJoueur):
    def attaquer(self):
        print("Attaque")
    
    def sauter(self):
        print("Saute")
    
    def idle(self):
        print("ne fait plus rien")
    
    def deplacer(self):
        print("non")

class EtatEtourdi(EtatJoueur):
    def attaquer(self):
        print("non")
    
    def sauter(self):
        print("non")
    
    def idle(self):
        print("non")
    
    def deplacer(self):
        print("non")

class EtatSaute(EtatJoueur):
    def attaquer(self):
        print("Attaque")
    
    def sauter(self):
        print("Saute")
    
    def idle(self):
        print("ne fait plus rien")
    
    def deplacer(self):
        print("non")

class Joueur:
    def __init__(self):
        self.etat: EtatJoueur = EtatIdle()
    
    def attaquer(self):
        self.etat.attaquer()
        self.etat = EtatAttaque()
    
    def sauter(self):
        self.etat.sauter()
        self.etat = EtatSaute()
    
    def idle(self):
        self.etat.idle()
        self.etat = EtatIdle()
    
    def deplacer(self):
        self.etat.deplacer()
        self.etat = EtatDeplacement()
    
    def etourdir(self):
        self.etat = EtatEtourdi()

joueur = Joueur()