import os,sys
import time

for i in range(3):
    pid1 = os.fork()
    if pid1 == 0 and i == 0:
        os.execlp("who","who")
    if pid1 == 0 and i == 1:
        os.execlp("/bin/ps","ps")
    if pid1 == 0 and i == 2:
        os.execlp("/bin/ls","ls","-l")

for i in range(3):
    pid1 = os.fork()
    time.sleep(10)
    if pid1 == 0 and i == 0:
        os.execlp("who","who")
    if pid1 == 0 and i == 1:
        os.execlp("/bin/ps","ps")
    if pid1 == 0 and i == 2:
        os.execlp("/bin/ls","ls","-l")
