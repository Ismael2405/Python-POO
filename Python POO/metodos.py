#CLASS nombre de la clase:
    #DEF nombre del metodo(SELF) metodo=accion o movimiento
#SELF.nombre de la variable = ALGORITMO o valor
class Ropa:
    def __init__(self):
        self.marca = 'zyson'
        self.talla = 'XL'
        self.color = 'rosa'
camisa = Ropa()
print(camisa.talla)

class Calculadora:
    def __init__(self,n1,n2):
        self.suma = n1+n2
        self.resta = n1-n2
        self.multi = n1*n2
        self.division = n1/n2
operacion = Calculadora(10,3)
print(operacion.multi,operacion.division)

