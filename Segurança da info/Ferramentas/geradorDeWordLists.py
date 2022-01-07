#itertools gera uma lista com varias palavras sem repeticao.
import itertools

#resultado = itertools.permutations('abcdf',3)
#string = input("String a ser permutada: ")
resultado = itertools.permutations(string,len(string))
for i in resultado:
    print(''.join(i))