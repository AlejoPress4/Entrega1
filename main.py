from dominio.categoria_proyector import CategoriaProyector
import sqlite3
from infraestructura.repositorio_estudiantes_sqlite import RepositorioEstudiantesSQLite
from infraestructura.repositorio_equipos_sqlite import RepositorioEquiposSQLite
from infraestructura.repositorio_prestamos_sqlite import RepositorioPrestamosSQLite
from infraestructura.repositorio_prestamos_memoria import RepositorioPrestamosMemoria
from infraestructura.proveedor_fecha_fija import ProveedorFechaFija
from infraestructura.notificador_consola import NotificadorConsola

from aplicacion.casos_uso.registrar_prestamo import RegistrarPrestamo
from aplicacion.casos_uso.registrar_devolucion import RegistrarDevolucion

from dominio.estudiante import Estudiante
from dominio.equipo import Equipo
from dominio.categoria_portatil import CategoriaPortatil
from dominio.categoria_camara import CategoriaCamara
from dominio.categoria_kit_robotica import CategoriaKitRobotica
from dominio.categoria import Categoria


def inicializar_bd(nombre_archivo=":memory:"):
    conexion = sqlite3.connect(nombre_archivo)
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS estudiantes (id TEXT PRIMARY KEY, nombre TEXT, multa_pendiente INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS equipos (id TEXT PRIMARY KEY, categoria TEXT, estado TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS prestamos (id TEXT PRIMARY KEY, id_estudiante TEXT, id_equipo TEXT, fecha_prestamo TEXT, fecha_limite TEXT, activo INTEGER, fecha_devolucion TEXT, multa_generada REAL, FOREIGN KEY(id_estudiante) REFERENCES estudiantes(id), FOREIGN KEY(id_equipo) REFERENCES equipos(id))")
    conexion.commit()
    return conexion

def ejecutar_demo():
    print("--- INICIANDO DEMO ---")
    conexion = inicializar_bd()
    
    categorias_extra = {"PROYECTOR": CategoriaProyector()}
    
    repo_estudiantes = RepositorioEstudiantesSQLite(conexion)
    repo_equipos = RepositorioEquiposSQLite(conexion, categorias_extra)
    repo_prestamos_sql = RepositorioPrestamosSQLite(conexion, repo_estudiantes, repo_equipos)
    repo_prestamos_memoria = RepositorioPrestamosMemoria()
    
    # LSP: Cambiando esta linea a repo_prestamos_memoria deberia funcionar igual
    repo_prestamos = repo_prestamos_memoria 
    
    notificador = NotificadorConsola()
    proveedor_fecha = ProveedorFechaFija(2026, 10, 5)
    
    caso_prestamo = RegistrarPrestamo(repo_estudiantes, repo_equipos, repo_prestamos, notificador, proveedor_fecha)
    caso_devolucion = RegistrarDevolucion(repo_prestamos, repo_equipos, repo_estudiantes, notificador, proveedor_fecha)
    
    # Cargar datos iniciales
    repo_estudiantes.guardar(Estudiante("Ana", "Ana Gomez"))
    
    luis = Estudiante("Luis", "Luis Perez")
    luis.multa_pendiente = True
    repo_estudiantes.guardar(luis)
    
    repo_equipos.guardar(Equipo("PORTATIL-01", CategoriaPortatil()))
    repo_equipos.guardar(Equipo("CAMARA-02", CategoriaCamara()))
    repo_equipos.guardar(Equipo("PROYECTOR-01", CategoriaProyector()))
    
    # CA3 prep: CAMARA-02 lent on 2026-10-01
    proveedor_fecha.fecha_fija = ProveedorFechaFija(2026, 10, 1).hoy()
    p1 = caso_prestamo.ejecutar("Ana", "CAMARA-02")
    
    proveedor_fecha.fecha_fija = ProveedorFechaFija(2026, 10, 5).hoy()
    
    print("\n--- CA1: Ana pide PORTATIL-01 ---")
    try:
        p2 = caso_prestamo.ejecutar("Ana", "PORTATIL-01")
        print(f"Exito. Prestamo ID: {p2.id}")
    except Exception as e:
        print(f"Error: {e}")
        
    print("\n--- CA2: Ana pide un tercer equipo (PROYECTOR-01) ---")
    try:
        p3 = caso_prestamo.ejecutar("Ana", "PROYECTOR-01")
    except Exception as e:
        print(f"Rechazado correctamente: {e}")
        
    print("\n--- CA3: CAMARA-02 devuelta tarde ---")
    try:
        proveedor_fecha.fecha_fija = ProveedorFechaFija(2026, 10, 6).hoy()
        caso_devolucion.ejecutar(p1.id, equipo_daniado=False)
        proveedor_fecha.fecha_fija = ProveedorFechaFija(2026, 10, 5).hoy()
    except Exception as e:
        print(f"Error: {e}")
        
    print("\n--- CA4: Luis pide equipo con multa pendiente ---")
    try:
        p4 = caso_prestamo.ejecutar("Luis", "PORTATIL-01")
    except Exception as e:
        print(f"Rechazado correctamente: {e}")
        
    print("\n--- CA5: Devolver con danio (PORTATIL-01) ---")
    try:
        # Before CA5, Ana needs to pay her fine to borrow again or we just test returning PORTATIL-01
        # Wait, the prompt says "Un equipo se devuelve con danio. Queda EN_MANTENIMIENTO y no se puede prestar."
        # So we just return p2
        caso_devolucion.ejecutar(p2.id, equipo_daniado=True)
        eq = repo_equipos.buscar_por_id("PORTATIL-01")
        print(f"Estado de PORTATIL-01 despues de devolver con danio: {eq.estado}")
        print("Intentando prestar equipo en mantenimiento...")
        # Clean Ana's fine to avoid "multa pendiente" exception, we want "equipo no disponible" exception
        ana = repo_estudiantes.buscar_por_id("Ana")
        ana.multa_pendiente = False
        repo_estudiantes.guardar(ana)
        caso_prestamo.ejecutar("Ana", "PORTATIL-01")
    except Exception as e:
        print(f"Rechazado correctamente: {e}")
        
    print("\n--- CA6: Prestar PROYECTOR-01 (OCP) ---")
    try:
        p5 = caso_prestamo.ejecutar("Ana", "PROYECTOR-01")
        print(f"Exito. Prestamo ID: {p5.id}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ejecutar_demo()
