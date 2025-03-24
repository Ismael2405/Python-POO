class Persona:
    edad=31
    nombre = 'DENNIS'
    pais = 'Noruega'
inge = Persona()
#para llamar al atributo edad de otra manera
print(getattr(inge,'edad'))
#para cambiar un nombre
print('el doctor tiene un nombre?',hasattr(inge,'nombre'))
print('antes era: ',inge.nombre)
setattr(inge,'nombre','Ismael')
print('ahora se llama: ',inge.nombre)
#para eliminar un atributo
delattr(Persona,'pais')
print(inge.nombre)