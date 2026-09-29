from abc import ABC, abstractmethod
class RepositorioEstudiantes(ABC):
    @abstractmethod
    def buscar_por_id(self, id_estudiante): pass
    @abstractmethod
    def guardar(self, estudiante): pass
