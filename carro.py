class Carro:
    def __init__(self,marca, modelo,cor,ano):
        self.marca = marca
        self.modelo = modelo 
        self.cor = cor 
        self.ano = ano

    def acelerar(self):
        print(f"O carro {self.marca} {self.modelo} {self.cor} {self.ano} esta acelerando")

    def frear(self):
        print(f"O carro {self.marca} {self.modelo} {self.cor} {self.ano} esta freiando")

carro1 = Carro ("Toyata", "Corolla", "vermelho", "2024")
carro2 = Carro ("Ferrari", "Enzo", "vermelho", "2004")

carro1.acelerar()
carro2.acelerar()

carro1.frear()
carro2.frear() 
