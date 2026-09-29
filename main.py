from domain.categoria_equipo import CategoriaEquipo
from domain.equipo import Equipo
from domain.estudiante import Estudiante
from app.casos_uso import (
    GestionCategoriasEquipo,
    GestionEquipos,
    GestionEstudiantes,
    RegistrarPrestamo,
    RegistrarDevolucion,
)
from infrastructure.adaptadores import NotificadorEmail, ProveedorFechaFija
from infrastructure.repositorios_memoria import (
    RepositorioEquiposMemoria,
    RepositorioEstudiantesMemoria,
    RepositorioPrestamosMemoria,
    RepositorioCategoriasEquipoMemoria,
)


def crear_estado_demo():
    repositorio_categorias = RepositorioCategoriasEquipoMemoria()
    repositorio_equipos = RepositorioEquiposMemoria()
    repositorio_estudiantes = RepositorioEstudiantesMemoria()
    repositorio_prestamos = RepositorioPrestamosMemoria()

    gestion_categorias = GestionCategoriasEquipo(repositorio_categorias)
    gestion_equipos = GestionEquipos(repositorio_equipos, repositorio_categorias)
    gestion_estudiantes = GestionEstudiantes(repositorio_estudiantes)

    categoria_portatil = CategoriaEquipo("PORTATIL", 15000, 10)
    categoria_proyector = CategoriaEquipo("PROYECTOR", 12000, 7)
    gestion_categorias.registrar(categoria_portatil)
    gestion_categorias.registrar(categoria_proyector)

    equipo1 = Equipo("Laptop Dell", categoria_portatil.id)
    equipo2 = Equipo("Proyector Epson", categoria_proyector.id)
    equipo1.cuota_diaria = categoria_portatil.cuota_diaria
    equipo1.plazo_maximo_dias = categoria_portatil.plazo_maximo_dias
    equipo2.cuota_diaria = categoria_proyector.cuota_diaria
    equipo2.plazo_maximo_dias = categoria_proyector.plazo_maximo_dias
    gestion_equipos.registrar(equipo1)
    gestion_equipos.registrar(equipo2)

    estudiante1 = Estudiante("Ana García", 20, "Sistemas")
    estudiante2 = Estudiante("Luis Torres", 22, "Ingeniería")
    gestion_estudiantes.registrar(estudiante1)
    gestion_estudiantes.registrar(estudiante2)

    return {
        "repositorio_categorias": repositorio_categorias,
        "repositorio_equipos": repositorio_equipos,
        "repositorio_estudiantes": repositorio_estudiantes,
        "repositorio_prestamos": repositorio_prestamos,
        "gestion_categorias": gestion_categorias,
        "gestion_equipos": gestion_equipos,
        "gestion_estudiantes": gestion_estudiantes,
        "notificador": NotificadorEmail(),
        "proveedor_fecha": ProveedorFechaFija("2026-09-29"),
    }


def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Listar categorías")
    print("2. Listar equipos")
    print("3. Listar estudiantes")
    print("4. Listar préstamos")
    print("5. Registrar categoría")
    print("6. Registrar equipo")
    print("7. Registrar estudiante")
    print("8. Registrar préstamo")
    print("9. Registrar devolución")
    print("0. Salir")


def mostrar_categorias(gestion_categorias):
    categorias = gestion_categorias.listar_todos()
    if not categorias:
        print("No hay categorías registradas.")
        return
    print("\nCategorías:")
    for categoria in categorias:
        print(f"- {categoria.id}: {categoria.nombre} | cuota={categoria.cuota_diaria} | plazo={categoria.plazo_maximo_dias}")


def mostrar_equipos(gestion_equipos):
    equipos = gestion_equipos.listar_todos()
    if not equipos:
        print("No hay equipos registrados.")
        return
    print("\nEquipos:")
    for equipo in equipos:
        print(f"- {equipo.id}: {equipo.nombre} | categoria_id={equipo.categoria_id} | estado={equipo.estado}")


def mostrar_estudiantes(gestion_estudiantes):
    estudiantes = gestion_estudiantes.listar_todos()
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    print("\nEstudiantes:")
    for estudiante in estudiantes:
        print(f"- {estudiante.id}: {estudiante.nombre} | edad={estudiante.edad} | carrera={estudiante.carrera}")


def mostrar_prestamos(repositorio_prestamos):
    prestamos = repositorio_prestamos.listar_todos()
    if not prestamos:
        print("No hay préstamos registrados.")
        return
    print("\nPréstamos:")
    for prestamo in prestamos:
        print(f"- {prestamo.id}: equipo_id={prestamo.equipo_id} | estudiante_id={prestamo.estudiante_id} | estado={prestamo.estado}")


