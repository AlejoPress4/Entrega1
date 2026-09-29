from app.ports import Notificador, ProveedorFecha


class NotificadorEmail(Notificador):
    def enviar(self, mensaje, destinatario):
        """Simula el envío de una notificación por correo."""
        pass


class ProveedorFechaSistema(ProveedorFecha):
    def obtener_fecha_actual(self):
        """Retorna la fecha actual del sistema."""
        pass
