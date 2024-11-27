import socket

DNS_SERVER_IP = "127.0.0.1"  
DNS_SERVER_PORT = 1234

tabela_dns = [
    ("alice", "192.168.1.2"),
    ("bob", "192.168.1.3"),
    ("charlie", "192.168.1.4"),
    ("Debie", "192.168.1.5"),
    ("Evellyn", "192.168.1.6")
]

def encontra_ip(nome):
    for entrada in tabela_dns:
        if entrada[0] == nome.lower():
            return entrada[1]
    return "Not found"

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((DNS_SERVER_IP, DNS_SERVER_PORT))
    print(f"Servidor DNS rodando em {DNS_SERVER_IP}:{DNS_SERVER_PORT}")
    
    while True:

        data, client_end = server_socket.recvfrom(1024)
        nome = data.decode("utf-8")
        print(f"Consulta recebida: {nome} de {client_end}")
        
        ip = encontra_ip(nome)
        print(f"Respondendo com IP: {ip}")
        
        server_socket.sendto(ip.encode("utf-8"), client_end)

if __name__ == "__main__":
    main()