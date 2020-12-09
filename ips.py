import ipaddress

ip = '10.0.0.0/24'

endereco = ipaddress.ip_network(ip)

for ip in endereco:
    print(ip)