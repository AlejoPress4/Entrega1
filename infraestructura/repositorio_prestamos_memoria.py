from aplicacion.puertos.repositorio_prestamos import RepositorioPrestamos

class RepositorioPrestamosMemoria(RepositorioPrestamos):
    def __init__(self):
        self.prestamos = {}

    def contar_activos_de_estudiante(self, id_estudiante):
        count = 0
        for p in self.prestamos.values():
            if p.estudiante.id == id_estudiante and p.activo:
                count += 1
        return count

    def buscar_por_id(self, id_prestamo):
        return self.prestamos.get(id_prestamo)

    def guardar(self, prestamo):
        self.prestamos[prestamo.id] = prestamo
