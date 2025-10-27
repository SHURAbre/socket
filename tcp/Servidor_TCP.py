import socket

IP = "0.0.0.0"
PORTA = 10402
BUFFER = 1024

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((IP, PORTA))
servidor.listen(1)

print(f"Servidor TCP ativo na porta {PORTA}. Aguardando conexão...")

conn, addr = servidor.accept()
print(f"Conectado com {addr}\nDigite 'QUIT' para encerrar.\n")

while True:
    dados = conn.recv(BUFFER)
    if not dados:
        break

    msg = dados.decode().strip()
    print("Cliente:", msg)

    if msg.upper() == "QUIT":
        print("Cliente encerrou a conversa.")
        conn.send("QUIT".encode())
        break

    resposta = input("Servidor: ")
    conn.send(resposta.encode())

    if resposta.strip().upper() == "QUIT":
        print("Encerrando servidor...")
        break

conn.close()
