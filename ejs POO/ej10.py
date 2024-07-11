class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}')

    def es_mayor_de_edad(self):
        return self.edad >= 18

class Alumno(Persona):
    def __init__(self, nombre, edad, dni):
        super().__init__(nombre, edad, dni)
        self.notas = {}
        self.__comision = None

    def asignar_nota(self, materia, nota):
        self.notas[materia] = nota
        self.__asignar_comision()

    def __asignar_comision(self):
        promedio = sum(self.notas.values()) / len(self.notas)
        if self.edad > 17:
            self.__comision = 'N'
        elif promedio >= 8:
            self.__comision = 'A'
        elif promedio >= 6:
            self.__comision = 'B'
        else:
            self.__comision = 'C'

    def mostrar_notas(self):
        for materia, nota in self.notas.items():
            print(f'{materia}: {nota}')

    def obtener_comision(self):
        return self.__comision

class Profesor(Persona):
    def __init__(self, nombre, edad, dni, materia):
        super().__init__(nombre, edad, dni)
        self.materia = materia

    def evaluar(self, alumno, nota):
        alumno.asignar_nota(self.materia, nota)





alumno = Alumno('Pedro', 18, '12345678A')
profesor = Profesor('Ana', 30, '87654321B', 'Matemáticas')

profesor.evaluar(alumno, 7)
alumno.mostrar_notas() 
print(alumno.obtener_comision())  
