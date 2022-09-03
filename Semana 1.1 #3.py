import time
SEPARADOR=("*" * 20) + "\n"

segundos=int(input("Cantidad de segundos a esperar: \n"))
time.sleep(segundos)
print(f"Han transcurrido,por lo menos,{segundos}segundos")
print(SEPARADOR*2)

print("Iniciaremos la medición de un proceso simulado")

horaInicial=time.time()
for termino in range(10):
    time.sleep(segundos)

print("proceso simulado concluído!")
duracion=time.time() - horaInicial
print(f"La duración del proceso simulado fue de{duracion}segundos")