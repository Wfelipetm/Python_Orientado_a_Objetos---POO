'''
Polimorfismo com herança
Na herança, a classe filha herda os métodos da classe pai. No
entanto, é possível modificar um método em uma classe filha
herdada da classe pai. Isso é particularmente útil nos casos em
que o método herdado da classe pai não se encaixa
perfeitamente na classe filha.

'''


class Passaro:
    def voar(self): pass


class Pardal(Passaro):
    def voar(self):
        print("Pardal voa")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

# FIXME: Exemplo ruim do uso de herança para "ganhar" o método voar


class Avião(Passaro):
    def voar(self):
        print('Avião está decolando....')


def plano_de_voo(obj):
    obj.voar()


plano_de_voo(Pardal())
plano_de_voo(Avestruz())
plano_de_voo(Avião())
