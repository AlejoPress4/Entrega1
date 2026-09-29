from aplicacion.puertos.proveedor_fecha import ProveedorFecha
from datetime import date
class ProveedorFechaSistema(ProveedorFecha):
    def hoy(self):
        return date.today()
