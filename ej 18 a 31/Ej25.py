def modificar_por_referencia(lista):	
  lista.append(100)

def modificar_por_valor(lista_copia):
  lista_copia.append(100)
  return lista_copia

lista_original = [1, 2, 3]

modificar_por_referencia(lista_original)
print(f"Lista original después de modificar por referencia: {lista_original}")  

lista_modificada = modificar_por_valor(lista_original.copy()) 
print(f"Lista original después de modificar por valor: {lista_original}") 
print(f"Lista modificada por valor: {lista_modificada}")  
