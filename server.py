import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sockfd.bind(("127.0.0.1", 8886))

sockfd.listen(3)

connfd, addr = sockfd.accept()

f = open("time.png", "wb")
while True:
    data = connfd.recv(1024)
    if not data:
        break
    f.write(data)

f.close()
connfd.close()
sockfd.close()
