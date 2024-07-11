#Solicitar al usuario que ingrese su edad, saludarlo y decirle que edad tendría dentro de 730 días.

nombre = input("Ingresá tu nombre: ")
edadActual = int(input("Ingresá es tu edad actual: ")) 

edadFutura = edadActual +2

print(f"Hola {nombre}! La edad que vas a tener en 730 días es de {edadFutura} años")