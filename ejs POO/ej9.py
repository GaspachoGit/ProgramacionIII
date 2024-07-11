class NumeroEntero:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, otro):
        return NumeroEntero(self.valor + otro.valor)

    def __sub__(self, otro):
        return NumeroEntero(self.valor - otro.valor)

    def __mul__(self, otro):
        return NumeroEntero(self.valor * otro.valor)

    def __truediv__(self, otro):
        if otro.valor == 0:
            print("Error: División por cero")
            return NumeroEntero(0)
        return NumeroEntero(self.valor / otro.valor)

    def __str__(self):
        return str(self.valor)


num1 = NumeroEntero(10)
num2 = NumeroEntero(0)

print(num1 + num2)  
print(num1 - num2)  
print(num1 * num2)  
print(num1 / num2)  