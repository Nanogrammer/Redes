import socket

host = 'localhost'
puerto = 8000

clienteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clienteSocket.connect((host, puerto))

while True:
    mensaje = input()
    if mensaje != 'chau':
        clienteSocket.send(mensaje.encode())
        respuesta = clienteSocket.recv(1024).decode()
        print(f"Servidor dice: {respuesta}")

    else:
        clienteSocket.send(mensaje.encode())
        clienteSocket.close()