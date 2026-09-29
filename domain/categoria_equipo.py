class CategoriaEquipo:
    def __init__(self, nombre, cuota_diaria, plazo_maximo_dias):
        self.id = None
        self.nombre = nombre.upper()
        self.cuota_diaria = cuota_diaria
        self.plazo_maximo_dias = plazo_maximo_dias

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def mostrar_informacion(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cuota_diaria": self.cuota_diaria,
            "plazo_maximo_dias": self.plazo_maximo_dias,
        }

    def __str__(self):
        return f"CategoriaEquipo({self.nombre}, cuota={self.cuota_diaria}, plazo={self.plazo_maximo_dias})"
