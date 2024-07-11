"""La cuota de un club deportivo incrementa su costo todos los meses 
en un 2% respecto del mes anterior. Si el valor de la cuota en enero es de $1000, 
determinar el valor para el mes de abril."""

cuotaInicial = 1000

tasaIncremento = 0.02
"""para abril = 3, va contando de a un mes menos"""
numMeses = 3 

cuotaAbril = cuotaInicial * (1 + tasaIncremento) ** numMeses

print(f"El valor de la cuota en abril es: ${cuotaAbril:.2f}")
