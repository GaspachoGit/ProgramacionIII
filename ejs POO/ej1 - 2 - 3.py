class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}')

    def es_mayor_de_edad(self):
        return self.edad >= 18

# persona1 = Persona('Juan', 20, '12345678A')
# persona1.mostrar()
# print(persona1.es_mayor_de_edad())  

#Ejercicio 2

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self._cantidad = cantidad

    def mostrar(self):
        print(f'Titular: {self.titular.nombre}, Cantidad: {self._cantidad}')

    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad

    def retirar(self, cantidad):
        self._cantidad -= cantidad
        
# persona1 = Persona('Juan', 20, '12345678A')
# cuenta1 = Cuenta(persona1, 100.0)
# cuenta1.mostrar()
# cuenta1.ingresar(50)
# cuenta1.mostrar()
# cuenta1.retirar(30)
# cuenta1.mostrar()

# EJERCICO 3

class CuentasBancarias:
    def __init__(self):
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def saldo_deudor(self):
        saldo_total = sum(cuenta._cantidad for cuenta in self.cuentas if cuenta._cantidad < 0)
        return saldo_total

    def mostrar_cuentas_con_saldo_negativo(self):
        for cuenta in self.cuentas:
            if cuenta._cantidad < 0:
                print(f'Titular: {cuenta.titular.nombre}, Saldo adeudado: {cuenta._cantidad}')


persona1 = Persona('Juan', 20, '12345678A')
persona2 = Persona('Maria', 22, '87654321B')

cuenta1 = Cuenta(persona1, -50.0)
cuenta2 = Cuenta(persona2, 200.0)

banco = CuentasBancarias()
banco.agregar_cuenta(cuenta1)
banco.agregar_cuenta(cuenta2)

print(banco.saldo_deudor())
banco.mostrar_cuentas_con_saldo_negativo()
