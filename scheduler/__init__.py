import psutil
import socket
import requests
import time

def get_ipv4_address(interface_name):
    try:
        interfaces = psutil.net_if_addrs()
        if interface_name in interfaces:
            for addr in interfaces[interface_name]:
                if addr.family == socket.AF_INET:
                    return addr.address
    except Exception as e:
        print(f"Erro ao obter o endereço IPv4: {e}")
    return None

online = False

while online == False:
    try:
        requests.get(f'http://127.0.0.1:8000/')
        online = True
    except:
        print('Aguardando 3 segundos...')
        time.sleep(3)
