from abc import ABC, abstractmethod
class Notificador(ABC):
    @abstractmethod
    def notificar(self, id_estudiante, mensaje): pass
