from dominio.categoria import Categoria

class CategoriaProyector(Categoria):
    @property
    def nombre(self): return "PROYECTOR"
    @property
    def plazo_dias(self): return 2
    @property
    def tarifa_diaria(self): return 6000.0
