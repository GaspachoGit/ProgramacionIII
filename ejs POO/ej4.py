class Sublistas:
    def __init__(self, lista):
        self.lista = lista

    def obtener_sublistas(self):
        sublistas = []
        for i in range(len(self.lista)):
            for j in range(i + 1, len(self.lista) + 1):
                sublistas.append(self.lista[i:j])
        return [sublista for sublista in sublistas if sublista]


lista = [4, 5, 6]
sublistas = Sublistas(lista)
print(sublistas.obtener_sublistas())
