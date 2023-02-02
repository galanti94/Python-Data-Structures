
class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("O motor foi ligado!")


class Motocicleta(Veiculo):
    pass 


class Carro(Veiculo):
    pass 


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        # o super traz os atributos da classe pai
        super().__init__(cor, placa, numero_rodas)       
        self.carregado = carregado

    def esta_carregado(self):
        print(f"Tá carregado {'sim' if self.carregado else 'não'}") 

if __name__:
    moto = Motocicleta("Azul", "BXO1108", 2)
    caminhao = Caminhao("Preto", "kkj0932", 4, False)

    moto.ligar_motor()
    caminhao.esta_carregado()