class cartao:
    def __init__(self,numero, titular, cod_seguranca, validade = 'MM/AA', limite_de_compras = 1000.0, senha = None, status = 'bloqueado'):
        self.__numero = numero
        self.__titular = titular
        self.__validade = validade
        self.__limite_de_compras = limite_de_compras
        self.__cod_seguranca = cod_seguranca
        self.__senha = senha
        self.__fatura_a_pagar = 0
        self.__status = status
        self.__valor_minimo = self.__fatura_a_pagar * 0.3


    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self,titular):
        self.__titular = titular
    
    @property
    def validade(self):
        return self.__validade
    
    @property
    def limite_de_compras(self):
        return self.__limite_de_compras
    
    @property
    def cod_seguranca(self):
        return self.__cod_seguranca
    
    @property
    def senha(self):
        return self.__senha
    
    @property
    def fatura_a_pagar(self):
        return self.__fatura_a_pagar
    
    @property
    def valor_minimo(self):
        return self.__valor_minimo
    
    @property
    def status(self):
        return self.__status    
    
    def desbloquear(self):
        if self.__status != 'liberado':
            self.__status = 'liberado'
            print(self.__status)
        else:
            print(f'Este cartão já está liberado!')
    

    def bloquear(self):
        if self.__status != 'bloqueado':
            self.__status = 'bloqueado'
            print(self.__status)
        else:
            print(f'Este cartão já está bloqueado!')

    
    def mudar_senha(self):
        verif = int(input('Insira o código de segurança do cartão: '))
        if verif == self.__cod_seguranca and self.__senha != None:
            self.__senha = int(input('Insira a nova senha:'))
            print('Senha alterada!')
        elif verif != self.__cod_seguranca:
            print('Código de segurança inválido!')
        else:
            print('Você ainda não inseriu uma senha para esse cartão!')
            self.__senha = int(input('Insira uma nova senha: '))
            print('Senha definida!')

        
    def comprar(self):
        valor_compra = float(input('Insira o valor da compra: '))
        senha = int(input('Insira a senha do cartão: '))
        mes = int(self.__validade[:2])
        ano = int(self.__validade[3:])
        mes_atual = int(input('Insira o mês atual no formato MM: '))
        ano_atual = int(input('Insira o ano atual no formato AA: '))
        if valor_compra <= self.__limite_de_compras and self.__status == 'liberado'and mes >= mes_atual and ano >= ano_atual:
            if senha == self.__senha:
                print('Compra aprovada!')
                self.__limite_de_compras -= valor_compra
                self.__fatura_a_pagar += valor_compra
                self.__valor_minimo += self.__fatura_a_pagar * 0.3
            else:
                print('Senha incorreta!')
        elif valor_compra > self.__limite_de_compras:
            print('O valor da compra é maior que o limite!')
        elif self.__status != 'liberado':
            print('Cartão bloqueado!')
        elif ano < ano_atual or  ano == ano_atual and mes < mes_atual:
            print('Cartão vencido!')

    
    def pagar_fatura(self):
        valor_pago = float(input('Insira o valor que deseja pagar: '))
        if valor_pago >=self.__valor_minimo and valor_pago <= self.__fatura_a_pagar:
            print('Fatura paga!')
            self.__fatura_a_pagar -= valor_pago
            self.__limite_de_compras += valor_pago
        else:
            print('Valor inválido!')


    def __str__(self):
        return f'Número do cartão: {self.__numero}, Titular: {self.__titular}, Valor: {self.__fatura_a_pagar} e Valor Mínimo: {self.__valor_minimo}'
    

def main():
    cartoes = [cartao('1234567890123456', 'João Silva', 123, '01/25', 2000.0, 456,'liberado'),cartao('9876543210987654', 'Maria Souza', 789, '02/24', 1500.0, None,'bloqueado'),cartao('5678901234567890', 'José Santos', 345, '06/23', 1000.0, 678, 'liberado'),cartao('4321098765432109', 'Ana Paula', 901, '09/22', 500.0, 234, 'bloqueado')]
    cartoes[1].desbloquear()
    cartoes[0].bloquear()
    cartoes[1].mudar_senha()
    cartoes[2].comprar()
    cartoes[2].pagar_fatura()
    print(cartoes[3])


if __name__ == '__main__':
    main()