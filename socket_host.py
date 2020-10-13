import socket


def resolve(host):
    return socket.gethostbyname(host)


print(resolve)
print(resolve('google.com'))
