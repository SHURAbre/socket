import socket

IP_SERVIDOR = "127.0.0.1"
PORTA = 10402

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mensagem = input("Digite uma mensagem para enviar ao servidor UDP: ")
cliente.sendto(mensagem.encode(), (IP_SERVIDOR, PORTA))

dados, servidor = cliente.recvfrom(1024)
print("Resposta do servidor:", dados.decode())

cliente.close()
