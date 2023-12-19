from ipaddress import *

for a in range(256):
    try:
        net = ip_network(f'243.46.4.198/255.255.{a}.0', 0)

        if all((bin(int(ip))[2:])[:16].count('0') <= (bin(int(ip))[2:])[16:].count('0') for ip in net):
            print(a)
            break
    except:
        pass
