class RegistrarDevolucion:
    def __init__(self, repo_prestamos, repo_equipos, repo_estudiantes, notificador, proveedor_fecha):
        self.repo_prestamos = repo_prestamos
        self.repo_equipos = repo_equipos
        self.repo_estudiantes = repo_estudiantes
        self.notificador = notificador
        self.proveedor_fecha = proveedor_fecha

    def ejecutar(self, id_prestamo, equipo_daniado):
        prestamo = self.repo_prestamos.buscar_por_id(id_prestamo)
        fecha_devolucion = self.proveedor_fecha.hoy()
        
        dias_retraso = (fecha_devolucion - prestamo.fecha_limite).days
        multa = 0.0
        
        if dias_retraso > 0:
            tarifa = prestamo.equipo.categoria.tarifa_diaria
            multa = dias_retraso * tarifa
            prestamo.estudiante.multa_pendiente = True
            self.repo_estudiantes.guardar(prestamo.estudiante)
            mensaje = f"Devolucion tardia. Multa generada: ${multa}"
            self.notificador.notificar(prestamo.estudiante.id, mensaje)
            
        prestamo.finalizar(fecha_devolucion, multa)
        
        if equipo_daniado:
            prestamo.equipo.marcar_mantenimiento()
        else:
            prestamo.equipo.marcar_disponible()
            
        self.repo_prestamos.guardar(prestamo)
        self.repo_equipos.guardar(prestamo.equipo)
        return prestamo
