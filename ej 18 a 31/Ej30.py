import random
import string

def generarPalabra(longitud):
    return ''.join(random.choices(string.ascii_lowercase, k=longitud))

def generarParrafo(cantidadPalabras):
    parrafo = ' '.join(generarPalabra(random.randint(4, 10)) for _ in range(cantidadPalabras))
    return parrafo.capitalize() + '.'

def parrafos(cantidadParrafos, palabrasPorParrafo):
    texto = '\n\n'.join(generarParrafo(palabrasPorParrafo) for _ in range(cantidadParrafos))
    return texto

cantidadParrafos = int(input("Ingrese la cantidad de párrafos: "))
palabrasPorParrafo = int(input("Ingrese la cantidad de palabras por párrafo: "))

textoGenerado = parrafos(cantidadParrafos, palabrasPorParrafo)
print(textoGenerado)
