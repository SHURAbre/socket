import socket

IP_SERVIDOR = "127.0.0.1"  # localhost
PORTA = 10402

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((IP_SERVIDOR, PORTA))

print("Conectado ao servidor. Digite mensagens ou 'QUIT' para encerrar.\n")

while True:
    msg = input("Você: ")
    cliente.send(msg.encode())

    if msg.strip().upper() == "QUIT":
        print("Encerrando conexão...")
        break

    resposta = cliente.recv(1024).decode()
    print("Servidor:", resposta)

cliente.close()