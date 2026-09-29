class Prestamo:
    def __init__(self, id_prestamo, estudiante, equipo, fecha_prestamo, fecha_limite):
        self.id = id_prestamo
        self.estudiante = estudiante
        self.equipo = equipo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_limite = fecha_limite
        self.activo = True
        self.fecha_devolucion = None
        self.multa_generada = 0.0
    def finalizar(self, fecha_devolucion, multa):
        self.activo = False
        self.fecha_devolucion = fecha_devolucion
        self.multa_generada = multa
