import socket
# socket.AF_INET -> protocolo IP e 
# socket.SOCK_DGRAM -> tipo de protocolo UDP
s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket Criado com Sucesso!!")

host = 'localhost'
port=5432

s.bind((host,port)) # faz a ligação entre cliente servidor e a porta
mensagem = 'Servidor: Olá Cliente!!'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print("Servidor enviando mensagem...")
        s.sendto(dados + (mensagem.encode()), end)
        s.close()
    