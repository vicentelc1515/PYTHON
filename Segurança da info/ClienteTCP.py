# TCP protocolo de controle e transmissão, protocolo de comunicação, que dão suporte a rede global
#verificando se os dados são enviados na sequencia correta e sem erros
#UDP protocolo de datagrama dentro do pacote TCP, só verifica se o destino está recebendo os dados. 
#
#

import socket #relacionamento da placa de rede com o S.O.
import sys # fornece acesso a algumas variáveis e funções que tem interação com o python.


def principal():
    try:
        s=socket.socket(socket.AF.INET, socket.SOCK.STREAM, 0)
    except socket.error as e:
        print("A conexção falhou\n")
        print("Erro: {}".format(e))
        sys.exit()
        
    print("Socket criado com sucesso!!")
    
if __name__ == '__main__':
    HostAlvo= input("Digite o Host ou Ip a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ") 
    
    try:
    s.conect((HostAlvo, int(PortaAlvo)))
    print("Cliente TCP conectado com Sucesso no Host: ", + HostAlvo + "e na Porta: "+ PortaAlvo)
    s.shutdown(2)
    except secket.error as e:
    print("Não foi possivel conectar no Host: " + HostAlvo + "-Porta: " + PortaAlvo)
    print("Erro: {}".format(e))
    sys.exit()