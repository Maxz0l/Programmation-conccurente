import os

pid1 = os.fork()
pid2 = os.fork()
if pid1 == 0 and pid2 == 0:
    for i in range(1,101):
        print(i)
    for j in range (101,201):
        print(j)
