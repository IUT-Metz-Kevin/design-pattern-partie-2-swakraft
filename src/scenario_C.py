import abc

class Command(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        raise NotImplementedError

class Tv:
    def __init__(self):
        self.chaine = "0"

    def allumer(self):
        print('TV ON')
    
    def eteindre(self):
        print('bye ')
    
    def open(self, app_name: str):
        print(f"Ouverture de {app_name}")
    

class AllumerTv(Command):
    def __init__(self, tv: Tv):
        self.tv = tv

    def execute(self):
        self.tv.allumer()

class Eteindre(Command):
    def __init__(self, tv: Tv):
        self.tv = tv

    def execute(self):
        self.tv.eteindre()

class AllumerNetflix(Command):
    def __init__(self, tv: Tv):
        self.tv = tv

    def execute(self):
        self.tv.open('Netflix')

class AmazonPrime(Command):
    def __init__(self, tv: Tv):
        self.tv = tv

    def execute(self):
        self.tv.open('Amazon Prime')

class DisneyPlus(Command):
    def __init__(self, tv: Tv):
        self.tv = tv

    def execute(self):
        self.tv.open('Disney +')

class NumChaine(Command):
    def __init__(self, tv: Tv):
        self.tv = tv

    def execute(self):
        self.tv.open(self.tv.chaine)

class Remote():
    def __init__(self, tv: Tv):
        self.tv = tv
        self.pile: list[Command] = []
    
    def on(self):
        self.tv.allumer()
    
    def off(self):
        self.tv.eteindre()

    def netflix(self):
        command = AllumerNetflix(self.tv)
        self.pile.append(command)
        command.execute()
    
    def amazon_prime(self):
        command = AmazonPrime(self.tv)
        self.pile.append(command)
        command.execute()
    
    def disney_plus(self):
        command = DisneyPlus(self.tv)
        self.pile.append(command)
        command.execute()
    
    def num_chaine(self):
        command = NumChaine(self.tv)
        self.pile.append(command)
        command.execute()
    
    def retour(self):
        self.pile.pop()
        self.pile[-1].execute()

tv = Tv()
remote = Remote(tv)

remote.on()
remote.netflix()
remote.amazon_prime()
remote.retour()