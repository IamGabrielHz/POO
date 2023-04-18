import datetime
import random
import calendar 


class consulta:
    def __init__(self,paciente: str,medico: str,data: str,valor: float,paga: bool):
        self.__paciente = paciente
        self.__medico = medico
        self.__data = data
        self.__valor = valor
        self.__paga = paga
        

    def __str__(self):
        return f'Paciente : {self.__paciente}\t Médico = {self.__medico}\t Data = {self.__data}\t Valor = {self.__valor}\t Situação = {self.__paga}'
    
    @property
    def paciente(self):
        return self.__paciente
    

    @paciente.setter
    def paciente(self, paciente):
        self.__paciente = paciente

    
    @property
    def medico(self):
        return self.__medico
    

    @medico.setter
    def medico(self,medico):
        print('Sem permissão')


def relatorio_medicos(Consultas):
    agora = datetime.date.today()
    Consultas_mes_atual = [consulta for consulta in Consultas if consulta.__data.month == agora.month]
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