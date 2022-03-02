import time

f = open("log.txt", "a+")

f.seek(0, 0)
n = 0

for line in f:
    n += 1

while True:
    n += 1
    time.sleep(2)
    s = ("%d ,%s\n" % (n, time.ctime()))
    f.write(s)
    f.flush()
