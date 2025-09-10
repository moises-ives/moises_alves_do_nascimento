
class Pessoa:
    def __init__(self,nome,idade,cidade,exemplo_carro2,Carro):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.exemplo_carro2 = exemplo_carro2

    def apresentar(self):
        print(f"Olá sou o {self.nome} tenho {self.idade} anos e moro {self.cidade}")
    def digirir(self):
        print(f"{self.nome} está diringindo o {self.exemplo_carro2.marca} {self.exemplo_carro2.modelo} {self.exemplo_carro2.cor} {self.exemplo_carro2.ano}")
        self.exemplo_carro2.acelerar
       
meu_carro = carro ("ford", "fiesta", "vermelho", "2016") # type: ignore
pessoa1 = Pessoa ("Renato", "16", "São Paulo", meu_carro)

pessoa1.apresentar()
pessoa1.digirir()