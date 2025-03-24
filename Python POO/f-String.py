class Estudiante:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.edad}"

nuevo_estudiante = Estudiante(nombre='Dennis',apellido='Marquez',edad='22')
print(f"{nuevo_estudiante}")