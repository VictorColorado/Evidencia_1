import sys
import os
SEPARADOR=("*" * 20) + "\n"#usodelmódulosys
lista=list()
for numero in range(1,1001):
    lista.append(numero)
print(f"La lista tiene{len(lista)}elementos,ytiene un tamaño de{sys.getsizeof(lista)}bytes")
    
print(SEPARADOR)

tupla = tuple(lista)
print(f"La tupla tiene{len(tupla)}elementos,y tiene un tamaño de {sys.getsizeof(tupla)}bytes")

print(SEPARADOR)

print(f"El directorio actual de trabajo es{os.getcwd()}")

for raiz, dirs, archivos in os.walk(".",topdown=False):
    for nombre in archivos:
        print(os.path.join(raiz, nombre))
    for nombre in dirs:
        print(os.path.join(raiz, nombre))