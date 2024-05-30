import os,sys,signal,time

def fin(sig, frame) :
    print( "SIGINT pour le processus : %d" %os.getpid() )
    sys.exit(1)

signal.signal(signal.SIGINT , fin)

N = 1
pid = os.fork()
if pid != 0 :
    while N>0:
        N = 1 + N
        time.sleep(1)
        print(N)
sys.exit(0)
