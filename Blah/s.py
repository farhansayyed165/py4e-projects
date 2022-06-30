import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('https://www.pr4e.com', 443))
cmd = 'GET https://www.pr4e.com/code3/mbox.txt HTTP/1.0\r\n\r\n'.encode()

mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode(),end='')
mysock.close()
