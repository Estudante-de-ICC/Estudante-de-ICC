import _socket
import sys

host = ''
port = 8888

s = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
print("Socket criado")

try:
    s.bind((host, port))
except _socket.error as msg: 
    print("bind falhou. código de erro:" + str(msg[0]) + "Mensagem: " + msg[1])
    sys.exit()

print("Socket encontrado")

s.listen(10)
print("Socket escutando")

while 1: 
    conn, addr = s._accept()
    print("Conectado com" +  addr[0] + ":" + str(addr[1]))

sys.close()