import socket
import sys
from _thread import start_new_thread

# Função para lidar com cada conexão (cliente)
def clientthread(conn):
    while True:
        try:
            # Recebe os dados da requisição do cliente
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break
            
            # Processa a requisição HTTP
            if data.startswith("GET"):
                # Cria uma resposta HTTP simples
                response = "HTTP/1.1 200 OK\r\n"
                response += "Content-Type: text/html\r\n\r\n"
                response += "<html><body><h1>Hello, World!</h1></body></html>"
                conn.sendall(response.encode('utf-8'))
            else:
                # Resposta padrão para métodos não suportados
                response = "HTTP/1.1 405 Method Not Allowed\r\n\r\n"
                conn.sendall(response.encode('utf-8'))
        except Exception as e:
            print(f"Erro ao processar a requisição: {e}")
            break

    conn.close()

# Configuração do servidor
host = ''
port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Garante que o socket pode ser reutilizado após interrupção
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    s.bind((host, port))
    print(f"Servidor iniciado na porta {port}")
except socket.error as msg:
    print(f"Erro ao iniciar o servidor: {msg}")
    sys.exit()

# O servidor escuta conexões
s.listen(5)

# Continua aceitando conexões
while True:
    conn, addr = s.accept()
    print(f"Conectado com {addr[0]}:{addr[1]}")

    # Cria nova thread para cada cliente
    start_new_thread(clientthread, (conn,))

s.close()
