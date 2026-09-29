class GestionCategoriasEquipo:
    def __init__(self, repositorio_categorias):
        self.repositorio_categorias = repositorio_categorias

    def registrar(self, categoria):
        """Guarda una categoría de equipo."""
        if categoria.id is None:
            categoria.id = self._siguiente_id_disponible()
        return self.repositorio_categorias.guardar(categoria)

    def buscar_por_id(self, categoria_id):
        """Busca una categoría por su identificador."""
        return self.repositorio_categorias.buscar_por_id(categoria_id)

    def listar_todos(self):
        """Retorna todas las categorías disponibles."""
        return self.repositorio_categorias.listar_todos()

    def actualizar(self, categoria_id, nombre=None, cuota_diaria=None, plazo_maximo_dias=None):
        """Actualiza los datos de una categoría de equipo."""
        categoria = self.buscar_por_id(categoria_id)
        if categoria is None:
            raise ValueError(f"No existe la categoría con id {categoria_id}")

        if nombre is not None:
            categoria.nombre = nombre.upper()
        if cuota_diaria is not None:
            categoria.cuota_diaria = cuota_diaria
        if plazo_maximo_dias is not None:
            categoria.plazo_maximo_dias = plazo_maximo_dias

        return self.repositorio_categorias.actualizar(categoria_id, categoria)

    def eliminar(self, categoria_id):
        """Elimina una categoría de equipo."""
        return self.repositorio_categorias.eliminar(categoria_id)

    def obtener_cuota(self, categoria):
        """Obtiene la cuota diaria asociada a una categoría."""
        if categoria is None:
            return 0
        return getattr(categoria, "cuota_diaria", 0)

    def obtener_plazo(self, categoria):
        """Obtiene el plazo máximo asociado a una categoría."""
        if categoria is None:
            return 0
        return getattr(categoria, "plazo_maximo_dias", 0)

    def _siguiente_id_disponible(self):
        categorias = self.listar_todos()
        if not categorias:
            return 1
        return max(categoria.id for categoria in categorias) + 1
