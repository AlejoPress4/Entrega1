


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
    PLAZOS_POR_CATEGORIA = {
        "PROYECTOR": 7,
        "PORTATIL": 10,
        "CAMARA": 15,
        "KIT_ROBOTICA": 12,
        "AUDIO": 20,
    }

    def __init__(self, nombre, categoria):
        self.id = None
        self.nombre = nombre
        self.categoria = categoria.upper()
        self.estado = "DISPONIBLE"
        self.cuota_diaria = self._obtener_cuota_por_categoria(self.categoria)
        self.plazo_maximo_dias = self._obtener_plazo_por_categoria(self.categoria)

    def _obtener_cuota_por_categoria(self, categoria):
        return self.CUOTAS_POR_CATEGORIA.get(categoria, 0)

    def _obtener_plazo_por_categoria(self, categoria):
        return self.PLAZOS_POR_CATEGORIA.get(categoria, 0)

    @classmethod
    def agregar_categoria(cls, categoria, cuota_diaria, plazo_maximo_dias):
        categoria = categoria.upper()
        cls.CUOTAS_POR_CATEGORIA[categoria] = cuota_diaria
        cls.PLAZOS_POR_CATEGORIA[categoria] = plazo_maximo_dias
        if categoria not in cls.CATEGORIAS:
            cls.CATEGORIAS.append(categoria)

    @classmethod
    def actualizar_categoria(cls, categoria, cuota_diaria=None, plazo_maximo_dias=None):
        categoria = categoria.upper()
        if cuota_diaria is not None:
            cls.CUOTAS_POR_CATEGORIA[categoria] = cuota_diaria
        if plazo_maximo_dias is not None:
            cls.PLAZOS_POR_CATEGORIA[categoria] = plazo_maximo_dias
        if categoria not in cls.CATEGORIAS:
            cls.CATEGORIAS.append(categoria)

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
            "plazo_maximo_dias": self.plazo_maximo_dias,
        }
