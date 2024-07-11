nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M para Mujer, H para Hombre): ")
nombre = nombre.lower()

if (sexo == "M" and nombre < 'm') or (sexo == "H" and nombre > 'n'):
    grupo = "A"
else:
    grupo = "B"

print(f"Usted pertenece al grupo {grupo}.")
