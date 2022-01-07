from threading import Thread
import datetime
# realiza operações simultaneamente
def carro(velocidade,piloto):
	trajeto = 0
	while trajeto <=100:
		print('Carro1: ', trajeto)
		trajeto+=velocidade
        time.speep(5)
        print('piloto: {} Km: {} \n'.format(piloto,trajeto))
	
		
t_carro1 = Thread(target = carro1, arg[1,'V'])
t_carro2 = Thread(target = carro2, arg[2,'T'])