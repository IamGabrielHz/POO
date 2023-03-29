class Human:
    def __init__(self, nome=None, sexo=None, etnia=None, idade=None, peso=None, e_civil=None):
        self.nome = nome
        self.sexo = sexo
        self.etnia = etnia
        self.idade = idade
        self.peso = peso
        self.e_civil = e_civil

    def mudar_nome(self, nome):
        self.nome = nome

    def envelhecer(self, anos=1):
        self.idade += anos

    def engordar(self, peso=1):
        self.peso += peso

    def emagrecer(self, peso=1):
        self.peso -= peso

    def mudar_e_civil(self, e_civil):
        self.e_civil = e_civil

pessoa = Human(nome='Maria Clara', sexo='Feminino', etnia='Branca', idade=23, peso=49, e_civil='Solteira')

pessoa.mudar_nome('Indyara')

pessoa.envelhecer(anos=3)

pessoa.engordar(peso=5)

print(f'O nome dessa pessoa agora é {pessoa.nome}.')
print(f'Ela pesa atualmente {pessoa.peso} kg.')
print(f'Sua idade atual é {pessoa.idade} anos.')