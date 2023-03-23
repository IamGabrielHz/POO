import datetime
import random
import calendar 


class consulta:
    paciente = None
    medico = None
    data = None
    valor = None
    paga = None


    def __init__(self,paciente,medico,data,valor,paga):
        self.paciente = paciente
        self.medico = medico
        self.data = data
        self.valor = valor
        self.paga = paga


    def __str__(self):
        return f'Paciente : {self.paciente}\t Médico = {self.medico}\t Data = {self.data}\t Valor = {self.valor}\t Situação = {self.paga}'


def aleatory_date():
    hoje = datetime.date.today()
    ultimo_dia_mes = calendar.monthrange(hoje.year, hoje.month)[1]
    data_aleatoria = hoje + datetime.timedelta(days=random.randint(0, ultimo_dia_mes))
    return data_aleatoria


def plusmonth(agendamento):
    if agendamento.month == 12:
        agendamento = agendamento.replace(year=agendamento.year+1, month=1)
    else:
        agendamento = agendamento.replace(month=agendamento.month+1)
    return agendamento


def relatorio_medicos(Consultas):
    agora = datetime.date.today()
    Consultas_mes_atual = [consulta for consulta in Consultas if consulta.data.month == agora.month]
    quantidade_por_medico = {}
    for objeto in Consultas_mes_atual:
        medico = objeto.medico
        if medico in quantidade_por_medico:
            quantidade_por_medico[medico] += 1
        else:
            quantidade_por_medico[medico] = 1
    if not quantidade_por_medico:
        print("Nenhum médico teve consultas marcadas neste mês.")
    else:
        for medico, quantidade in quantidade_por_medico.items():
            print("Médico:", medico, "- Quantidade:", quantidade)


def relatorio_faturamento(Consultas):
    valor_total = 0
    for consulta in Consultas:
        valor_total += consulta.valor
    return valor_total


def menu(lista_medicos,Consultas):
    while True:
            command = input('1 - Nova consulta (agendamento)\n2- Pagar Consulta\n3- Cancelar consulta\n4- Agendar retorno\n5- Relatório de Consultas realizadas no mes por médico\n6- Relatório de relatorio_faturamento da Clinica por mes\n0- Finalizar\n')
            if command == '1':
                agendamento = aleatory_date()
                nova_consulta = consulta(input('Insira seu nome: '),random.choice(lista_medicos),agendamento,300,False)
                Consultas.append(nova_consulta)
                print(f'Essa é a data da sua consulta {agendamento}, deseja pagar?')
            if command == '2': 
                Consultas[-1].paga = True
                print('Paga!')
            if command == '3':
                 del Consultas[-1]
                 print('A última consulta foi cancelada!')
            if command == '4':
                Consultas[-1].data = plusmonth(agendamento)
                print('Sua consulta foi reagendada!')
            if command == '5':
                print(relatorio_medicos(Consultas))
            if command == '6':
                print(relatorio_faturamento(Consultas))
            if command == '0':
                break


def main():
    lista_medicos = ['Carlos', 'Roberto', 'Jose', 'João', 'Guilherme', 'Antonio']    
    Consultas = []
    menu(lista_medicos,Consultas)
    print('Obrigado por colaborar conosco!')


if __name__ == '__main__':
     main()