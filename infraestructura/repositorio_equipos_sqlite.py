import sqlite3
from aplicacion.puertos.repositorio_equipos import RepositorioEquipos
from dominio.equipo import Equipo
from dominio.categoria_portatil import CategoriaPortatil
from dominio.categoria_camara import CategoriaCamara
from dominio.categoria_kit_robotica import CategoriaKitRobotica

class RepositorioEquiposSQLite(RepositorioEquipos):
    def __init__(self, conexion, categorias_adicionales=None):
        self.conexion = conexion
        self.categorias = {
            "PORTATIL": CategoriaPortatil(),
            "CAMARA": CategoriaCamara(),
            "KIT_ROBOTICA": CategoriaKitRobotica()
        }
        if categorias_adicionales:
            self.categorias.update(categorias_adicionales)

    def buscar_por_id(self, id_equipo):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT id, categoria, estado FROM equipos WHERE id = ?", (id_equipo,))
        fila = cursor.fetchone()
        if fila:
            categoria_nombre = fila[1]
            categoria = self.categorias.get(categoria_nombre)
            equipo = Equipo(fila[0], categoria)
            equipo.estado = fila[2]
            return equipo
        return None

    def guardar(self, equipo):
        cursor = self.conexion.cursor()
        cursor.execute("INSERT OR REPLACE INTO equipos (id, categoria, estado) VALUES (?, ?, ?)", 
                       (equipo.id, equipo.categoria.nombre, equipo.estado))
        self.conexion.commit()
