cantidadNumeros = int(input("Ingresá la cantidad de números reales: "))
contadorPositivos = 0

for i in range(cantidadNumeros):
    numero = float(input(f"Ingresá el número {i+1}: "))
    if numero > 0:
        contadorPositivos += 1

print(f"La cantidad de números positivos es: {contadorPositivos}")
