class Moneda:
    conversion_rates = {
        "EUR": 1.0,
        "USD": 1.1,
        "ARG": 120.0,
        "YEN": 130.0
    }

    def __init__(self, cantidad, unidad):
        self.cantidad = cantidad
        self.unidad = unidad

    def __add__(self, otra):
        if isinstance(otra, Moneda):
            total = self.cantidad + (otra.cantidad * Moneda.conversion_rates[otra.unidad] / Moneda.conversion_rates[self.unidad])
            return Moneda(total, self.unidad)
        elif isinstance(otra, (int, float)):
            return Moneda(self.cantidad + otra, self.unidad)
        else:
            raise TypeError("La operación de suma sólo es válida con Moneda o números.")

    def __radd__(self, otra):
        return self.__add__(otra)

    def __str__(self):
        return f'{self.cantidad:.2f} {self.unidad}'


moneda1 = Moneda(100, "EUR")
moneda2 = Moneda(110, "USD")

print(moneda1 + moneda2)  
print(moneda1 + 50)   
print(50 + moneda1)  
