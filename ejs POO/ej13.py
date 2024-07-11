import getpass

class CuentaCorreo:
    def __init__(self):
        self.id = input("Ingrese el ID de correo: ")
        self.dominio = input("Ingrese el dominio de correo: ")
        self.__password = self.__solicitar_password()

    def __solicitar_password(self):
        pwd = getpass.getpass("Ingrese su password: ")
        confirm_pwd = getpass.getpass("Confirme su password: ")
        while pwd != confirm_pwd:
            print("Las contraseñas no coinciden. Inténtelo de nuevo.")
            pwd = getpass.getpass("Ingrese su password: ")
            confirm_pwd = getpass.getpass("Confirme su password: ")
        return pwd

    def cambiar_password(self):
        self.__password = self.__solicitar_password()

    def mostrar_correo(self):
        return f'{self.id}@{self.dominio}'


cuenta = CuentaCorreo()
print(cuenta.mostrar_correo())  
cuenta.cambiar_password()
