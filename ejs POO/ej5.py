class ParSuma:
    def __init__(self, numeros, objetivo):
        self.numeros = numeros
        self.objetivo = objetivo

    def encontrar_par(self):
        for i in range(len(self.numeros)):
            for j in range(i + 1, len(self.numeros)):
                if self.numeros[i] + self.numeros[j] == self.objetivo:
                    return (i, j)
        return None


numeros = [10, 20, 10, 40, 50, 60, 70]
objetivo = 50
par_suma = ParSuma(numeros, objetivo)
print(par_suma.encontrar_par())
