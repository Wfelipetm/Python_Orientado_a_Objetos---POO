class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Quando precisa ter acesso ao contexto da classe -> Método de class
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

# Não precisa de contexto nem de class nem instacia do objeto -> Método estatico.
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa("Wallace", 36)
print(p.nome, p.idade)

p = Pessoa.criar_de_data_nascimento(1986, 4, 7, "Wallace")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
