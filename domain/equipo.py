


class Equipo():
    ESTADOS = ["EN_MANTENIMIENTO", "DISPONIBLE", "PRESTADO"]
    CATEGORIAS = ["PROYECTOR", "PORTATIL", "CAMARA", "KIT_ROBOTICA", "AUDIO"]
    CUOTAS_POR_CATEGORIA = {
        "PROYECTOR": 15000,
        "PORTATIL": 12000,
        "CAMARA": 8000,
        "KIT_ROBOTICA": 10000,
        "AUDIO": 5000,
    }

    def __init__(self, nombre, categoria):
        self.id = None
        self.nombre = nombre
        self.categoria = categoria.upper()
        self.estado = "DISPONIBLE"
        self.cuota_diaria = self._obtener_cuota_por_categoria(self.categoria)

    def _obtener_cuota_por_categoria(self, categoria):
        return self.CUOTAS_POR_CATEGORIA.get(categoria, 0)

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

    def get_categoria(self):
        return self.categoria

    def set_cuota_diaria(self, cuota):
        self.cuota_diaria = cuota

    def calcular_pago(self):
        return self.cuota_diaria

    def mostrar_informacion(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "estado": self.estado,
            "cuota_diaria": self.cuota_diaria,
        }
