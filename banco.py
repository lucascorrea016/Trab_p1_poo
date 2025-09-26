'''3 - Crie uma classe que apresente os seguinte atributos:
      Class Banco(numero, nome, saldo, nome do banco, agencia) <-- atributos
        - Métodos
            - transferir - TED, sacar, PIX, Cheque_especial, emprestimo, crédito
            - transferir - TED se eu tiver a quantia em conta -- tem um % cobrado se o banco for diferente
            - PIX só posso realizar o pix se eu tiver isso em conta
            - Cheque_especial --> o seu saldo precisa ser < 0 ele tem juros -- nada de ter time
            - Empréstimo --> Comprar um casa e solicita um empréstimo ao banco e seu perfil será avaliado
             - Crédito --> é quando você quer comprar algo e ter um saldo < ou > que o valor do produto e terá um cobrança no final do mês
            - Crédito deve ter um relatório de ações.'''

class Banco:
    def __init__(self, numero: str, nome: str, saldo: float, banco: str, agencia: str):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
        self.banco = banco
        self.agencia = agencia
        self.credito_pendente = []
        self.relatorio_credito = []

    def __str__(self):
        return (f"Cliente: {self.nome}\n"
                f"Conta: {self.numero} | Agência: {self.agencia} | Banco: {self.banco}\n"
                f"Saldo: R${self.saldo:.2f}")
    
    def sacar(self, valor: float):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso! \nSaldo atual: R${self.saldo}.")
        else:
            print("Saldo insuficiente para saque!")

    def TED(self, valor: float, banco_destino: str):

        if valor <= self.saldo:
            taxa = 0
            if banco_destino != self.banco:
                taxa = valor * 0.01
            total = valor + taxa

            if total <= self.saldo:
                self.saldo -= total
                print(f"TED de R${valor:.2f} enviado para {banco_destino}. \nTaxa: R${taxa:.2f}.")
            else:
                print("Saldo insuficiente para realizar TED.")
        else:
            print("Saldo insuficiente para realizar TED.")
    def pix(self, valor: float):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"PIX de R${valor:.2f} realizado. \nSaldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para realizar o PIX!")

    def cheque_especial(self, valor: float):
        if self.saldo < 0:
            juros = valor * 0.1
            self.saldo -= (valor + juros)
            print(F"Cheque especial de R${valor:.2f} usado. \nJuros: R${juros:.2f}. \nSaldo atual: R${self.saldo:.2f}")
        else:
            print("Você só pode utilizar cheque especial se seu saldo for negativo.")

    def emprestimo(self, valor: float, finalidade: str = 'casa'):
        if self.saldo >= 1000:
            self.saldo += valor
            print(f"Empréstimo de R${valor:.2f} aprovado para {finalidade}. \nSaldo atual: R${self.saldo:.2f}")
        else:
            print("Perfil não aprovado para empréstimo.")

    def credito(self, valor: float, produto: str):
        self.credito_pendente.append(valor)
        self.relatorio_credito.append(f"Compra: {produto} - R${valor:.2f}")
        print(f"Compra de R${valor:.2f} em '{produto}' realizada com sucesso.")

    def fechar_fatura_credito(self):
        if not self.credito_pendente:
            print("Nenhuma compra no crédito para fechar.")
            return
        
        total = sum(self.credito_pendente)
        if total <= self.saldo:
            self.saldo -= total
            print(f"Fatura de R${total:.2f} paga! \nSaldo atual: R${self.saldo:.2f}")
        else:
            print(f"Fatura de R${total:.2f} não realizada! \nSaldo insuficiente.")

            self.credito_pendente = []

    def relatorio_de_credito(self):
        print("\nRelatório de Crédito")
        for acao in self.relatorio_credito:
            print(acao)
        print("-----------------------")

cliente = Banco("12345-6", "Lucas", 2500.00, "Santander", "0012")

while True:
    print(f"\n{cliente}")
    print("\n---Menu Principal---")
    print("1 - Sacar")
    print("2 - TED")
    print("3 - PIX")
    print("4 - Cheque Especial")
    print("5 - Empréstimo")
    print("6 - Crédito (compra)")
    print("7 - Fechar Fatura de Crédito")
    print("8 - Relatório de Crédito")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("\nDigite o valor do saque: "))
        cliente.sacar(valor)

    elif opcao == "2":
        valor = float(input("\nDigite o valor do TED: "))
        banco_destino = input("Digite o nome do banco destino: ")
        cliente.TED(valor, banco_destino)

    elif opcao == "3":
        valor = float(input("\nDigite o valor do PIX: "))
        cliente.pix(valor)

    elif opcao == "4":
        valor = float(input("\nDigite o valor do Cheque especial: "))
        cliente.cheque_especial(valor)

    elif opcao == "5":
        valor = float(input("\nDigite o valor do empréstimo: "))
        finalidade = input("Finalidade do empréstimo: ")
        cliente.emprestimo(valor, finalidade)

    elif opcao == "6":
        valor = float(input("\nDigite o valor da compra no crédito: "))
        produto = input("Nome do produto: ")
        cliente.credito(valor, produto)

    elif opcao == "7":
        cliente.fechar_fatura_credito()

    elif opcao == "8":
        cliente.relatorio_de_credito()

    elif opcao == "0":
        print("\nEncerrando o sistema. Até logo!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")