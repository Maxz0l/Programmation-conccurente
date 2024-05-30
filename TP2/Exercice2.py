import os,sys

for i in range(3):
    retour = os.fork()
    pid = os.getpid()
    ppid = os.getppid()
    print("i:", i , "je suis le processus:", pid , "mon père est:", ppid , "Retour:", retour)