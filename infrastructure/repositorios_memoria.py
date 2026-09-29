from app.ports import RepositorioEquipos, RepositorioEstudiantes, RepositorioPrestamos


class RepositorioEquiposMemoria(RepositorioEquipos):
    def __init__(self):
        self._equipos = {}

    def guardar(self, equipo):
        """Guarda o actualiza un equipo en memoria."""
        self._equipos[equipo.id] = equipo
        return equipo

    def buscar_por_id(self, equipo_id):
        """Busca un equipo por su identificador."""
        return self._equipos.get(equipo_id)

    def listar_todos(self):
        """Devuelve todos los equipos almacenados."""
        return list(self._equipos.values())


class RepositorioEstudiantesMemoria(RepositorioEstudiantes):
    def __init__(self):
        self._estudiantes = {}

    def guardar(self, estudiante):
        """Guarda o actualiza un estudiante en memoria."""
        self._estudiantes[estudiante.id] = estudiante
        return estudiante

    def buscar_por_id(self, estudiante_id):
        """Busca un estudiante por su identificador."""
        return self._estudiantes.get(estudiante_id)

    def listar_todos(self):
        """Devuelve todos los estudiantes almacenados."""
        return list(self._estudiantes.values())


class RepositorioPrestamosMemoria(RepositorioPrestamos):
    def __init__(self):
        self._prestamos = {}

    def guardar(self, prestamo):
        """Guarda o actualiza un préstamo en memoria."""
        self._prestamos[prestamo.id] = prestamo
        return prestamo

    def buscar_por_id(self, prestamo_id):
        """Busca un préstamo por su identificador."""
        return self._prestamos.get(prestamo_id)

    def listar_todos(self):
        """Devuelve todos los préstamos almacenados."""
        return list(self._prestamos.values())
