import random
SEPARADOR=("*" * 20 ) + "\n"
print(f"Obteniendo un numero entero aleatorio que puede ir de l0 al 19: {random.randrange(20)}")
print(SEPARADOR)
print(f"Obteniendo un numero entero aleatorio par que puede ir de l2 al 20: {random.randrange(2,21,2)}")
print(SEPARADOR)
print(f"Obteniendo un valor numérico entre 0.0 y 1.0: {random.random()}")
print(SEPARADOR*2)

listaDePrueba=[10,20,30,40,15,25,35,45]
print(f"La lista de prueba es {listaDePrueba}")
print(f"El valor seleeccionado aleatoriamente de la lista anteriores {random.choice(listaDePrueba)}")
print(SEPARADOR)
random.shuffle(listaDePrueba)
print(f"La lista ya ' perturbada/barajada ' es{listaDePrueba}")