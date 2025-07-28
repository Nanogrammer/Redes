from socket import *


host = "192.168.100.9"
puerto = 13000

# def crearServerTCP():
#     server = socket(AF_INET,SOCK_STREAM)
    
#     server.bind((host,puerto))## enlace del server
#     server.listen(5) ## server escuchando
#     print("servidor escuchando") 
    
#     conexion, direccion = server.accept() #acepta solicitud de conexion
#     print(f"conexion establecida con {conexion} atravez del puerto {direccion}")
#     peticion = conexion.recv(1024).decode() #guarda el mensaje recibido y decodifica
        
#     while peticion != "chau": #si la peticion es chau termina
#         conexion.send(input("ingrese un mensaje a enviar al cliente").encode())#sino envia una entrada
#         conexion.close()
#         conexion, direccion = server.accept() #acepta solicitud de conexion
#         print(f"conexion establecida con {conexion} atravez del puerto {direccion}")

        
        
#     print("desconectando")
#     conexion.send("desconectando".encode()) #enviia desconectando
#     conexion.close()
#     print("el cliente se desconectó", direccion)    
    
    

def crearServerUDP():
    Rmensaje =""
    ipHost = "192.168.100.9"
    serverPort = 13000
    server = socket(AF_INET,SOCK_DGRAM)
    server.bind((ipHost,serverPort))
    print("el servidor esta listo para recibir\n")
    while Rmensaje!="chau":
        mensaje, direccion = server.recvfrom(2048)
        Rmensaje = mensaje.decode()
        print(f"Recibido del cliente {direccion}:{Rmensaje} \t")

        
        server.sendto(input("ingrese respuesta\n").encode(),direccion)
        
    msj = "adioooz"
    server.sendto(msj.encode(),direccion)
    server.close()

            

            