from dominio.excepcion_regla_negocio import ExcepcionReglaNegocio
class ExcepcionEquipoNoDisponible(ExcepcionReglaNegocio):
    def __init__(self): super().__init__("El equipo no se encuentra disponible para prestamo.")
