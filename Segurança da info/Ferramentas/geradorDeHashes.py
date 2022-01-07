#criptografa o conteúdo para ser armazenado de forma segura, muito usada em senhas e logins!!

import hashlib

string = input("Digite o texto a ser gerado a hash: ")

#resultado = hashlib.md5(b'Python Security')
def menu(a):
    menu = int(input('''### MENU - ESCOLHA O TIPO DE HASH  ###
1) MD5
2) SHA1
3) SHA256
4) SHA512
Digite o numero do hash a ser gerado: '''))

if __name__ == '__main__':
    if menu ==1:
        resultado = hashlib.md5(string.encode('utf-8'))
        print('A hash da string é: ', resultado.hexdigest())

    elif menu ==2:
        resultado = hashlib.SHA1(string.encode('utf-8'))
        print('A hash da string é: ', resultado.hexdigest())

    elif menu ==3:
        resultado = hashlib.SHA256(string.encode('utf-8'))
        print('A hash da string é: ', resultado.hexdigest())

    elif menu ==4:
        resultado = hashlib.SHA512(string.encode('utf-8'))
        print('A hash da string é: ', resultado.hexdigest())
    else:
        print("Opção invalida, tente novamente...")
