import random

def lanzarDados(cantidadDados):
    suma = 0
    for _ in range(cantidadDados):
        suma += random.randint(1, 6)
    return suma

apuesta = float(input("Ingrese el monto de la apuesta: "))
cantidadDados = int(input("¿Con cuántos dados jugará? (1, 2 o 3): "))

sumaDados = lanzarDados(cantidadDados)

if cantidadDados == 1:
    if sumaDados > 4:
        ganancia = apuesta * 0.10
        resultado = "ganó"
    else:
        ganancia = -apuesta
        resultado = "perdió"
elif cantidadDados == 2:
    if sumaDados > 8:
        ganancia = apuesta * 0.50
        resultado = "ganó"
    else:
        ganancia = -apuesta
        resultado = "perdió"
elif cantidadDados == 3:
    if sumaDados == 18:
        ganancia = apuesta * 3.00
        resultado = "ganó"
    else:
        ganancia = -apuesta
        resultado = "perdió"
else:
    print("Cantidad de dados no válida.")
    ganancia = 0
    resultado = "no válido"

if resultado != "no válido":
    print(f"Usted {resultado}. La suma de los dados es {sumaDados}. Su ganancia es {ganancia}.")
else:
    print("Juego no válido.")
