from dominio.categoria import Categoria
class CategoriaKitRobotica(Categoria):
    @property
    def nombre(self): return "KIT_ROBOTICA"
    @property
    def plazo_dias(self): return 1
    @property
    def tarifa_diaria(self): return 12000.0
