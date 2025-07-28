from socket import *


host = "192.168.100.9"
puerto = 12000


def CrearclienteUDP():    
    serverPort = 13000
    cliente = socket(AF_INET,SOCK_DGRAM)
    mensaje = input("ingrese un mensaje en minuscula")

    while mensaje!="chau":    
        cliente.sendto(mensaje.encode(),("192.168.100.9",serverPort))
        Mmensaje, direccionServer = cliente.recvfrom(2048)
        print("Recibido del server:\t" , Mmensaje.decode(), direccionServer)
        mensaje = input("ingrese un mensaje en minuscula")

    cliente.sendto("chau".encode(),("192.168.100.9",serverPort))
    cliente.close()

CrearclienteUDP()


# def crearclienteTCP():

#     cliente = socket(AF_INET,SOCK_STREAM)
#     mensaje = input("ingrese un mensaje en minuscula")
#     if mensaje != "chau":
#         cliente.connect((host,puerto))
#         mensaje = input("ingrese mensaje en minuscula")
#         cliente.send(mensaje.encode())
#         recibido = cliente.recv(1024)
#         print(f"para el servidor: {recibido.decode()}")
#     else:
#         cliente.send(mensaje.encode())    
#         cliente.close()
