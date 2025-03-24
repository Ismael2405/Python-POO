class Nombre:
    pass
victor = Nombre()
maria = Nombre()

#object.atributo = valor
victor.edad = 30
victor.profesion = 'ingeniero'
victor.pais = 'alemania'

maria.edad = 12
maria.profesion = 'estudiante'
maria.pais = 'suiza'

print(victor.profesion +" de "+ victor.pais+ " "+str(victor.edad) + " anios")
print(maria.profesion +" de "+ maria.pais+ " "+str(maria.edad)+ " anios")
