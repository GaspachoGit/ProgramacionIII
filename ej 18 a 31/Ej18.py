def suma_multiplicacion(lista):
  if not lista:
    return 0, 0
  suma = lista[0]
  multiplicacion = 1
  for numero in lista[1:]:
    suma += numero
    multiplicacion *= numero
  return suma, multiplicacion

lista = [1, 2, 3, 4, 5]
suma, multiplicacion = suma_multiplicacion(lista)
print(f"Suma: {suma}")
print(f"Multiplicación: {multiplicacion}")
