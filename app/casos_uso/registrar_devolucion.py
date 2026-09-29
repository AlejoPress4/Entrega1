class RegistrarDevolucion:
    def __init__(self, repositorio_prestamos, repositorio_equipos, notificador=None, proveedor_fecha=None):
        self.repositorio_prestamos = repositorio_prestamos
        self.repositorio_equipos = repositorio_equipos
        self.notificador = notificador
        self.proveedor_fecha = proveedor_fecha

    def ejecutar(self, prestamo_id):
        """Registra la devolución de un equipo prestado."""
        prestamo = self.repositorio_prestamos.buscar_por_id(prestamo_id)
        if prestamo is None:
            raise ValueError(f"No existe el préstamo con id {prestamo_id}")
        if prestamo.estado == "DEVUELTO":
            raise ValueError(f"El préstamo {prestamo_id} ya fue devuelto")

        equipo = self.repositorio_equipos.buscar_por_id(prestamo.equipo_id)
        if equipo is not None:
            equipo.estado = "DISPONIBLE"
            self.repositorio_equipos.guardar(equipo)

        fecha_actual = self.proveedor_fecha.obtener_fecha_actual() if self.proveedor_fecha is not None else None
        prestamo.fecha_devolucion = fecha_actual
        prestamo.estado = "DEVUELTO"
        self.repositorio_prestamos.guardar(prestamo)

        if self.notificador is not None and equipo is not None:
            self.notificador.enviar(
                f"Devolución registrada del equipo {equipo.nombre}.",
                "sistema",
            )

        return prestamo
