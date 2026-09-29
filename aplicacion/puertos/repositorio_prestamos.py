from abc import ABC, abstractmethod
class RepositorioPrestamos(ABC):
    @abstractmethod
    def contar_activos_de_estudiante(self, id_estudiante): pass
    @abstractmethod
    def guardar(self, prestamo): pass
    @abstractmethod
    def buscar_por_id(self, id_prestamo): pass
