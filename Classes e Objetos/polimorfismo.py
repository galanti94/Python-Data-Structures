
class Passaro:
    def voar(self):
        print("Voando")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

class Aviao(Passaro):
    def voar(self):
        print("O avião está decolando")

def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Aviao())
plano_voo(Avestruz())