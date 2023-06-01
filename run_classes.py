from classes import *

cliente1 = Cliente('034902384', 'Cleber')
cliente2 = Cliente('878573232', 'Alana')
cliente3 = Cliente('342342344', 'Josue')
cliente4 = Cliente('234234324','José')

conta1 = Conta('1', cliente1)
conta1.depositar(1000)
conta1.sacar(500)

conta2 = Conta('2', cliente2, 5000)
conta2.depositar(2000)

conta3 = Conta('3', cliente1, 1500)
conta3.depositar(500)

conta4 = Conta('4', cliente3, 3000)
conta4.depositar(1000)
conta4.sacar(200)

conta5 = Conta('5', cliente2, 800)

conta6 = Conta('6', cliente3, 2000)
conta6.depositar(300)

conta7 = Conta('7',cliente4, 0)

banco1 = Banco('Bradesco')
banco1.Adicionar(conta1)
banco1.Adicionar(conta2)

banco2 = Banco('Itaú')
banco2.Adicionar(conta3)
banco2.Adicionar(conta4)
banco2.Adicionar(conta5)

banco3 = Banco('Caixa')
banco3.Adicionar(conta6)
banco3.Adicionar(conta7)
banco3.Remover(conta7)


print(cliente1)
print(cliente2)
print(cliente3)

print(conta1)
print(conta2)
print(conta3)
print(conta4)
print(conta5)
print(conta6)

print(banco1)
print(banco2)
print(banco3)
