import uuid
import datetime as dt
class Paciente:
    def __init__(self,id_pac,nome_pac,dt_nasc,contato):
        self.__id_paciente = id_pac
        self.nome_paciente = nome_pac 
        if type(dt_nasc) == dt.date:
            self.__dt_nasc = dt_nasc
        else:
            raise Exception('Error!')
        self.__contato = contato

        @property
        def id_paciente(self):
            return self.__id_paciente
        @property
        def dt_nasc(self):
            return self.__dt_nasc
        @property
        def contato(self):
            return self.__contato
        
    def __str__(self):
       return f"ID: {self.__id_paciente}, Nome: {self.nome_paciente}, Data de Nascimento: {self.__dt_nasc}, Contato: {self.__contato}"

class Medico:
    def __init__(self,id_medico,crm,nome_medico,esp):
        self.__id_medico = id_medico
        self.__crm = crm
        self.nome_medico = nome_medico
        self.especialidade = esp

        @property
        def __id(self):
            return self.__id
        @property
        def __crm(self):
            return self.__crm
        
    def __str__(self):
        return f"ID: {self.__id_medico}, CRM: {self.__crm}, Nome: {self.nome_medico}, Especialidade: {self.especialidade}"
        
class ConsultaMedica:
    def __init__(self,id,medico,paciente,data,pago=False):
        self.__id = id
        if type(medico)==Medico:
            self.__medico = medico
        else:
            raise Exception('Error!')
        if type(paciente)==Paciente:
            self.__paciente = paciente
        else:
            raise Exception('Error!')
        if type(data) == dt.date and data >= dt.date.today():
            self.__data = data
        else:
            raise Exception('Error!')
        self.__data = data
        self.__pago = pago
        self.__data_retorno = None

        @property
        def __id(self):
            return self.__id
        @property
        def __medico(self):
            return self.__medico
        @property
        def __paciente(self):
            return self.__paciente
        @property
        def __data(self):
            return self.__data
        @property
        def __pago(self):
            return self.__pago
        @property
        def __data_retorno(self):
            return self.__data_retorno
        
    def pagar(self):
        self.__pago = True

    def retorno(self,nova_data):
        self.__data_retorno = dt.date(int(input('Insira o ano da nova da consulta: ')),int(input('Insira o mês da nova da consulta: ')), int(input('Insira o dia da nova da consulta: ')))

    def __str__(self):
        return f'Consulta marcada para a data: {self.__data}\nPaciente:{self.__paciente.nome_paciente}\nMédico:{self.__medico.nome_medico}'


def menu():
  print("1 - Cadastrar Paciente")
  print("2 - Cadastrar Médico")
  print("3 - Marcar consulta")
  print("4 - Pagar consulta")
  print("5 - Cancelar consulta")
  print("6 - Marcar retorno")
  print("7 - Sair")
  
pacientes = []
medicos = []
consultas = []

