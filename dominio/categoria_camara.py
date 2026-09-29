from dominio.categoria import Categoria
class CategoriaCamara(Categoria):
    @property
    def nombre(self): return "CAMARA"
    @property
    def plazo_dias(self): return 2
    @property
    def tarifa_diaria(self): return 8000.0
