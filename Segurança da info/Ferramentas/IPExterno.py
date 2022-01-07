import re, json
from urllib.requiest import urlopen

url = 'https: //ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']

print("Detalhes do IP Externo\n: ")

print("IP: {ip}\n, Região: {regiao}\n, Pais: {pais}\n, Cidade: {cid}\n, Org: {org}")