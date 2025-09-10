'''
o que é Abstração 

É esconder os detalhes internos de implementação e mostrar apenas o que é necessário.

A ideia é trabalhar no nível mais genérico e deixar que as classes 
mais específicas implementem os detalhes.

'''

from abc import ABC, abstractmethod

# Classe abstrata (não pode ser instanciada diretamente)
class Pessoa(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def apresentar(self): # método abstrato (obrigatório para as filhas)
        pass

# Classe concreta Cliente
class Cliente(Pessoa):
    def apresentar(self):
        print(f"Sou cliente {self.nome}, comprando no sistema.")

# Classe concreta Aluno
class Aluno(Pessoa):
    def apresentar(self):
        print(f"Sou aluno {self.nome}, estudando no sistema.")

# p = Pessoa("Carlos")  # Isso dá erro: Pessoa é abstrata!

c = Cliente("Maria")
a = Aluno("João")

c.apresentar()
a.apresentar()