def registrar_categoria(gestion_categorias):
    nombre = input("Nombre de la categoría: ").strip()
    cuota = float(input("Cuota diaria: "))
    plazo = int(input("Plazo máximo en días: "))
    categoria = CategoriaEquipo(nombre, cuota, plazo)
    categoria_guardada = gestion_categorias.registrar(categoria)
    print(f"Categoría creada: {categoria_guardada.id} - {categoria_guardada.nombre}")


def registrar_equipo(gestion_equipos, gestion_categorias):
    nombre = input("Nombre del equipo: ").strip()
    mostrar_categorias(gestion_categorias)
    categoria_id = int(input("Id de la categoría: "))
    categoria = gestion_categorias.buscar_por_id(categoria_id)
    if categoria is None:
        print("La categoría no existe.")
        return

    equipo = Equipo(nombre, categoria_id)
    equipo.cuota_diaria = categoria.cuota_diaria
    equipo.plazo_maximo_dias = categoria.plazo_maximo_dias
    equipo_guardado = gestion_equipos.registrar(equipo)
    print(f"Equipo creado: {equipo_guardado.id} - {equipo_guardado.nombre}")


def registrar_estudiante(gestion_estudiantes):
    nombre = input("Nombre del estudiante: ").strip()
    edad = int(input("Edad: "))
    carrera = input("Carrera: ").strip()
    estudiante = Estudiante(nombre, edad, carrera)
    estudiante_guardado = gestion_estudiantes.registrar(estudiante)
    print(f"Estudiante creado: {estudiante_guardado.id} - {estudiante_guardado.nombre}")


def registrar_prestamo_interactivo(repositorio_prestamos, repositorio_equipos, repositorio_estudiantes, gestion_categorias, notificador, proveedor_fecha):
    mostrar_equipos(gestion_equipos)
    equipo_id = int(input("Id del equipo a prestar: "))
    mostrar_estudiantes(gestion_estudiantes)
    estudiante_id = int(input("Id del estudiante: "))

    caso_uso = RegistrarPrestamo(
        repositorio_prestamos,
        repositorio_equipos,
        repositorio_estudiantes,
        gestion_categorias.repositorio_categorias if hasattr(gestion_categorias, "repositorio_categorias") else None,
        notificador,
        proveedor_fecha,
    )

    prestamo = caso_uso.ejecutar(equipo_id, estudiante_id)
    print(f"Préstamo registrado con id={prestamo.id} y estado={prestamo.estado}")


def registrar_devolucion_interactivo(repositorio_prestamos, repositorio_equipos, notificador, proveedor_fecha):
    mostrar_prestamos(repositorio_prestamos)
    prestamo_id = int(input("Id del préstamo a devolver: "))
    caso_uso = RegistrarDevolucion(repositorio_prestamos, repositorio_equipos, notificador, proveedor_fecha)
    prestamo = caso_uso.ejecutar(prestamo_id)
    print(f"Devolución registrada para préstamo {prestamo.id}; estado={prestamo.estado}")


def ejecutar_menu():
    estado = crear_estado_demo()
    repositorio_categorias = estado["repositorio_categorias"]
    repositorio_equipos = estado["repositorio_equipos"]
    repositorio_estudiantes = estado["repositorio_estudiantes"]
    repositorio_prestamos = estado["repositorio_prestamos"]
    gestion_categorias = estado["gestion_categorias"]
    gestion_equipos = estado["gestion_equipos"]
    gestion_estudiantes = estado["gestion_estudiantes"]
    notificador = estado["notificador"]
    proveedor_fecha = estado["proveedor_fecha"]

    print("=== SISTEMA DE PRÉSTAMOS - MODO INTERACTIVO ===")
    print(f"Fecha actual del sistema: {proveedor_fecha.obtener_fecha_actual()}")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_categorias(gestion_categorias)
        elif opcion == "2":
            mostrar_equipos(gestion_equipos)
        elif opcion == "3":
            mostrar_estudiantes(gestion_estudiantes)
        elif opcion == "4":
            mostrar_prestamos(repositorio_prestamos)
        elif opcion == "5":
            registrar_categoria(gestion_categorias)
        elif opcion == "6":
            registrar_equipo(gestion_equipos, gestion_categorias)
        elif opcion == "7":
            registrar_estudiante(gestion_estudiantes)
        elif opcion == "8":
            registrar_prestamo_interactivo(repositorio_prestamos, repositorio_equipos, repositorio_estudiantes, gestion_categorias, notificador, proveedor_fecha)
        elif opcion == "9":
            registrar_devolucion_interactivo(repositorio_prestamos, repositorio_equipos, notificador, proveedor_fecha)
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar_menu()
