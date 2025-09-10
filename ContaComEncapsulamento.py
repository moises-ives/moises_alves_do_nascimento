# Exemplo Com Encapsulamento
# Usando atributos publicos, protegido e privado

class ContaBancaria:
    def __init__(self, titular, saldo_inicial, senha):
        # Público: pode ser acessado livremente
        self.titular = titular

        #Protegido: não deve ser alterado diretamente
        self._saldo = float(saldo_inicial)

        # Privado: não pode ser acessado diretamente
        self.__senha = str(senha)

    def ver_saldo(self, senha_digitada):
        #Verificar se a senha está correta
        if str(senha_digitada) == self.__senha:
            print(f'Saldo de {self.titular}: R${self._saldo:.2f}')
        else:
            print("Senha incorreta! Acesso negado.")


# Teste 
conta2 = ContaBancaria("Moisés", 1000.00, "1234")

# Consulta com senha correta
conta2.ver_saldo("1234")

# Alterando o público (permitido)
conta2.titular = "Moisés Atualizado"
conta2.ver_saldo("1234")

# Tentando alterar protegido (possível, mas não recomendado)
conta2._saldo = 50.00
conta2.ver_saldo("1234")

# Tentando acessar privado (não funciona)
try:
    print(conta2.__senha)
except AttributeError:
    print("Atributo privado não pode ser acessado diretamente")
    


