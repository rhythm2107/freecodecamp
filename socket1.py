import socket # Importing Socket Module

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Setting up the socket for connection. AF_INET = ipv4 & SOCK_STREAM = TCP
mysock.connect(('data.pr4e.org', 80)) # Tuples with link and port to connect to
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
