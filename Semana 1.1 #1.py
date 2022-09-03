import math
SEPARADOR = ("*" * 20) + "\n"

valorFlotante = float(input("Introduce un valor con fracción decimal: \n"))
print(f"El siguiente entero hacia arriba de {valorFlotante} es {math.ceil(valorFlotante)}")
print(SEPARADOR)
print(f"El siguiente entero hacia abajo de{valorFlotante} es {math.floor(valorFlotante)}")
print(SEPARADOR)
print(f"Laparteenteratruncadade{valorFlotante} es {math.trunc(valorFlotante)}")
print(SEPARADOR*2)
pass

valorNumerico =int(input("Dame un valor entero: \n"))
print(f"La raiz a cuadrada de{valorNumerico}esiguala{math.sqrt(valorNumerico)}")
print(SEPARADOR)
print(f"El factorial de{valorNumerico}esiguala{math.factorial(valorNumerico)}")
potencia = int(input("Dame un valor entero : \n"))
print(f"El resultado de elevar {valorNumerico} ala {potencia}potencia es igual a {math.pow(valorNumerico,potencia)}")
print(SEPARADOR * 2)
pass
print(f"El valor de Pies{math.pi}")