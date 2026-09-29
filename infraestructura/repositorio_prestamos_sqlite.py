import sqlite3
from datetime import datetime
from aplicacion.puertos.repositorio_prestamos import RepositorioPrestamos
from dominio.prestamo import Prestamo

class RepositorioPrestamosSQLite(RepositorioPrestamos):
    def __init__(self, conexion, repo_estudiantes, repo_equipos):
        self.conexion = conexion
        self.repo_estudiantes = repo_estudiantes
        self.repo_equipos = repo_equipos

    def contar_activos_de_estudiante(self, id_estudiante):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM prestamos WHERE id_estudiante = ? AND activo = 1", (id_estudiante,))
        return cursor.fetchone()[0]

    def buscar_por_id(self, id_prestamo):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT id, id_estudiante, id_equipo, fecha_prestamo, fecha_limite, activo, fecha_devolucion, multa_generada FROM prestamos WHERE id = ?", (id_prestamo,))
        fila = cursor.fetchone()
        if fila:
            estudiante = self.repo_estudiantes.buscar_por_id(fila[1])
            equipo = self.repo_equipos.buscar_por_id(fila[2])
            fecha_prestamo = datetime.strptime(fila[3], "%Y-%m-%d").date()
            fecha_limite = datetime.strptime(fila[4], "%Y-%m-%d").date()
            prestamo = Prestamo(fila[0], estudiante, equipo, fecha_prestamo, fecha_limite)
            prestamo.activo = bool(fila[5])
            if fila[6]:
                prestamo.fecha_devolucion = datetime.strptime(fila[6], "%Y-%m-%d").date()
            prestamo.multa_generada = fila[7]
            return prestamo
        return None

    def guardar(self, prestamo):
        cursor = self.conexion.cursor()
        fp = prestamo.fecha_prestamo.strftime("%Y-%m-%d")
        fl = prestamo.fecha_limite.strftime("%Y-%m-%d")
        fd = prestamo.fecha_devolucion.strftime("%Y-%m-%d") if prestamo.fecha_devolucion else None
        cursor.execute("INSERT OR REPLACE INTO prestamos (id, id_estudiante, id_equipo, fecha_prestamo, fecha_limite, activo, fecha_devolucion, multa_generada) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                       (prestamo.id, prestamo.estudiante.id, prestamo.equipo.id, fp, fl, int(prestamo.activo), fd, prestamo.multa_generada))
        self.conexion.commit()
