from datetime import date, time, datetime, datedelta 

class Cabecalho:

    def dataHora():
        data_atual = datetime.now()
        print(data_atual)
        print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
        print(data_atual.strftime('%c'))
        print(data_atual.weekday())
        print(data_atual.month())
        tupla= ('segunda','terca','quarta','quinta','sexta','sabado','domingo')
        print(tupla[data_atual.weekday()])
        tupla2=('jan','fev','mar','abr','mai','jun','jul','ago','set,'out','nov','dez')
        print(tupla2[data_atual.month()])
        
        data_string='01/02/2022 12:20:22'
        data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
        print(data_convertida)
        
        nova_data = data_convertida - timedelta(days = 365, hours=2, minutes=15)
        print(nova_data)
    def data():
        data_atual=date.today()
        print(data_atual)
        
    def hora():
        horario = time(hour=10, minute=18, second=30)
        print(horario)
        horario_str= horario.strftime('%H:%M:%S')

if __name__ == '__main__':
    data()
    hora()
    dataHora()
    