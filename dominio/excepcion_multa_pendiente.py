from dominio.excepcion_regla_negocio import ExcepcionReglaNegocio
class ExcepcionMultaPendiente(ExcepcionReglaNegocio):
    def __init__(self): super().__init__("El estudiante tiene una multa pendiente y no puede pedir prestado.")
