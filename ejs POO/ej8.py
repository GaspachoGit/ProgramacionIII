from datetime import date, datetime

class Fecha:
    def __init__(self, dia=1, mes=1, año=1900):
        self.dia = dia
        self.mes = mes
        self.año = año
        self.__validar()

    def __validar(self):
        if not (1 <= self.dia <= 31):
            self.dia = 1
        if not (1 <= self.mes <= 12):
            self.mes = 1
        if not (1900 <= self.año <= 2050):
            self.año = 1900

    def año_bisiesto(self):
        return (self.año % 4 == 0 and self.año % 100 != 0) or (self.año % 400 == 0)

    def dias_mes(self, mes):
        dias_por_mes = [31, 29 if self.año_bisiesto() else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return dias_por_mes[mes - 1]

    def hoy(self):
        hoy = date.today()
        return Fecha(hoy.day, hoy.month, hoy.year)

    def corta(self):
        return f'{self.dia:02d}-{self.mes:02d}-{self.año}'

    def larga(self):
        dias_semana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
        dia_semana = dias_semana[date(self.año, self.mes, self.dia).weekday()]
        meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
        return f'{dia_semana} {self.dia} de {meses[self.mes - 1]} de {self.año}'

    # Métodos getter y setter
    def get_dia(self):
        return self.dia

    def set_dia(self, dia):
        self.dia = dia
        self.__validar()

    def get_mes(self):
        return self.mes

    def set_mes(self, mes):
        self.mes = mes
        self.__validar()

    def get_año(self):
        return self.año

    def set_año(self, año):
        self.año = año
        self.__validar()


fecha = Fecha(2, 9, 2003)
print(fecha.corta())  
print(fecha.larga())  
print(fecha.año_bisiesto())  
print(fecha.dias_mes(2))  
