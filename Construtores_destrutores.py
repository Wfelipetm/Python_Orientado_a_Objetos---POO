class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe ... ")
        self.nome = nome
        self.com = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instància de classe.")

    def falar(self):
        print("auau")


def criar_cachorro():
    c = Cachorro(" Negão", " Preto ", False)
    print(c.nome)


c = Cachorro("Chappie", " amarelo")
c.falar()

print("ola mundo")

# del c  # se eu quiser deletar e continuar

print("ola mundo")
print("ola mundo")
criar_cachorro()
