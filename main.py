from infrastructure.adaptadores import NotificadorEmail, ProveedorFechaSistema
from infrastructure.repositorios_memoria import (
    RepositorioEquiposMemoria,
    RepositorioEstudiantesMemoria,
    RepositorioPrestamosMemoria,
)
from infrastructure.repositorios_sql import (
    RepositorioEquiposSQL,
    RepositorioEstudiantesSQL,
    RepositorioPrestamosSQL,
)


if __name__ == "__main__":
    repositorio_equipos = RepositorioEquiposMemoria()
    repositorio_estudiantes = RepositorioEstudiantesMemoria()
    repositorio_prestamos = RepositorioPrestamosMemoria()
    notificador = NotificadorEmail()
    proveedor_fecha = ProveedorFechaSistema()

    # Aquí se inyectan las dependencias para continuar la implementación.
    # La lógica real de cada caso de uso se desarrolla luego.
    print("Sistema listo para continuar con la implementación.")
    print(repositorio_equipos)
    print(repositorio_estudiantes)
    print(repositorio_prestamos)
    print(notificador)
    print(proveedor_fecha)
