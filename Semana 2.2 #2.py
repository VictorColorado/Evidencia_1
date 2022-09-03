SEPARADOR = ("*" * 20) + "\n"
cola = list()
for cantidad in range(5):
    nuevo = input("Nombre del recién llegado: ")
    cola.append(nuevo)
    
print(f"Se agregaron {len(cola)}, elementos:")
for elemento in cola:
    print(elemento)
print(SEPARADOR)

print("Procedemos a retirarlos de la cola")
while cola:
    print(cola.pop(0))
pass