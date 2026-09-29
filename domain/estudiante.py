class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.id = None
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}"

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def __str__(self):
        return self.mostrar_informacion()