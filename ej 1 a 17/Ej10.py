cadenaTexto = input("Ingresá una cadena de texto: ")
contadorVocales = 0
vocales = "aeiouAEIOU"

for char in cadenaTexto:
    if char in vocales:
        contadorVocales += 1

print(f"La cantidad de vocales en la cadena es: {contadorVocales}")
