def contar_mayusculas(cadena):
  contador_mayusculas = 0
  for caracter in cadena:
    if caracter.isupper():
      contador_mayusculas += 1
  return contador_mayusculas


cadena_usuario = input("Ingrese una cadena de texto: ")
cantidad_mayusculas = contar_mayusculas(cadena_usuario)
print(f"La cadena tiene {cantidad_mayusculas} letras mayúsculas.")
