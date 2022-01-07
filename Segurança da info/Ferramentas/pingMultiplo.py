import os
import time


with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    
    for ip in dump:
        print('Verificando IP: ',ip)
        print("-"*60)
        print('ping -n 2{}'.format(ip))
        print("-"*60)
        time.sleep(5)

