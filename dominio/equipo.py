class Equipo:
    def __init__(self, id_equipo, categoria):
        self.id = id_equipo
        self.categoria = categoria
        self.estado = "DISPONIBLE"
    def marcar_prestado(self):
        self.estado = "PRESTADO"
    def marcar_disponible(self):
        self.estado = "DISPONIBLE"
    def marcar_mantenimiento(self):
        self.estado = "EN_MANTENIMIENTO"
    def esta_disponible(self):
        return self.estado == "DISPONIBLE"
