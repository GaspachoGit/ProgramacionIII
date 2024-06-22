numero1 = float(input("Por favor, ingresa el primer número: "))
numero2 = float(input("Por favor, ingresa el segundo número: "))

if numero1 > numero2:
    mayor = numero1
elif numero2 > numero1:
    mayor = numero2
else:
    mayor = "ambos números son iguales"

if isinstance(mayor, str):
    print(f"No hay un número mayor, {mayor}.")
else:
    print(f"El mayor de los dos números es: {mayor}")
