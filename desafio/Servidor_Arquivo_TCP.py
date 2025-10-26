import socket
import os

TCP_IP = '0.0.0.0'
TCP_PORTA = 10402
BUFFER = 1024

os.makedirs("arquivos_recebidos", exist_ok=True)

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((TCP_IP, TCP_PORTA))
servidor.listen(1)

print(f"Servidor aguardando conexão na porta {TCP_PORTA}...")

conn, addr = servidor.accept()
print(f"Conectado com: {addr}")

nome_arquivo = conn.recv(BUFFER).decode()
print(f"Recebendo arquivo: {nome_arquivo}")

with open(f"arquivos_recebidos/{nome_arquivo}", "wb") as f:
    while True:
        dados = conn.recv(BUFFER)
        if not dados:
            break
        f.write(dados)

print("Arquivo recebido com sucesso!")
conn.close()