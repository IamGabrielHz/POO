class Banco:
    def __init__(self, nome):
        self.__nome = nome
        self.__contas = []


    @property
    def nome(self):
        return self.__nome

    def Adicionar(self,conta):
        if type(conta) == Conta:
            self.__contas.append(conta)
            print('Conta adicionada com sucesso!')
        else:
            print('Impóssivel prosseguir!')
            raise TypeError
        
    def Remover(self,conta):
        if type(conta) == Conta:
            if conta.saldo == 0:
                self.__contas.remove(conta)
                print('Conta removida devido a valor zero em caixa!')
            else:
                print('Saldo diferente de 0! Impóssivel remover conta.')
        

    def valorTotal(self):
        total = 0
        for conta in self.__contas:
            total += conta.saldo
        return total

    def __str__(self):
        return f'O nome do banco é {self.__nome} e ele tem {self.valorTotal()} totais depositados.'


class Conta:
    def __init__(self,numero,titular,saldo = 0):
        self.__numero = numero
        self.__titular =  titular
        self.__saldo = saldo


    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self,valor):
        self.__saldo += valor
        print('Valor depositado com sucesso!')
    
    def sacar(self,valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print('Valor sacado com sucesso!')
        else:
            print('Saldo insuficiente!')

    def __str__(self):
        return f'O número dessa conta é {self.__numero}, o saldo da conta é {self.__saldo}.'

    
class Cliente:
    def __init__(self, cpf, nome):
        self.__cpf = cpf
        self.__nome = nome

    
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    def __str__(self):
        return f'O nome desse cliente é {self.__nome} e o seu cpf é {self.__cpf}'