while True:
    menu()
    op = int(input("Entre com a opção: "))
    if op==1:
        # dar os inputs para os atributos
        id_pac = uuid.uuid4()
        nome_pac = input('Insira o nome do paciente: ')
        data_n = dt.date(int(input('Insira o ano de nascimento do paciente: ')),int(input('Insira o mês de nascimento do paciente: ')), int(input('Insira o dia de nascimento do paciente: ')))
        ctt = input('Insira o telefone para contato do paciente: ')
        # criar o objeto
        novo_paciente = Paciente(id_pac.node,nome_pac,data_n,ctt)
        # inserir na lista
        pacientes.append(novo_paciente)
        print(f'Paciente {nome_pac} cadastrado!')

    elif op==2:
        # dar os inputs para os atributos
        id_med = uuid.uuid4()
        nome_med = input('Insira o nome do médico:')
        crm = input('Insira o CRM do médico correspondente: ')
        espec = input('Insira a especialidade do médico correspondente: ')
        # criar o objeto
        novo_medico = Medico(id_med.node,crm,nome_med,espec)
        # inserir na lista
        medicos.append(novo_medico)
        print(f'Médico {nome_med} cadastrado!')

    elif op==3:
        # dar os inputs para os atributos
        id_consulta = uuid.uuid4()
        data_cons = dt.date(int(input('Insira o ano da consulta: ')),int(input('Insira o mês da consulta: ')), int(input('Insira o dia da consulta: ')))
        # pegar o nome do paciente
        for i,valor in enumerate(pacientes):
           print(f'Índice: {i}| {valor} |')
        # buscar na lista de pacientes o objeto correspondente
        num_p = int(input('Insira o índice correspondente ao paciente desejado: '))
        # pegar o nome do medico
        for i,valor in enumerate(medicos):
           print(f'Índice: {i}| {valor} |')
        #buscar na lista de médicos o objeto correspondente
        num_m = int(input('Insira o índice do médico desejado: '))
        #criar o objeto ConsultaMedica
        nova_consulta = ConsultaMedica(id_consulta.node,medicos[num_m],pacientes[num_p],data_cons)
        # inserir na lista de consultas médicas
        consultas.append(nova_consulta)
        print('Consulta marcada!')

    elif op==4:
        # pegar na lista de consultas (por data, por nome do paciente ou por nome do médico)
        print('''
        Como deseja buscar as consultas:
         1 - Data
         2 - Nome do paciente
         3 - Nome do médico ''')
        rsp = int(input())
        # retornar o objeto correspondente ao critério da pesquisa
        if rsp == 1: 
            data = input("Insira a data da consulta (no formato dd/mm/aaaa): ")
            for i,valor in enumerate(consultas):
               if valor._ConsultaMedica__data.strftime('%d/%m/%Y') == data:
                    print(f'Índice: {i}| {valor} |')
                    esc = int(input('Qual consulta deseja pagar?: '))
                    consultas[esc].pagar()
                    print('Consulta paga!')
        if rsp == 2:
            nome_paciente = input("Insira o nome do paciente: ")
            for i,valor in enumerate(consultas):
               if valor._ConsultaMedica__paciente.nome_paciente.lower() == nome_paciente.lower():
                    print(f'Índice: {i}| {valor} |')
                    esc = int(input('Qual consulta deseja pagar?: '))
                    consultas[esc].pagar()
                    print('Consulta paga!')
        if rsp == 3:
            nome_medico = input('Insira o nome do médico:')
            for i,valor in enumerate(consultas):
               if valor._ConsultaMedica__medico.nome_medico.lower() == nome_medico.lower():
                    print(f'Índice: {i}| {valor} |')
                    esc = int(input('Qual consulta deseja pagar?: '))
                    consultas[esc].pagar()
                    print('Consulta paga!')
    elif op==5:
        print('''
        Como deseja buscar as consultas:
         1 - Data
         2 - Nome do paciente
         3 - Nome do médico ''')
        rsp = int(input())
        if rsp == 1: 
            data = input("Insira a data da consulta (no formato dd/mm/aaaa): ")
            for i,valor in enumerate(consultas):
               if valor._ConsultaMedica__data.strftime('%d/%m/%Y') == data:
                    print(f'Índice: {i}| {valor} |')
                    esc = int(input('Qual consulta deseja cancelar?: '))
                    del consultas[esc]
                    print('Consulta cancelada!')
        if rsp == 2:
            nome_paciente = input("Insira o nome do paciente: ")
            for i,valor in enumerate(consultas):
               if valor._ConsultaMedica__paciente.nome_paciente.lower() == nome_paciente.lower():
                    print(f'Índice: {i}| {valor} |')
                    esc = int(input('Qual consulta deseja cancelar?: '))
                    del consultas[esc]
                    print('Consulta cancelada!')
        if rsp == 3:
            nome_medico = input('Insira o nome do médico:')
            for i,valor in enumerate(consultas):
               if valor._ConsultaMedica__medico.nome_medico.lower() == nome_medico.lower():
                    print(f'Índice: {i}| {valor} |')
                    esc = int(input('Qual consulta deseja cancelar?: '))
                    del consultas[esc]
                    print('Consulta cancelada!')

    elif op==6:
        print('''
        Como deseja buscar as consultas:
         1 - Data
         2 - Nome do paciente
         3 - Nome do médico ''')
        rsp = int(input())
        if rsp == 1: 
            data = input("Insira a data da consulta (no formato dd/mm/aaaa): ")
            for i,valor in enumerate(consultas):
               if valor._ConsultaMedica__data.strftime('%d/%m/%Y') == data:
                    print(f'Índice: {i}| {valor} |')
                    esc = int(input('Qual consulta deseja remarcar?: '))
                    consultas[esc].remarcar()
                    print('Consulta remarcada!')
        if rsp == 2:
            nome_paciente = input("Insira o nome do paciente: ")
            for i,valor in enumerate(consultas):
               if valor._ConsultaMedica__paciente.nome_paciente.lower() == nome_paciente.lower():
                    print(f'Índice: {i}| {valor} |')
                    esc = int(input('Qual consulta deseja remarcar?: '))
                    consultas[esc].remarcar()
                    print('Consulta remarcada!')

        if rsp == 3:
            nome_medico = input('Insira o nome do médico:')
            for i,valor in enumerate(consultas):
               if valor._ConsultaMedica__medico.nome_medico.lower() == nome_medico.lower():
                    print(f'Índice: {i}| {valor} |')
                    esc = int(input('Qual consulta deseja remarcar?: '))
                    consultas[esc].remarcar()
                    print('Consulta remarcada!')
    
    elif op == 7:
        print('Obrigado pela colaboração')
        break