class Equipo:
    ESTADOS = ["EN_MANTENIMIENTO", "DISPONIBLE", "PRESTADO"]

    def __init__(self, nombre, categoria_id):
        self.id = None
        self.nombre = nombre
        self.categoria_id = categoria_id
        self.estado = "DISPONIBLE"
        

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado


    def mostrar_informacion(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "categoria_id": self.categoria_id,
            "estado": self.estado
        }
