import socket

IP = "0.0.0.0"
PORTA = 10402
BUFFER = 1024

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind((IP, PORTA))

print(f"Servidor UDP ativo em {IP}:{PORTA}")

while True:
    dados, endereco = servidor.recvfrom(BUFFER)
    print(f"Mensagem recebida de {endereco}: {dados.decode()}")
    resposta = dados.decode().upper()
    servidor.sendto(resposta.encode(), endereco)