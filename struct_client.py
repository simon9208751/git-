from socket import *
from struct import *

s = socket(AF_INET, SOCK_DGRAM)
st = Struct("i32sif")
ADDR = ("127.0.0.1", 8001)

while True:
    number = int(input("請輸入編號："))
    name = input("請輸入名字：").encode()
    age = int(input("請輸入年齡："))
    score = float(input("請輸入分數："))
    data = st.pack(number, name, age, score)
    s.sendto(data, ADDR)
