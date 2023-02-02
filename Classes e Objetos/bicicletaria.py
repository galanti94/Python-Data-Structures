
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("A bicicleta está buzinando")

    def parar(self):
        print("A bicicleta está parada")

    def correr(self):
        print("A bicicleta está correndo")

    def __str__(self):
        return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"


bicicleta1 = Bicicleta("Azul", "Yamaha", "2023", 3000)

bicicleta1.buzinar()
print(bicicleta1)