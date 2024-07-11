#Calcular el área y el perímetro de un rectángulo, para lo cual se deben ingresar el valor del lado A y el valor del lado B. 

lado_a = float(input("Por favor, ingresa el valor del lado A: "))
lado_b = float(input("Por favor, ingresa el valor del lado B: "))

area = lado_a * lado_b
perimetro = (2 * lado_a) + (2 * lado_b)

print(f"el área es {area} y el perímetro es {perimetro}")