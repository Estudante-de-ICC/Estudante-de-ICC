import socket
import time

#Criado um socket UDP
C_Socket = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)

print("Conectado ao servidor na porta 50000")

tempos = []
perdas = 0
pings = 10
for i in range(pings):
    try:
        C_Socket.settimeout(2)
        enviado = time.time()
        C_Socket.sendto(b'ping', ('127.0.0.1', 50000))
        dados, addr = C_Socket.recvfrom(1024)
        recebido = time.time()
        print(f"Recebeu {dados.decode()} from {addr} em {recebido - enviado} segundos")
        tempos.append(recebido - enviado)
    except: 
        print("Request timed out")
tempos.sort()
tam = len(tempos)
somas = 0
for i in range(tam-1):
    somas += tempos[i]

print("Estatísticas: ")
print(f"Enviado: 10, Recebidos: {tam}, Perdidos {10-tam} ({((10-tam)/10)*100 }% de perda)")
print(f"Mínimo = {tempos[0]}ms, Máximo = {tempos[tam-1]}ms, Média = {somas / tam}ms ")

