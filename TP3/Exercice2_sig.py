import os,sys,time,signal

signal.signal(signal.SIGINT , signal.SIG_IGN)

N = 1
pid = os.fork()
if pid != 0 :
    while N>0:
        N = 1 + N
        time.sleep(1)
        print(N)
sys.exit(0)

# On constate que l'intérrpution n'est pas possible 