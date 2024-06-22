CantidadNumeros = 0
Positivos = 0

while True:
    numero = float(input("Ingrese un número real (ingrese un número negativo para finalizar): "))
    if numero < 0:
        break
    CantidadNumeros += 1
    if numero > 0:
        Positivos += 1

print(f"Se ingresaron un total de {CantidadNumeros} números.")
print(f"De esos números, {Positivos} son positivos.")
