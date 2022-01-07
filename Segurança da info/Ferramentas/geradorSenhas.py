#md5decrupt.net criptografa senhas, palavras etc!!
import random, string 
tamanho = 16
chars = string.acsii.letters + string.digits + '!@$%&$*().+-*/?^~'
rnd = randon.SystemRandom()
print(''.join(rnd.choice(chars) for i in range(tamanho)))