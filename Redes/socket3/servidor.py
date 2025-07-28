import socket
from datetime import datetime


host = 'localhost'
puerto = 8000

servidorSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidorSocket.bind((host, puerto))
servidorSocket.listen(5)

while True:
    print("Esperando conexiones...")
    conexionSock, direccion = servidorSocket.accept()
    print("Conectado con cliente", direccion)

    while True:
        recibido = conexionSock.recv(1024).decode()
        print(f"Cliente dice: {recibido}")

        """ if recibido == 'hora':
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            mensaje=(f"Hora actual {current_time}")
            conexionSock.send(mensaje.encode())
        """

        if recibido == 'chau':
            print("Cerrando conexion...")
            mensaje="Desconectando..."
            conexionSock.send(mensaje.encode())
            break
            
        conexionSock.send(input().encode())
    
    print("El cliente se desconecto", direccion)
    conexionSock.close()