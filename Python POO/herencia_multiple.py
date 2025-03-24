#Herencia Multiple
    #class Base_uno:
        #pass
    #class Base_dos:
        #pass
    #class DerivadMulltiple(Base_uno,Base_dos):
        #pass
class Telefono:
    def __init__(self):
        pass
    def llamar(self):
        print('llamando...')
    def ocupado(self):
        print('ocupado...')


class Camara:
    def __init__(self):
        pass
    def fotografia(self):
        print('tomando fotos...')


class Reproducion:
    def __init__(self):
        pass
    def reproduccionmusica(self):
        print('reproduce musica...')
    def reproduccionvideo(self):
        print('reproducir video...')

class Smartphone(Telefono,Camara,Reproducion):
    #usamos del para limpiar recursos
    def __del__(self):
        print('telefono apagado')

movil = Smartphone()
print(movil.llamar())
