cadena = input("Ingrese una palabra o frase para verificar si es un palíndromo: ")
cadena = cadena.replace(" ", "").lower()

if cadena == cadena[::-1]:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for asignatura in asignaturas:
    nota = input(f"Ingrese la nota de {asignatura}: ")
    notas.append(nota)

for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} sacó {notas[i]}.")
