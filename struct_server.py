from socket import *
from struct import *

s = socket(AF_INET, SOCK_DGRAM)
st = Struct("i32sif")

f = open("student.txt", "a")
s.bind(("127.0.0.1", 8001))
while True:
    data,addr = s.recvfrom(2048)
    data = st.unpack(data)
    info = "%d %-10s %d %.1f" % (data[0], data[1].decode(), data[2], data[3])
    f.write(info)
    f.flush()
