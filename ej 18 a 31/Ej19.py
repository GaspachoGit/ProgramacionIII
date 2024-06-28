def elevar_lista(lista, exponente):
  """
  Función que eleva cada elemento de una lista a un exponente dado.

  Parámetros:
    lista (list): La lista de números.
    exponente (int): El exponente al que se elevarán los elementos.

  Retorno:
    list: Una nueva lista con los elementos de la lista original elevados al exponente.
  """
  return [numero**exponente for numero in lista]

# Ejemplo de uso
lista = [2, 3, 4]
exponente = 3
lista_elevada = elevar_lista(lista, exponente)
print(f"Lista original: {lista}")
print(f"Lista elevada al exponente {exponente}: {lista_elevada}")
