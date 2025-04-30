import abc
from typing import Optional

class Handler(metaclass=abc.ABCMeta):
    __slots__ = ('next',)

    def __init__(self, next: Optional['Handler']):
        self.next = next

    def set_next(self, next: 'Handler'):
        self.next = next
    
    @abc.abstractmethod
    def handle(self, pret: 'Pret'):
        pass

    def forward(self, pret: 'Pret'):
        if self.next:
            self.next.handle(pret)
        
        else:
            raise Exception("Wow, aucun handler n'a été défini pour la suite ! :(")


class EmployeeHandler(Handler):
    def __init__(self, next: Optional[Handler] = None):
        super().__init__(next)
        
    def handle(self, pret: "Pret"):
        if (pret.montant > 100_000):
            self.forward(pret)
        
        else:
            print(f"{self.__class__.__name__} : Je gère")

class ManagerHandler(Handler):
    def __init__(self, next: Optional[Handler] = None):
        super().__init__(next)
        
    def handle(self, pret: "Pret"):
        if (pret.montant > 500_000):
            self.forward(pret)

        else:
            print(f"{self.__class__.__name__} : Je gère")

class DptBossHandler(Handler):
    def __init__(self, next: Optional[Handler] = None):
        super().__init__(next)
        
    def handle(self, pret: "Pret"):
        if (pret.montant > 10_000_000):
            self.forward(pret)
        
        else:
            print(f"{self.__class__.__name__} : Je gère")

class BigBossHandler(Handler):
    def __init__(self, next: Optional[Handler] = None):
        super().__init__(next)
        
    def handle(self, pret: "Pret"):
        print(f"{self.__class__.__name__} : Je gère")
    
class Pret:
    __slots__ = ('montant',)
    def __init__(self, montant: int) -> None:
        self.montant = montant

bigboss = BigBossHandler()
dptboss = DptBossHandler(bigboss)
manager = ManagerHandler(dptboss)
employee = EmployeeHandler(manager)

for i in range(0, 10_200_000, 100_000):
    employee.handle(Pret(i))