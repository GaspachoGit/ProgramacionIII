import matplotlib.pyplot as plt

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

class Rectangulo(Punto):
    def __init__(self, punto_inicial=None, punto_final=None):
        if punto_inicial is None:
            punto_inicial = Punto()
        if punto_final is None:
            punto_final = Punto()
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def base(self):
        return abs(self.punto_final.x - self.punto_inicial.x)

    def altura(self):
        return abs(self.punto_final.y - self.punto_inicial.y)

    def area(self):
        return self.base() * self.altura()

    def dibujar(self):
        x_values = [self.punto_inicial.x, self.punto_final.x, self.punto_final.x, self.punto_inicial.x, self.punto_inicial.x]
        y_values = [self.punto_inicial.y, self.punto_inicial.y, self.punto_final.y, self.punto_final.y, self.punto_inicial.y]
        plt.plot(x_values, y_values)
        plt.fill(x_values, y_values, 'b', alpha=0.1)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Rectángulo')
        plt.grid()
        plt.show()


punto1 = Punto(1, 1)
punto2 = Punto(4, 5)
rectangulo = Rectangulo(punto1, punto2)
print('Base:', rectangulo.base())  
print('Altura:', rectangulo.altura())  
print('Área:', rectangulo.area())  
rectangulo.dibujar()
