n = int(input("Ingresá la cantidad de números enteros: "))
suma = 0

for i in range(n):
    numero = int(input(f"Ingresá el número {i+1}: "))
    suma += numero

print(f"La suma de los {n} números enteros es: {suma}")
