from aplicacion.puertos.proveedor_fecha import ProveedorFecha
from datetime import date
class ProveedorFechaFija(ProveedorFecha):
    def __init__(self, anio, mes, dia):
        self.fecha_fija = date(anio, mes, dia)
    def hoy(self):
        return self.fecha_fija
