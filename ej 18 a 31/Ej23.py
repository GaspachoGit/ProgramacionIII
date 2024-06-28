def concatenar_cadenas(*cadenas):
  oracion_concatenada = " ".join(cadenas)
  return oracion_concatenada




	
cadena1 = "Hola"
cadena2 = "mundo"
cadena3 = "!"

oracion_completa = concatenar_cadenas(cadena1, cadena2, cadena3)
print(f"Oración concatenada: {oracion_completa}")
