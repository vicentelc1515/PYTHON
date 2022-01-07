#ICMP é um protocolo integrante do protocolo IP
#Ping usa o ICMP
#O que é Ping?? é uma ferramenta que testa a conectividade entre máquinas.
#envia pacotes para ver se está disponivel, ping faz isso.
#Digitar no CMD ping -n 6 www.google.com, envia 6 pacotes ao google para testar a conectividade. 
# 
#
#

import os # importa o módulo os que integra os programas e recursos do S.O.

print("#"*60)
ip_ou_host = input("Digite o IP ou Host a ser verificado")
print("#"*60)
os.system('ping -n 6 {}'.format(ip_ou_host))

