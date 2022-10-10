class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula) -> None:
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f'{self.nome} - {self.matricula} - {self.escola}'


def mostrar_valores(*obj):
    for obj in obj:
        print(obj)


aluno_01 = Estudante('Wallace', "01")
aluno_02 = Estudante("Marina", "10")
aluno_03 = Estudante("João", "06")
mostrar_valores(aluno_01, aluno_02, aluno_03)

aluno_01.matricula = 36
Estudante.escola = "Neptav"
mostrar_valores(aluno_01, aluno_02, aluno_03)
