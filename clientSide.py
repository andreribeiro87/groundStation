# server.py
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("localhost", 12345)  # Escolha a porta desejada
server_socket.bind(server_address)
server_socket.listen(1)

print(f"Aguardando conexão em {server_address}")

connection, client_address = server_socket.accept()

try:
    while True:
        data = connection.recv(1024)
        if not data:
            break
        print(data.decode("utf-8"))
finally:
    connection.close()
