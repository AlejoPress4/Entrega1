class RegistrarPrestamo:
    def __init__(self, repositorio_prestamos, repositorio_equipos, repositorio_estudiantes, notificador, proveedor_fecha):
        self.repositorio_prestamos = repositorio_prestamos
        self.repositorio_equipos = repositorio_equipos
        self.repositorio_estudiantes = repositorio_estudiantes
        self.notificador = notificador
        self.proveedor_fecha = proveedor_fecha

    def ejecutar(self, equipo_id, estudiante_id):
        """Registra un préstamo validando disponibilidad, estudiante y equipo."""
        pass


class RegistrarDevolucion:
    def __init__(self, repositorio_prestamos, repositorio_equipos, notificador, proveedor_fecha):
        self.repositorio_prestamos = repositorio_prestamos
        self.repositorio_equipos = repositorio_equipos
        self.notificador = notificador
        self.proveedor_fecha = proveedor_fecha

    def ejecutar(self, prestamo_id):
        """Registra la devolución de un equipo prestado."""
        pass


class GestionEquipos:
    def __init__(self, repositorio_equipos):
        self.repositorio_equipos = repositorio_equipos

    def registrar(self, equipo):
        """Guarda un equipo en el repositorio."""
        pass

    def buscar_por_id(self, equipo_id):
        """Busca un equipo por su identificador."""
        pass

    def listar_todos(self):
        """Retorna todos los equipos disponibles en el sistema."""
        pass

    def cambiar_estado(self, equipo_id, nuevo_estado):
        """Actualiza el estado de un equipo."""
        pass


class GestionEstudiantes:
    def __init__(self, repositorio_estudiantes):
        self.repositorio_estudiantes = repositorio_estudiantes

    def registrar(self, estudiante):
        """Guarda un estudiante en el repositorio."""
        pass

    def buscar_por_id(self, estudiante_id):
        """Busca un estudiante por su identificador."""
        pass

    def listar_todos(self):
        """Retorna la lista de estudiantes registrados."""
        pass
