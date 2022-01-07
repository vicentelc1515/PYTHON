import ipaddress

ip = '192.168.0.1'
end = ipaddress.ip_address(ip)
print(end + 256)

ips = ('192.168.0.1','192.168.0.1/24','192.168.0.1/4','192.168.0.1/0','192.168.0.1/32')
ip = ips[0]
rede = ipaddress.ip_network(ip[, strict=False)
print(rede)
print("__"*30)
for i in rede:
    print(rede)