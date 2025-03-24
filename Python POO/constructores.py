class Persona:
    pass
    def __init__(self,nombre,año): #iniciar tu constructor - __init__
        self.nombre = nombre
        self.año = año
    def descripcion(self):
        return '{} tiene {},'.format(self.nombre,self.año)
    def comentario (self,frase):
        return '{} dijo {}'.format(self.nombre,frase)

inge = Persona('Dennis',22)
print(inge.descripcion(),inge.comentario('Hoolaa'))


class Email:
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True
mi_correo = Email()
print(mi_correo.enviado)
mi_correo.enviar_correo()
print(mi_correo.enviado)
