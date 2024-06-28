def mostrar_informacion_personas(personas):
  personas_ordenadas = sorted(personas.items(), key=lambda item: item[0])

  for nombre_completo, correo_electronico in personas_ordenadas:
    print(f"{nombre_completo}: {correo_electronico}")

datos_personas = {
  "Caceres, Pedro": "usuario1@gmail.com",
  "Gomez, Gustavo": "usuario2@hotmail.com",
  "Lamas, Maria": "usuario3@hotmail.com"
}

mostrar_informacion_personas(datos_personas)
