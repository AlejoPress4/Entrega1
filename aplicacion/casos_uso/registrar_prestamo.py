from datetime import timedelta
from dominio.excepcion_limite_prestamos import ExcepcionLimitePrestamos
from dominio.excepcion_equipo_no_disponible import ExcepcionEquipoNoDisponible
from dominio.excepcion_multa_pendiente import ExcepcionMultaPendiente
from dominio.prestamo import Prestamo
import uuid

class RegistrarPrestamo:
    def __init__(self, repo_estudiantes, repo_equipos, repo_prestamos, notificador, proveedor_fecha):
        self.repo_estudiantes = repo_estudiantes
        self.repo_equipos = repo_equipos
        self.repo_prestamos = repo_prestamos
        self.notificador = notificador
        self.proveedor_fecha = proveedor_fecha

    def ejecutar(self, id_estudiante, id_equipo):
        estudiante = self.repo_estudiantes.buscar_por_id(id_estudiante)
        equipo = self.repo_equipos.buscar_por_id(id_equipo)
        self._validar_reglas(estudiante, equipo)
        
        fecha_prestamo = self.proveedor_fecha.hoy()
        plazo = equipo.categoria.plazo_dias
        fecha_limite = fecha_prestamo + timedelta(days=plazo)
        
        id_prestamo = str(uuid.uuid4())[:8]
        prestamo = Prestamo(id_prestamo, estudiante, equipo, fecha_prestamo, fecha_limite)
        
        equipo.marcar_prestado()
        
        self.repo_equipos.guardar(equipo)
        self.repo_prestamos.guardar(prestamo)
        
        mensaje = f"Prestamo registrado. Fecha limite: {fecha_limite.strftime("%Y-%m-%d")}."
        self.notificador.notificar(estudiante.id, mensaje)
        
        return prestamo

    def _validar_reglas(self, estudiante, equipo):
        if estudiante.multa_pendiente:
            raise ExcepcionMultaPendiente()
        if not equipo.esta_disponible():
            raise ExcepcionEquipoNoDisponible()
        activos = self.repo_prestamos.contar_activos_de_estudiante(estudiante.id)
        if activos >= 2:
            raise ExcepcionLimitePrestamos()
