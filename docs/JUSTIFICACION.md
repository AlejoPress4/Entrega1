# Justificación de Clean Architecture y Clean Code

## Principios SOLID
| Principio | Archivo | Decisión concreta donde se aplica |
| --- | --- | --- |
| SRP | aplicacion/casos_uso/registrar_prestamo.py | El caso de uso solo orquesta las reglas de negocio, delegando la persistencia a los repositorios y la notificación al puerto Notificador. |
| OCP | dominio/categoria.py y main.py | Se creó una interfaz abstracta `Categoria`. Para agregar PROYECTOR (CA6) solo se crea una clase `CategoriaProyector` y se inyecta en main.py sin modificar casos de uso ni entidades. |
| LSP | main.py | `repo_prestamos_memoria` (memoria) puede reemplazar a `repo_prestamos_sql` (SQLite) sin alterar el comportamiento de la aplicación, ya que ambos cumplen con la interfaz abstracta RepositorioPrestamos. |
| ISP | aplicacion/puertos/ | Se segregaron interfaces específicas en lugar de un repositorio genérico. Existen `RepositorioEstudiantes`, `RepositorioEquipos`, `RepositorioPrestamos`, `Notificador` y `ProveedorFecha` de manera independiente. |
| DIP | aplicacion/casos_uso/registrar_prestamo.py | El caso de uso depende de abstracciones (puertos e interfaces) inyectados en el constructor, y no de implementaciones concretas de bases de datos o notificaciones. |

## Revisión de Importaciones
- **Dominio**: Ejemplo `dominio/estudiante.py` no tiene importaciones externas, solo clases nativas, garantizando que el núcleo de negocio sea independiente del framework.
- **Aplicación (Casos de uso)**: Ejemplo `aplicacion/casos_uso/registrar_prestamo.py` importa clases de dominio y la librería `datetime`. No importa `sqlite3` ni clases de infraestructura, manteniendo la regla de dependencia hacia adentro.
- **Infraestructura**: Ejemplo `infraestructura/repositorio_estudiantes_sqlite.py` importa `sqlite3`, el puerto `RepositorioEstudiantes` (aplicación) y la entidad `Estudiante` (dominio), adaptando los datos a la DB.

## Declaración de Autoría
Declaramos que el diseño, el código y los diagramas son de nuestra autoría y que no usamos IA generativa para producirlos.
Juan y Pedro
