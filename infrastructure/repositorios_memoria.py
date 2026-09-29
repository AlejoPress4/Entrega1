from app.ports import RepositorioEquipos, RepositorioEstudiantes, RepositorioPrestamos, RepositorioCategoriasEquipo


class RepositorioEquiposMemoria(RepositorioEquipos):
    def __init__(self):
        self._equipos = {}
        self._ultimo_id = 0

    def guardar(self, equipo):
        """Guarda o actualiza un equipo en memoria."""
        if equipo.id is None:
            self._ultimo_id += 1
            equipo.id = self._ultimo_id
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
        self._ultimo_id = 0

    def guardar(self, estudiante):
        """Guarda o actualiza un estudiante en memoria."""
        if estudiante.id is None:
            self._ultimo_id += 1
            estudiante.id = self._ultimo_id
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
        self._ultimo_id = 0

    def guardar(self, prestamo):
        """Guarda o actualiza un préstamo en memoria."""
        if prestamo.id is None:
            self._ultimo_id += 1
            prestamo.id = self._ultimo_id
        self._prestamos[prestamo.id] = prestamo
        return prestamo

    def buscar_por_id(self, prestamo_id):
        """Busca un préstamo por su identificador."""
        return self._prestamos.get(prestamo_id)

    def listar_todos(self):
        """Devuelve todos los préstamos almacenados."""
        return list(self._prestamos.values())


class RepositorioCategoriasEquipoMemoria(RepositorioCategoriasEquipo):
    def __init__(self):
        self._categorias = {}
        self._ultimo_id = 0

    def guardar(self, categoria):
        """Guarda o actualiza una categoría de equipo."""
        if categoria.id is None:
            self._ultimo_id += 1
            categoria.id = self._ultimo_id
        self._categorias[categoria.id] = categoria
        return categoria

    def buscar_por_id(self, categoria_id):
        """Busca una categoría por su identificador."""
        return self._categorias.get(categoria_id)

    def listar_todos(self):
        """Devuelve todas las categorías almacenadas."""
        return list(self._categorias.values())

    def actualizar(self, categoria_id, categoria_actualizada):
        """Actualiza una categoría existente."""
        if categoria_id not in self._categorias:
            raise ValueError(f"No existe la categoría con id {categoria_id}")
        categoria_actualizada.id = categoria_id
        self._categorias[categoria_id] = categoria_actualizada
        return categoria_actualizada

    def eliminar(self, categoria_id):
        """Elimina una categoría existente."""
        if categoria_id not in self._categorias:
            return False
        del self._categorias[categoria_id]
        return True
