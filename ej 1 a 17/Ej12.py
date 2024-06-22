cadena = input("Ingrese una palabra o frase para verificar si es un palíndromo: ")
cadena = cadena.replace(" ", "").lower()

if cadena == cadena[::-1]:
    print("La cadena ingresada es un palíndromo.")
else:
    print("La cadena ingresada NO es un palíndromo.")
