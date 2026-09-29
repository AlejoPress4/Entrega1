from dominio.excepcion_regla_negocio import ExcepcionReglaNegocio
class ExcepcionLimitePrestamos(ExcepcionReglaNegocio):
    def __init__(self): super().__init__("El estudiante ya tiene el maximo de prestamos activos permitidos.")
