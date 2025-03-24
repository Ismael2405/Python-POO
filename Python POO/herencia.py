class Pokemon:
    pass
    def __init__(self,nombre,habilidad):
        self.nombre = nombre
        self.habilidad = habilidad
    def descripcion(self):
        return '{} es un pokemon de tipo {}'.format(self.nombre,self.habilidad)

class electrico (Pokemon):
    def ataque(self,tipoataque):
        return 'tipo de ataque -> {}'.format(tipoataque)
class fuego (Pokemon):
    def defensa (self,tipodefensa):
        return 'tipo de defensa -> {}'.format(tipodefensa)

nuevo_Pokemon1 = electrico(nombre='Zeus',habilidad='electrico')
print(nuevo_Pokemon1.descripcion())
print(nuevo_Pokemon1.ataque('tormenta electrica'))

nuevo_Pokemon = fuego(nombre='boby',habilidad='fuego')
print(nuevo_Pokemon.descripcion())
print(nuevo_Pokemon.defensa('escudo de fuego'))