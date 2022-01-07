import hashlib

arquivo1='a.txt'
arquivo2='b.txt'

#criando as hashs
# ripemd160 -> tipo algoritmo de hash
hash1=hashlib.new('ripemd160')

hash1.update(open(arquivo1, 'rb')).read()

hash2=hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb')).read()

## fazendo a comparação entre eles

if hash1.digest():
    print(f'O Arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
    print('Hash a: {}'.format(arquivo1))
    print('Hash b: {}'.format(arquivo2))
else:
    print(f'O Arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')
    print('Hash a: {}'.format(arquivo1))
    print('Hash b: {}'.format(arquivo2))
    