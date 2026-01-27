import socket

ip = input('Ingrese la direccion IP a escanear: ')

for puerto in range(1,65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc