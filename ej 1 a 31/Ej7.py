horasTrabajadas = float(input("ingresa el número de horas trabajadas en la semana: "))
precioPorHora = float(input("ingresa el precio que se paga por hora: "))

limiteHorasNormales = 35
tarifaExtra = 1.5


if horasTrabajadas <= limiteHorasNormales:
    salarioSemanal = horasTrabajadas * precioPorHora
else:
    horasExtra = horasTrabajadas - limiteHorasNormales
    salarioSemanal = (limiteHorasNormales * precioPorHora) + (horasExtra * precioPorHora * tarifaExtra)


print(f"El salario neto semanal es: ${salarioSemanal:.2f}")
