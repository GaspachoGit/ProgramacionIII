def separar_pares_impares(lista):
  pares = []
  impares = []
  for numero in lista:
    if numero % 2 == 0:
      pares.append(numero)
    else:
      impares.append(numero)
  pares.sort()
  impares.sort()
  return pares, impares




lista = [1, 2, 3, 4, 5, 6]
pares, impares = separar_pares_impares(lista)
print(f"Pares: {pares}")
print(f"Impares: {impares}")
