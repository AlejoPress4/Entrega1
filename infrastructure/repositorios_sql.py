import sqlite3

from app.ports import RepositorioEquipos, RepositorioEstudiantes, RepositorioPrestamos


class RepositorioEquiposSQL(RepositorioEquipos):
    def __init__(self, nombre_db="prestamos.db"):
        self.nombre_db = nombre_db
        self.connection = sqlite3.connect(self.nombre_db)

    def guardar(self, equipo):
        pass

    def buscar_por_id(self, equipo_id):
        pass

    def listar_todos(self):
        pass


class RepositorioEstudiantesSQL(RepositorioEstudiantes):
    def __init__(self, nombre_db="prestamos.db"):
        self.nombre_db = nombre_db
        self.connection = sqlite3.connect(self.nombre_db)

    def guardar(self, estudiante):
        pass

    def buscar_por_id(self, estudiante_id):
        pass

    def listar_todos(self):
        pass


class RepositorioPrestamosSQL(RepositorioPrestamos):
    def __init__(self, nombre_db="prestamos.db"):
        self.nombre_db = nombre_db
        self.connection = sqlite3.connect(self.nombre_db)

    def guardar(self, prestamo):
        pass

    def buscar_por_id(self, prestamo_id):
        pass

    def listar_todos(self):
        pass