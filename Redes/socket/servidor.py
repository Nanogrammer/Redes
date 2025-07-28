from socket import socket, AF_INET, SOCK_STREAM
from datetime import datetime

class Servidor:
    def crearservidor(self):
        servidor = socket(AF_INET, SOCK_STREAM)
        servidor.bind(("192.168.100.9", 12345))
        servidor.listen(5)
        maximo = 5
        hostsConect = 0
        horaactual = datetime.now()
        print("Servidor escuchando con un máximo de 5 hosts\n")

        while hostsConect < maximo:  # Mantiene el servidor activo y escuchando
            conexion, direccion = servidor.accept()
            print(f"Se estableció una conexión desde {direccion} a las {horaactual} \n")
            hostsConect+=1
            datos = conexion.recv(1024).decode("utf-8")
            print(f"Datos recibidos: {datos if datos else 'no se recibieron datos'}")
            
            if datos == "chau":
                
                hostsConect-=1
                op = input("¿Cerrar servidor? (si/no): ").strip().lower()
                if op == "si":

                    conexion.send("chau".encode("utf-8"))
                    conexion.close()
                    print("conexion cerrada")
                    servidor.close()
                    print(f"Servidor cerrado. a las {horaactual}")
                    break  # Sale del bucle para cerrar el servidor

            else:
                respuesta = input("ingrese un mensaje respuesta para el cliente\n")
                conexion.send(respuesta.encode("utf-8"))
                hostsConect = hostsConect+1-1

                