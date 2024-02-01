# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança", "propriedades", "encapsulamento" e "classe abstrata".
from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self._nome = nome
        self.telefone = telefone
        self._renda_mensal = renda_mensal
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def renda_mensal(self):
        return self._renda_mensal
    
    @abstractmethod
    def obter_limite_saque(self):
        pass
    
    def __str__(self):
        return f'Nome: {self._nome}\t\tTelefone: {self.telefone}\t\tRenda mensal: {self.renda_mensal}'


class ClienteMulher(Cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)
    
    def obter_limite_saque(self):
        return self.renda_mensal


class ClienteHomem(Cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)
    
    def obter_limite_saque(self):
        return 0

class Operacao:
    def __init__(self, tipo, cliente: Cliente, valor):
        self.tipo = tipo
        self.cliente = cliente
        self.valor = valor
    
    def __str__(self):
         return f'\n--------------------\nOperação realizada: {self.tipo}\tValor: R$ {self.valor:.2f}\nCliente: {self.cliente.nome}'

class ContaCorrente:
    def __init__(self):
        self.saldo = 0
        self.operacoes = []
        self.clientes = []

    def adicionar_titular(self, cliente):
        self.clientes.append(cliente)

    def depositar(self, valor, cliente):
        tipo = 'deposito'
        if valor > 0:
            self.saldo += valor
            operacao = Operacao(tipo, cliente, valor)
            self.operacoes.append(operacao)
            print(f'Valor {valor} adicionado a conta!')
        else:
            print('Valor inválido!')
        
    def sacar(self, valor, cliente):
        tipo = 'saque'
        if valor > 0:
                limite_saque = cliente.obter_limite_saque()
                if valor <= limite_saque:
                    self.saldo =- valor

                    print(f'Saque de {valor} realizado!')
                    operacao = Operacao(tipo, cliente, valor)
                    self.operacoes.append(operacao)
                else:
                    print('Valor excedido! Impossivel realizar a operação!')

        else:
            print('Impossível realizar a operação. Informe um valor válido!')

    def historico_operacoes(self):
        for operacao in self.operacoes:
            print(operacao)
    

# Inicializando cliente mulher
ana = ClienteMulher('Ana Júlia', '96 982345678', 2000)
print(ana)
# Inicializando cliente homem
roberto = ClienteHomem('Roberto Ricardo', '98 98765432', 1500)
print(roberto)

# Inicializando conta
conta = ContaCorrente()
conta.adicionar_titular(ana)
conta.adicionar_titular(roberto)
# Depósito  
conta.depositar(500, roberto)

# Saque de cliente homem
conta.sacar(2000, roberto)

#Saque cliente mulher
conta.sacar(2000, ana)

conta.historico_operacoes()

