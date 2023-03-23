class filme:
    nome = None
    direçao = None
    data_lançamento = None
    genero = None
    duraçao = None
    orçamento = None
    receita = None
    visualizacoes = None
    idioma_dub = None
    idioma_leg = None
    sucessor = None
    antecessor = None
    data_de_adiçao = None
    nota = []
    status = None
    catalogo = []


    def dublar (self,idioma_dub):
        self.idioma_dub = idioma_dub


    def legendar (self,idioma_leg):
        self.idioma_leg = idioma_leg

    
    def aumentar_vizu (self):
        self.visualizacoes += int(input())
    

    def sequencia (self,sucessor):
        self.sucessor = sucessor


    def critica (self,nota):
        self.nota = nota 


    def add_streaming (self,data_de_adiçao):
        self.data_de_adiçao = data_de_adiçao


    def player (self,status):
        self.status = status


    def catlog (self,catalogo):
        self.catalogo = catalogo


produçao = filme()
produçao.nome = 'Harry Potter e Pedra Filosofal'
produçao.direçao = 'Chris Columbus'
produçao.data_lançamento = '16/11/2001'
produçao.genero = 'Aventura e Fantasia'
produçao.duraçao = '195 minutos'
produçao.orçamento = 'US$ 125 milhões'
produçao.receita = 1000000000
produçao.visualizacoes = 320000
produçao.idioma_leg = 'PT-BR'
produçao.nota = '6.5/10'
produçao.status = 'Playing'

print(f'O filme escolhido foi {produçao.nome}')
print(f'Que foi dirigido por {produçao.direçao}')
print(f'Sendo lançado em {produçao.data_lançamento}')
print(f'Classificado como {produçao.genero}')
print(f'Tendo duraçao de {produçao.duraçao}')
print(f'Gastando {produçao.orçamento} para ser produzido')
print(f'Com uma receita atual de {produçao.receita}')
print(f'Sendo visto no momento por {produçao.visualizacoes} de espectadores')
print(f'Sendo exibido legendado em {produçao.idioma_leg}')
print(f'Sendo avaliado atualmente pela crítica com uma note de {produçao.nota}')
print(produçao.status)


produçao.dublar('Português Brasil')
produçao.player('Paused')
produçao.catlog('HBO Max')
produçao.aumentar_vizu()
produçao.sequencia('Harry Potter e a Câmara Secreta')
produçao.critica('7.0/10')
produçao.add_streaming('23/04/2020')


print(f'O filme {produçao.nome}')
print(f'Teve um aumento de espectadores para {produçao.visualizacoes}')
print(f'E foi traduzido para {produçao.idioma_dub}')
print(f'Tendo uma média de notas de {produçao.nota}')
print(f'Acabou também por receber uma sequência nomeada de {produçao.sucessor}')
print(f'Com tudo isso esse filme foi adicionado a todas as plataformas de streaming no dia {produçao.data_de_adiçao}, na(s) plataforma(s) {produçao.catalogo}')
print(produçao.status)