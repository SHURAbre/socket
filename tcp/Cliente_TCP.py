import socket

IP_SERVIDOR = "127.0.0.1" 
PORTA = 10402

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((IP_SERVIDOR, PORTA))

mensagem = input("Digite uma mensagem para o servidor: ")
cliente.send(mensagem.encode())

resposta = cliente.recv(1024)
print("Resposta do servidor:", resposta.decode())

cliente.close()
