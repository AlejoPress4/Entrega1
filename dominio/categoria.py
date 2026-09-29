from abc import ABC, abstractmethod
class Categoria(ABC):
    @property
    @abstractmethod
    def nombre(self): pass
    @property
    @abstractmethod
    def plazo_dias(self): pass
    @property
    @abstractmethod
    def tarifa_diaria(self): pass
