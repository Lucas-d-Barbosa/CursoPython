

class Carro:
    def __init__(self, nome):
        self._nome = nome

    @property
    def motor(self):
        return self._motor.nome

    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        return self._fabricante._nome
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

class Motor:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nomeMotor):
        self._nome = nomeMotor
        

class Fabricante:
    def __init__(self, nome):
        self._nome = nome
        self._carros = []
    
    def adicionar_carro(self, carro):
        self._carros.append(carro)

    def listar_carros(self):
        for carro in self._carros:
            print(carro._nome)
        
fabricante1 = Fabricante("Toyota")
carro1 = Carro("Fusca")
motor1 = Motor("V4")
carro1.motor = motor1
carro1.fabricante = fabricante1 
print(carro1.motor)
print(carro1.fabricante)
carro1._fabricante.adicionar_carro(carro1)
carro1._fabricante.listar_carros()