import socket
import os

TCP_IP = '127.0.0.1'
TCP_PORTA = 10402
BUFFER = 1024

arquivo = input("Digite o nome do arquivo que deseja enviar: ")

if not os.path.exists(arquivo):
    print("Arquivo não encontrado!")
    exit()

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((TCP_IP, TCP_PORTA))

cliente.send(arquivo.encode())

with open(arquivo, "rb") as f:
    for dado in f:
        cliente.send(dado)

print("Arquivo enviado com sucesso!")
cliente.close()