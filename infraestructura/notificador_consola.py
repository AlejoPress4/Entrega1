from aplicacion.puertos.notificador import Notificador
class NotificadorConsola(Notificador):
    def notificar(self, id_estudiante, mensaje):
        print(f"[Notificacion a {id_estudiante}]: {mensaje}")
