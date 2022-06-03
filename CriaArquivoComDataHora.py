## Criando arquivos com data e hora no nome!!
import re
from datetime import datetime
  
# pegando a data e a hora
datahora = datetime.now()
  
# convertendo o valor para string
str_datahora = str(datahora)

#Retirando o espaço e trocando por _
str_datahora = re.sub(' ', '_', str_datahora)
str_datahora = re.sub(':', '', str_datahora)

# Criando um arquivo com data/hora no nome
file_name = "relatorio"+str_datahora[0:17]+".txt"

file = open(file_name, 'w')
## Aqui podem ser escritos os dados do arquivo!
file.close()

# A saída do arquivo é no formato "relatorio2022-06-03_121604", que é, 
# nome do arquivo+ano-mes-dia_horasMinutosSegundos+extensão
# também pode ser alterado para gerar um csv, basta alterar a extensão para o mesmo
# E ajustar os separadores por virgula ou ponto e virgula ou outro delimitador

# Criando uma função para o caso

def arquivoComDataHora(nome,extensao):
    datahora = datetime.now()
    str_datahora = str(datahora)
    str_datahora = re.sub(' ', '_', str_datahora)
    str_datahora = re.sub(':', '', str_datahora)
    file_name = nome+str_datahora[0:17]+extensao
    return file_name


file = open(arquivoComDataHora('bla', '.csv'), 'w')
file.close()