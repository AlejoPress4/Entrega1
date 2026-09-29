import sqlite3

from app.ports import RepositorioEquipos, RepositorioEstudiantes, RepositorioPrestamos, RepositorioCategoriasEquipo
from domain.categoria_equipo import CategoriaEquipo
from domain.equipo import Equipo
from domain.estudiante import Estudiante
from domain.prestamo import Prestamo


class RepositorioEquiposSQL(RepositorioEquipos):
    def __init__(self, nombre_db="prestamos.db"):
        self.nombre_db = nombre_db
        self.connection = sqlite3.connect(self.nombre_db)
        self.connection.row_factory = sqlite3.Row
        self._crear_tabla()

    def _crear_tabla(self):
        with self.connection as conn:
            conn.execute("PRAGMA foreign_keys = ON")
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS equipos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    categoria_id INTEGER,
                    estado TEXT,
                    FOREIGN KEY (categoria_id) REFERENCES categorias_equipo(id)
                )
                """
            )

    def guardar(self, equipo):
        if equipo.id is None:
            cursor = self.connection.execute(
                """
                INSERT INTO equipos (nombre, categoria_id, estado)
                VALUES (?, ?, ?)
                """,
                (equipo.nombre, equipo.categoria_id, equipo.estado),
            )
            equipo.id = cursor.lastrowid
        else:
            self.connection.execute(
                """
                UPDATE equipos
                SET nombre = ?, categoria_id = ?, estado = ?
                WHERE id = ?
                """,
                (equipo.nombre, equipo.categoria_id, equipo.estado, equipo.id),
            )
        self.connection.commit()
        return equipo

    def buscar_por_id(self, equipo_id):
        row = self.connection.execute("SELECT * FROM equipos WHERE id = ?", (equipo_id,)).fetchone()
        if row is None:
            return None

        equipo = Equipo(row["nombre"], row["categoria_id"])
        equipo.id = row["id"]
        equipo.estado = row["estado"]
        return equipo

    def listar_todos(self):
        rows = self.connection.execute("SELECT * FROM equipos ORDER BY id").fetchall()
        equipos = []
        for row in rows:
            equipo = Equipo(row["nombre"], row["categoria_id"])
            equipo.id = row["id"]
            equipo.estado = row["estado"]
            equipos.append(equipo)
        return equipos


class RepositorioEstudiantesSQL(RepositorioEstudiantes):
    def __init__(self, nombre_db="prestamos.db"):
        self.nombre_db = nombre_db
        self.connection = sqlite3.connect(self.nombre_db)
        self.connection.row_factory = sqlite3.Row
        self._crear_tabla()

    def _crear_tabla(self):
        with self.connection as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS estudiantes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    edad INTEGER,
                    carrera TEXT
                )
                """
            )

    def guardar(self, estudiante):
        if estudiante.id is None:
            cursor = self.connection.execute(
                """
                INSERT INTO estudiantes (nombre, edad, carrera)
                VALUES (?, ?, ?)
                """,
                (estudiante.nombre, estudiante.edad, estudiante.carrera),
            )
            estudiante.id = cursor.lastrowid
        else:
            self.connection.execute(
                """
                UPDATE estudiantes
                SET nombre = ?, edad = ?, carrera = ?
                WHERE id = ?
                """,
                (estudiante.nombre, estudiante.edad, estudiante.carrera, estudiante.id),
            )
        self.connection.commit()
        return estudiante

    def buscar_por_id(self, estudiante_id):
        row = self.connection.execute("SELECT * FROM estudiantes WHERE id = ?", (estudiante_id,)).fetchone()
        if row is None:
            return None

        estudiante = Estudiante(row["nombre"], row["edad"], row["carrera"])
        estudiante.id = row["id"]
        return estudiante

    def listar_todos(self):
        rows = self.connection.execute("SELECT * FROM estudiantes ORDER BY id").fetchall()
        estudiantes = []
        for row in rows:
            estudiante = Estudiante(row["nombre"], row["edad"], row["carrera"])
            estudiante.id = row["id"]
            estudiantes.append(estudiante)
        return estudiantes


