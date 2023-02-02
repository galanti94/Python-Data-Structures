# Construtores sempre são executados no instanciamento de uma classe __init__
# Destrutores destroem coisas quando a instância é destruída; libera memória; mais importante para C++
# Tudo que tem __ são chamados de métodos especiais

class Cachorro:
    def __init__(self, nome, raca, acrodado = True):
        print("Iniciando a classe")
        self.nome = nome
        self.raca = raca
        self.acordado = acrodado

    def __del__(self):
        print("Destruindo minha classe...")

cachorro = Cachorro("Tixe", "Vira-lata")
