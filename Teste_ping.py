import os # importa o módulo os que integra os programas e recursos do S.O.
from datetime import datetime

def cabecalho(arquivo):
    arquivo.write("*****Teste de Ping de Servidores Linux*****\n")
    #print("Data e Hora do teste: ",datetime.now())
    arquivo.write("#"*60)
    arquivo.write("\n\nMáquinas - Status\n")

def rodape(arquivo,maquinas_ligadas,maquinas_desligadas):
    arquivo.write("\n\nTotal de máquinas ligadas = ",maquinas_ligadas)
    arquivo.write("Total de máquinas desligadas = ",maquinas_desligadas)
    
def teste_ping(lista):
    maquinas_ligadas=0
    maquinas_desligadas=0
    saida=[]
    for i in range(0,len(lista)):
        if os.system('ping -n 4 {}'.format(lista[i])) == 0:
            maquinas_ligadas+=1
            saida.append("{} - ligada".format(lista[i]))
        else:
            maquinas_desligadas+=1
            saida.append("{} - Desligada".format(lista[i]))
    
    
    saida.sort()
    with open("Output\Situacao_Maquinas.txt", 'w') as arquivo:
        cabecalho(arquivo)
        for i in range(0,len(saida)):
            arquivo.write(str(saida[i]))
            arquivo.write('\n')
        rodape(arquivo,maquinas_ligadas,maquinas_desligadas)
        arquivo.write("Tempo de execução:","%2.f" % (fim-inicio),"segundos")
