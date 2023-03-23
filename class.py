class human:
    nome = None
    sexo = None
    etnia = None
    idade = None
    peso = None
    e_civil = None


    def mudar_nome(self,nome):
        self.nome = nome


    def envelhecer(self):
        self.idade += 1


    def engordar(self,peso):
        self.peso += peso


    def emagrecer(self,peso):
        self.peso -= peso

    def mudar_e_civil(self,e_civil):
        self.e_civil = e_civil


evoluir = human()
evoluir.nome = 'Maria Clara'
evoluir.sexo = 'Feminino'
evoluir.etnia = 'Branca'
evoluir.idade = 23
evoluir.peso = 49
evoluir.e_civil = 'Solteira'


evoluir.mudar_nome('Indyara')
evoluir.envelhecer()
evoluir.engordar(3)


print(f'O nome desse humano agora é {evoluir.nome}.')
print(f'Ele pesa atualmente {evoluir.peso} kg.')
print(f'Sua idade atual {evoluir.idade} anos.')