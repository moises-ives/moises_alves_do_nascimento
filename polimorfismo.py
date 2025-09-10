'''
O que é Polimorfismo?

É quando um mesmo método tem comportamentos diferentes dependendo da classe que o usa 

Pensa assim:

Todas as classes têm o método apresentar(),

Mas cada classe fala de um jeito próprio quando você chama esse método.
'''


class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def apresentar(self):
        print(f"Olá, eu sou {self.nome}.")

class Cliente(Pessoa):
    def apresentar(self): # mesmo nome, mas comportamento diferente
        print(f"Sou cliente {self.nome}, vim comprar algo.")

class Aluno(Pessoa):
    def apresentar(self): # mesmo nome, mas comportamento diferente
        print(f"Sou aluno {self.nome}, estou estudando.")

# Criando objetos
p = Pessoa("Carlos")
c = Cliente("Maria")
a = Aluno("João")

# Chamado o MESMO método "apresentar"
p.apresentar()
c.apresentar()
a.apresentar()
