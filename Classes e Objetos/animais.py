
class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas
        


    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):        
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):      
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass


class Ornitorrinco(Ave, Mamifero):
    pass

# Quando usamos herança múltipla, precisamos usar chave-valor na criação de instâncias
# Rapidamente o código vira um monstro complexo
gato = Gato(cor_pelo="Branco", numero_patas = 4)
print(gato)

ornito = Ornitorrinco(cor_bico="Laranja", cor_pelo="Branco", numero_patas=4)
print(ornito)