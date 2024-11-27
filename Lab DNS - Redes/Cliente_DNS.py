import socket

DNS_SERVER_IP = "127.0.0.1" 
DNS_SERVER_PORT = 1234

DEST_PORT = 60500

def main():
    # Criando o socket para se comunicar com o servidor DNS
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        #Solicitar o nome ao usuário
        nome = input("Digite o nome para consultar\n(ou 'sair' para encerrar): ")
        if nome.lower() == "sair":
            break
        
        #Solicitação ao servidor DNS
        client_socket.sendto(nome.encode("utf-8"), (DNS_SERVER_IP, DNS_SERVER_PORT))
        
        #Resposta do servidor DNS
        ip, _ = client_socket.recvfrom(1024)
        ip = ip.decode("utf-8")
        
        if ip == "Not found":
            print("Nome não encontrado na tabela DNS. Tente novamente...")
        else:
            print(f"IP encontrado: {ip}")
            
            #Envia mensagem
            message = input("Digite uma mensagem para enviar ao destino: ")
            dest_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            dest_socket.sendto(message.encode("utf-8"), (ip, DEST_PORT))
            print(f"Mensagem enviada para {ip}:{DEST_PORT}")
            dest_socket.close()
    
    client_socket.close()

if __name__ == "__main__":
    main()