import ctypes
pasta = input("Digite o caminha da pasta a ser ocultada: ex: (C:/pasta):  ")
atributo_ocultar= 0x02
retorno = ctypes.windll.kernel32.setFileAttributesW('ocultar.txt',atributo_ocultar)
retorno = ctypes.windll.kernel32.setFileAttributesW(pasta,atributo_ocultar)