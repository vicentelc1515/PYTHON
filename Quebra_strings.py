## Este código faz uma verificação do status da maquina (ligada ou desligado) com um teste
## de ping
## Ele chama uma função contida em outro arquivo (teste_ping) para realizar o teste e como saída
## ele gera um arquivo txt.


from Teste_ping import teste_ping

lista=[]
lista_nao_padrao=[]
file = open("prd\Servidores PRD.txt","r")
auxiliar= ''
## Aqui ele filtra cada linha para pegar apenas o nome das máquinas,
## Pois tudo após o espaço+traço+espaço não é aceito pelo o teste.
for line in file:
    if 'srv' in line or 'vrt' in line:
        lista.append(line[0:7])
    elif ( '-' in line) and not 'PRD' in line:
        lista_nao_padrao.append(line)

## Aqui trata aquelas máquinas que estão no formato padrão. exemplo: renor e rdsh-dsv-01
for i in range(0,len(lista_nao_padrao)-1):
    for j in range(0,20):
        if lista_nao_padrao[i][j]== ' ' and lista_nao_padrao[i][j+1]== '-':
            auxiliar = auxiliar + str(lista_nao_padrao[i][0:j])
    lista.append(auxiliar)
    auxiliar = ''
# gambiarra
lista.append('renor')

teste_ping(lista)
 
file.close()
