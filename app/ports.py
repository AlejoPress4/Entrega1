from abc import ABC, abstractmethod


class RepositorioEquipos(ABC):
    @abstractmethod
    def guardar(self, equipo):
        pass

    @abstractmethod
    def buscar_por_id(self, equipo_id):
        pass

    @abstractmethod
    def listar_todos(self):
        pass


class RepositorioEstudiantes(ABC):
    @abstractmethod
    def guardar(self, estudiante):
        pass

    @abstractmethod
    def buscar_por_id(self, estudiante_id):
        pass

    @abstractmethod
    def listar_todos(self):
        pass


class RepositorioPrestamos(ABC):
    @abstractmethod
    def guardar(self, prestamo):
        pass

    @abstractmethod
    def buscar_por_id(self, prestamo_id):
        pass

    @abstractmethod
    def listar_todos(self):
        pass


class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje, destinatario):
        pass


class ProveedorFecha(ABC):
    @abstractmethod
    def obtener_fecha_actual(self):
        pass
