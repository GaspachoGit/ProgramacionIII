class Rectangulo:
    def __init__(self, punto_inicial=[0, 0], punto_final=[0, 0]):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def base(self):
        return abs(self.punto_final[0] - self.punto_inicial[0])

    def altura(self):
        return abs(self.punto_final[1] - self.punto_inicial[1])

    def area(self):
        return self.base() * self.altura()


rectangulo = Rectangulo([1, 1], [4, 5])
print('Base:', rectangulo.base())
print('Altura:', rectangulo.altura())
print('Área:', rectangulo.area())
