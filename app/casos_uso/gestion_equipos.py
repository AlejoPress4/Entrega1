class GestionEquipos:
    def __init__(self, repositorio_equipos, repositorio_categorias=None):
        self.repositorio_equipos = repositorio_equipos
        self.repositorio_categorias = repositorio_categorias

    def registrar(self, equipo):
        """Guarda un equipo en el repositorio."""
        if equipo.id is None:
            equipo.id = self._siguiente_id_disponible()
        return self.repositorio_equipos.guardar(equipo)

    def buscar_por_id(self, equipo_id):
        """Busca un equipo por su identificador."""
        return self.repositorio_equipos.buscar_por_id(equipo_id)

    def listar_todos(self):
        """Retorna todos los equipos disponibles en el sistema."""
        return self.repositorio_equipos.listar_todos()

    def cambiar_estado(self, equipo_id, nuevo_estado):
        """Actualiza el estado de un equipo."""
        equipo = self.buscar_por_id(equipo_id)
        if equipo is None:
            raise ValueError(f"No existe el equipo con id {equipo_id}")
        equipo.estado = nuevo_estado
        return self.repositorio_equipos.guardar(equipo)

    def obtener_cuota(self, equipo):
        """Obtiene la cuota del equipo según su categoría."""
        if equipo is None:
            return 0
        if self.repositorio_categorias is not None:
            categoria = self.repositorio_categorias.buscar_por_id(equipo.categoria_id)
            if categoria is not None:
                return categoria.cuota_diaria
        return getattr(equipo, "cuota_diaria", 0) or 0

    def obtener_plazo(self, equipo):
        """Obtiene el plazo máximo del equipo según su categoría."""
        if equipo is None:
            return 0
        if self.repositorio_categorias is not None:
            categoria = self.repositorio_categorias.buscar_por_id(equipo.categoria_id)
            if categoria is not None:
                return categoria.plazo_maximo_dias
        return getattr(equipo, "plazo_maximo_dias", 0) or 0

    def _siguiente_id_disponible(self):
        equipos = self.listar_todos()
        if not equipos:
            return 1
        return max(equipo.id for equipo in equipos) + 1
