from socket import *


def find_word(word):
    f = open("dict.txt")
    for line in f:
        data01 = line.split(" ")[0]
        if data01 > word:
            f.close()
            return "沒有此單字"
        elif word == data01:
            f.close()
            return line
    else:
        f.close()
        return "沒有此單字"


sockfd = socket(AF_INET, SOCK_DGRAM)

sockfd.bind(("127.0.0.1", 8888))

while True:
    try:
        data, addr = sockfd.recvfrom(1024)
    except KeyboardInterrupt:
        print("exit server")
        break
    if not data:
        break
    result = find_word(data.decode())
    sockfd.sendto(result.encode(), addr)

sockfd.close()
