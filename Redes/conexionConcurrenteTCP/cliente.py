from socket import socket, AF_INET, SOCK_STREAM

class cliente():

    def crea_cliente(self):    
        respuesta=""

        while respuesta!="chau":
            host = socket(AF_INET, SOCK_STREAM)
            host.connect(("192.168.100.9", 12345))
            mensaje = input("ingrese un mensaje desde el cliente al servidor")
            host.send(mensaje.encode("utf-8"))
            respuesta = host.recv(1024).decode("utf-8")
            print(f"Datos recibidos: {respuesta if respuesta else 'no se recibieron datos'} desde '192.168.100.9', 12345")
            if respuesta=="chau":
                host.close()
            

x = cliente()
x.crea_cliente()
