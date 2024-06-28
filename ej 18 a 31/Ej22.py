import random
import string

def generar_contrasenas(cantidad, longitud=8):
  
  caracteres = string.digits
  contrasenas = []
  for _ in range(cantidad):
    contrasena = "".join(random.choice(caracteres) for _ in range(longitud))
    contrasenas.append(contrasena)
  return contrasenas





cantidad_contrasenas = 10
longitud_contrasena = 6
contrasenas_generadas = generar_contrasenas(cantidad_contrasenas, longitud_contrasena)
print(f"Se generaron {cantidad_contrasenas} contraseñas de longitud {longitud_contrasena}:")
for contrasena in contrasenas_generadas:
  print(contrasena)
