import sqlite3
from aplicacion.puertos.repositorio_estudiantes import RepositorioEstudiantes
from dominio.estudiante import Estudiante

class RepositorioEstudiantesSQLite(RepositorioEstudiantes):
    def __init__(self, conexion):
        self.conexion = conexion

    def buscar_por_id(self, id_estudiante):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT id, nombre, multa_pendiente FROM estudiantes WHERE id = ?", (id_estudiante,))
        fila = cursor.fetchone()
        if fila:
            estudiante = Estudiante(fila[0], fila[1])
            estudiante.multa_pendiente = bool(fila[2])
            return estudiante
        return None

    def guardar(self, estudiante):
        cursor = self.conexion.cursor()
        cursor.execute("INSERT OR REPLACE INTO estudiantes (id, nombre, multa_pendiente) VALUES (?, ?, ?)", 
                       (estudiante.id, estudiante.nombre, int(estudiante.multa_pendiente)))
        self.conexion.commit()
