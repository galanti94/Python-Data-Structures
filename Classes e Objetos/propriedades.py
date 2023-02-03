# A propriedade transforma um método em uma propriedade
class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

    # O deleter serviria para deixar a variável com um número estratégico para não quebrar o resto do código
    @x.deleter
    def x(self):
        self._x = -1

foo = Foo(10)
print(foo.x) # Consigo acessar um método com sintaxe de atributo

foo.x += 10
print(foo.x)