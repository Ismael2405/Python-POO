class Calculadora:
    def __init__(self,numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]
    def ingresardato(self):
        self.datos = [int(input( 'ingresar el '+str(i+1)+' dato: ')) for  i in range(self.n)]



class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,numero=2)

    def suma(self):
        a,b, = self.datos
        s = a+b
        print("el resultado es: ",s)

    def resta(self):
        a,b, = self.datos
        r = a-b
        print("el resultado es: ",r)



class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,numero=1)

    def cuadrada (self):
        import math
        a, = self.datos
        print("el resultado es: ",math.sqrt(a))


ejemplo = op_basicas()
print(ejemplo.ingresardato())
print(ejemplo.suma())
print(ejemplo.resta())

ejemplo1 = raiz()
print(ejemplo1.ingresardato())
print(ejemplo1.cuadrada())
