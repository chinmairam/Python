import socket
import os

def listen(self):
    x = socket(AF_INET6, SOCK_STREAM)
    x.bind(self.ADDR6, self.PORT)
    x.listen(10)

    while(True):
        interno,client = x.accept()
        pid = os.fork()
        if pid!=0:
            self.servicio()
        else:
            interno.close()

def servicio(self):
    pedido = interno.recv(self.buffer)
    externo = socket(AF_INET6, SOCK_STREAM)
    externo.connect(res[0][4][:2])
    externo
