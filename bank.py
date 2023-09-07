class ContaBancaria():

    def __init__(self, tipo, cliente):
        self.tipo = tipo
        self.cliente = cliente
    
        pass

class ContaCorrente(ContaBancaria):

    def __init__(self, tipo, cliente, saldo, cartaoCredito):
        super().__init__(tipo, cliente)
        self.tipo = 'Corrente'
        self.cliente = cliente
        self.saldo = 0
        self.cartaoCredito = bool
    
    def deposito(valor):
        saldo =+valor
    
    def saque(valor, saldo):
        if (valor < saldo):
            print('Você não possui saldo suficiente para a operacao. Deseja utilizar cheque especial? ')
            autChequeEspecial = int(input())
            if autChequeEspecial == 1:
                chequeEspecial = valor - saldo
            else:
                print('Voce nao autorizou o cheque especial, portanto nao e possivel realizar o saque')
            
        
        else:
            print(f'Voce sacou {valor} da sua conta.')
            print(f'Seu saldo atual e {saldo}')
            return saldo - valor

class ContaPoupanca(ContaBancaria):
    def __init__(self, tipo, cliente, saldo):
        super().__init__(tipo, cliente)
        self.tipo = 'Poupanca'
        self.cliente = cliente
        self.saldo = 0   

    def deposito(valor):
        saldo =+ valor
    
    def saque(valor, saldo):
        if valor > saldo:
            print('Voce nao tem saldo suficiente para esta operacao!')
        else:
            saldo = saldo - valor

class ContaUniversitaria(ContaBancaria):
    def __init__(self, tipo, cliente, saldo):
        super().__init__(tipo, cliente)
        self.tipo = 'Universitaria'
        self.cliente = cliente
        self.saldo = 0
    
    def deposito(valor):
        saldo =+ valor
    
    def saque(valor):
        if valor > 200:
            print('Limite excedido de saque!')
        elif valor > 200 and valor > saldo:
            print('Voce nao tem saldo suficiente para saque e limite excedido!')
        else:
            saldo = valor - saldo
        

cliente = input('Digite seu nome: ')

print('Digite o tipo de conta: ')
print('1. Conta Corrente: ')
print('2. Conta Poupanca: ')
print('3. Conta Universitaria: ')

tipoConta = int(input())


if tipoConta == 1:
    newCliente = ContaCorrente(tipoConta, cliente, 0, bool)
    saldo = 0
    print('Deseja operar sua conta?')
    print('1. Sim')
    print('2. Nao')
    operar = int(input())

    if operar == 1:
        print('Escolha a opcao desejada: ')
        print('1. Cartao de Credito')
        print('2. Deposito')
        print('3. Saque')
        print('4. Sair')
        tipoOperacao = int(input())

        while tipoOperacao != 4:
            if tipoOperacao == 1:
                print('Você deseja cartao de credito?')
                print('1. Sim')
                print('2. Nao')
                cartaoCredito = int(input())
                if cartaoCredito == 1:
                    print('Voce tem cartao!')
                    
                elif cartaoCredito == 2:
                    print('Voce recusou o cartao')
                    
                else:
                    print('Opção invalida')
            
                
            elif tipoOperacao == 2:
                input('Você deseja depositar?')
                break
            elif tipoOperacao == 3:
                input('Voce deseja sacar? ')
                break
            elif tipoOperacao == 4:
                input('Voce finalizou suas operacoes')
                break
            else:
                input('Operacao invalida')
    
    elif operar == 2:
        print('Obrigado por utilizar os servicos!')
    
    else:
        print('Opcao invalida!')

if tipoConta == 2:
    newCliente = ContaPoupanca(tipoConta, cliente, 0)
    saldo = 0
    print('Deseja operar sua conta?')
    print('1. Sim')
    print('2. Nao')
    operar = int(input())

    if operar == 1:
        print('Escolha a opcao desejada: ')
        print('1. Deposito')
        print('2. Saque')
        print('3. Sair')
        tipoOperacao = int(input())
    
    elif operar == 2:
        print('Obrigado por utilizar os servicos')
    
    else:
        print('Opcao invalida!')

if tipoConta == 3:
    newCliente = ContaUniversitaria(tipoConta, cliente, 0)
    saldo = 0
    print('Deseja operar sua conta?')
    print('1. Sim')
    print('2. Nao')
    operar = int(input())

    if operar == 1:
        print('Escolha a opcao desejada: ')
        print('1. Deposito')
        print('2. Saque')
        print('3. Sair')
        tipoOperacao = int(input())
    
    elif operar == 2:
        print('Obrigado por utilizar os servicos')
    
    else:
        print('Opcao invalida!')
