import time

Start = int(round(time.time() * 1000))
b = int(0)
for a in range(0, 5000000):
    b = b+a
End = int(round(time.time() * 1000))

print(End-Start)