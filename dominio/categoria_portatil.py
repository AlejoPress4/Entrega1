from dominio.categoria import Categoria
class CategoriaPortatil(Categoria):
    @property
    def nombre(self): return "PORTATIL"
    @property
    def plazo_dias(self): return 3
    @property
    def tarifa_diaria(self): return 5000.0
