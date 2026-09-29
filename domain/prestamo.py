class Prestamo:
    def __init__(self, equipo_id, estudiante_id, fecha_prestamo=None, fecha_devolucion=None):
        self.id = None
        self.equipo_id = equipo_id
        self.estudiante_id = estudiante_id
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.estado = "ACTIVO"

    def registrar_prestamo(self):
        """Registra la operación inicial del préstamo."""
        pass

    def registrar_devolucion(self):
        """Registra la devolución del equipo."""
        pass

    def calcular_total(self):
        """Calcula el valor total asociado al préstamo."""
        pass

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def __str__(self):
        return f"Prestamo(id={self.id}, equipo_id={self.equipo_id}, estudiante_id={self.estudiante_id}, fecha_prestamo={self.fecha_prestamo}, fecha_devolucion={self.fecha_devolucion}, estado={self.estado})"
