from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    # Forçando propriedade
    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTv(ControleRemoto):
    def ligar(self):
        print('ligando Tv...')
        print('Tv ligada!')

    def desligar(self):
        print('Desligando Tv...')
        print('Tv desligada!')

    @property
    def marca(self):
        return "NepTav"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('ligando ar...')
        print('Ar ligado!')

    def desligar(self):
        print('Desligando Ar...')
        print('Ar desligado!')

    @property
    def marca(self):
        return "NepTav"


controle = ControleTv()
controle.ligar()
controle.desligar()
print(f'Marca da Tv -> {controle.marca}')
print()

controle_ar = ControleArCondicionado()
controle_ar.ligar()
controle_ar.desligar()
print(f'Marca do AR Condicionado -> {controle_ar.marca}')
