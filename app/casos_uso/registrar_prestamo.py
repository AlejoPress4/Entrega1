from domain.prestamo import Prestamo


class RegistrarPrestamo:
    def __init__(self, repositorio_prestamos, repositorio_equipos, repositorio_estudiantes, repositorio_categorias=None, notificador=None, proveedor_fecha=None):
        self.repositorio_prestamos = repositorio_prestamos
        self.repositorio_equipos = repositorio_equipos
        self.repositorio_estudiantes = repositorio_estudiantes
        self.repositorio_categorias = repositorio_categorias
        self.notificador = notificador
        self.proveedor_fecha = proveedor_fecha

    def ejecutar(self, equipo_id, estudiante_id):
        """Registra un préstamo validando disponibilidad, estudiante y equipo."""
        equipo = self.repositorio_equipos.buscar_por_id(equipo_id)
        estudiante = self.repositorio_estudiantes.buscar_por_id(estudiante_id)

        if equipo is None:
            raise ValueError(f"No existe el equipo con id {equipo_id}")
        if estudiante is None:
            raise ValueError(f"No existe el estudiante con id {estudiante_id}")
        if equipo.estado == "PRESTADO":
            raise ValueError(f"El equipo {equipo.nombre} ya está prestado")

        fecha_actual = self.proveedor_fecha.obtener_fecha_actual() if self.proveedor_fecha is not None else None
        prestamo = Prestamo(equipo_id, estudiante_id, fecha_prestamo=fecha_actual, fecha_devolucion=None)
        prestamo.id = self._siguiente_id_disponible()

        if self.repositorio_categorias is not None:
            categoria = self.repositorio_categorias.buscar_por_id(equipo.categoria_id)
            if categoria is not None:
                equipo.cuota_diaria = categoria.cuota_diaria
                equipo.plazo_maximo_dias = categoria.plazo_maximo_dias

        equipo.estado = "PRESTADO"
        self.repositorio_equipos.guardar(equipo)
        self.repositorio_prestamos.guardar(prestamo)

        if self.notificador is not None:
            self.notificador.enviar(
                f"Préstamo registrado para {estudiante.nombre} con equipo {equipo.nombre}.",
                estudiante.nombre,
            )

        return prestamo

    def _siguiente_id_disponible(self):
        prestamos = self.repositorio_prestamos.listar_todos()
        if not prestamos:
            return 1
        return max(prestamo.id for prestamo in prestamos) + 1