class RepositorioPrestamosSQL(RepositorioPrestamos):
    def __init__(self, nombre_db="prestamos.db"):
        self.nombre_db = nombre_db
        self.connection = sqlite3.connect(self.nombre_db)
        self.connection.row_factory = sqlite3.Row
        self._crear_tabla()

    def _crear_tabla(self):
        with self.connection as conn:
            conn.execute("PRAGMA foreign_keys = ON")
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS prestamos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    equipo_id INTEGER,
                    estudiante_id INTEGER,
                    fecha_prestamo TEXT,
                    fecha_devolucion TEXT,
                    estado TEXT,
                    FOREIGN KEY (equipo_id) REFERENCES equipos(id),
                    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id)
                )
                """
            )

    def guardar(self, prestamo):
        if prestamo.id is None:
            cursor = self.connection.execute(
                """
                INSERT INTO prestamos (equipo_id, estudiante_id, fecha_prestamo, fecha_devolucion, estado)
                VALUES (?, ?, ?, ?, ?)
                """,
                (prestamo.equipo_id, prestamo.estudiante_id, prestamo.fecha_prestamo, prestamo.fecha_devolucion, prestamo.estado),
            )
            prestamo.id = cursor.lastrowid
        else:
            self.connection.execute(
                """
                UPDATE prestamos
                SET equipo_id = ?, estudiante_id = ?, fecha_prestamo = ?, fecha_devolucion = ?, estado = ?
                WHERE id = ?
                """,
                (prestamo.equipo_id, prestamo.estudiante_id, prestamo.fecha_prestamo, prestamo.fecha_devolucion, prestamo.estado, prestamo.id),
            )
        self.connection.commit()
        return prestamo

    def buscar_por_id(self, prestamo_id):
        row = self.connection.execute("SELECT * FROM prestamos WHERE id = ?", (prestamo_id,)).fetchone()
        if row is None:
            return None

        prestamo = Prestamo(row["equipo_id"], row["estudiante_id"], row["fecha_prestamo"], row["fecha_devolucion"])
        prestamo.id = row["id"]
        prestamo.estado = row["estado"]
        return prestamo

    def listar_todos(self):
        rows = self.connection.execute("SELECT * FROM prestamos ORDER BY id").fetchall()
        prestamos = []
        for row in rows:
            prestamo = Prestamo(row["equipo_id"], row["estudiante_id"], row["fecha_prestamo"], row["fecha_devolucion"])
            prestamo.id = row["id"]
            prestamo.estado = row["estado"]
            prestamos.append(prestamo)
        return prestamos


class RepositorioCategoriasEquipoSQL(RepositorioCategoriasEquipo):
    def __init__(self, nombre_db="categorias.db"):
        self.nombre_db = nombre_db
        self.connection = sqlite3.connect(self.nombre_db)
        self.connection.row_factory = sqlite3.Row
        self._crear_tabla()

    def _crear_tabla(self):
        with self.connection as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS categorias_equipo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    cuota_diaria REAL,
                    plazo_maximo_dias INTEGER
                )
                """
            )

    def guardar(self, categoria):
        if categoria.id is None:
            cursor = self.connection.execute(
                """
                INSERT INTO categorias_equipo (nombre, cuota_diaria, plazo_maximo_dias)
                VALUES (?, ?, ?)
                """,
                (categoria.nombre, categoria.cuota_diaria, categoria.plazo_maximo_dias),
            )
            categoria.id = cursor.lastrowid
        else:
            self.connection.execute(
                """
                UPDATE categorias_equipo
                SET nombre = ?, cuota_diaria = ?, plazo_maximo_dias = ?
                WHERE id = ?
                """,
                (categoria.nombre, categoria.cuota_diaria, categoria.plazo_maximo_dias, categoria.id),
            )
        self.connection.commit()
        return categoria

    def buscar_por_id(self, categoria_id):
        row = self.connection.execute("SELECT * FROM categorias_equipo WHERE id = ?", (categoria_id,)).fetchone()
        if row is None:
            return None

        categoria = CategoriaEquipo(row["nombre"], row["cuota_diaria"], row["plazo_maximo_dias"])
        categoria.id = row["id"]
        return categoria

    def listar_todos(self):
        rows = self.connection.execute("SELECT * FROM categorias_equipo ORDER BY id").fetchall()
        categorias = []
        for row in rows:
            categoria = CategoriaEquipo(row["nombre"], row["cuota_diaria"], row["plazo_maximo_dias"])
            categoria.id = row["id"]
            categorias.append(categoria)
        return categorias

    def actualizar(self, categoria_id, categoria_actualizada):
        categoria_actualizada.id = categoria_id
        return self.guardar(categoria_actualizada)

    def eliminar(self, categoria_id):
        cursor = self.connection.execute("DELETE FROM categorias_equipo WHERE id = ?", (categoria_id,))
        self.connection.commit()
        return cursor.rowcount > 0
