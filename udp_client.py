from socket import *

sockfd = socket(AF_INET, SOCK_DGRAM)

ADDR = ("127.0.0.1", 8888)
while True:
    word = input("send a word:")
    if not word:
        break
    sockfd.sendto(word.encode(), ADDR)

    data, addr = sockfd.recvfrom(1024)
    print(data.decode())

sockfd.close()
