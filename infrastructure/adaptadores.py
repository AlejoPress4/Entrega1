from datetime import date

from app.ports import Notificador, ProveedorFecha


class NotificadorEmail(Notificador):
    def enviar(self, mensaje, destinatario):
        """Simula el envío de una notificación por correo."""
        print(f"[EMAIL] Para: {destinatario} | Mensaje: {mensaje}")
        return True


class ProveedorFechaSistema(ProveedorFecha):
    def obtener_fecha_actual(self):
        """Retorna la fecha actual del sistema."""
        return date.today()


class ProveedorFechaFija(ProveedorFecha):
    def __init__(self, fecha):
        self.fecha = date.fromisoformat(fecha)

    def obtener_fecha_actual(self):
        """Retorna una fecha fija para el modo demo."""
        return self.fecha
