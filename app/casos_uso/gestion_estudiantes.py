class GestionEstudiantes:
    def __init__(self, repositorio_estudiantes):
        self.repositorio_estudiantes = repositorio_estudiantes

    def registrar(self, estudiante):
        """Guarda un estudiante en el repositorio."""
        if estudiante.id is None:
            estudiante.id = self._siguiente_id_disponible()
        return self.repositorio_estudiantes.guardar(estudiante)

    def buscar_por_id(self, estudiante_id):
        """Busca un estudiante por su identificador."""
        return self.repositorio_estudiantes.buscar_por_id(estudiante_id)

    def listar_todos(self):
        """Retorna la lista de estudiantes registrados."""
        return self.repositorio_estudiantes.listar_todos()

    def _siguiente_id_disponible(self):
        estudiantes = self.listar_todos()
        if not estudiantes:
            return 1
        return max(estudiante.id for estudiante in estudiantes) + 1
