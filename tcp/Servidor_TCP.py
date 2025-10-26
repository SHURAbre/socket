import socket

TCP_IP = '0.0.0.0'  
TCP_PORTA = 10402 
TAMANHO_BUFFER = 1024

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((TCP_IP, TCP_PORTA))
servidor.listen(1)

print(f"Servidor disponível na porta {TCP_PORTA} e escutando...")

conn, addr = servidor.accept()
print(f"Conexão estabelecida com {addr}")

while True:
    dados = conn.recv(TAMANHO_BUFFER)
    if not dados:
        break
    print("Mensagem recebida:", dados.decode())
    conn.sendall(dados.decode().upper().encode())

conn.close()