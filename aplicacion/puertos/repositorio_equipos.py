from abc import ABC, abstractmethod
class RepositorioEquipos(ABC):
    @abstractmethod
    def buscar_por_id(self, id_equipo): pass
    @abstractmethod
    def guardar(self, equipo): pass
