import socket
host = '127.0.0.1'
port = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host, port)

print("Conectando em %s porta %s" % server_address)

sock.connect(server_address)

message = "Olá, mundo"
sock.sendall(message.encode())
data = sock.recv(1024)
print("Recebidos: %s" %data.decode())

print("Fechando conexão com o servidor")
sock.close()
