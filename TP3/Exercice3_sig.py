import sys,time
import multiprocessing as mp
import os,signal

def fin(sig, frame) :
    global end
    print( "SIGINT pour le processus : %d" %os.getpid() )
    end = True
    return (end)

signal.signal(signal.SIGINT , fin)
end = False
N = 1

pid = os.fork()
if pid != 0 :
    while end == False:
        N = 1 + N
        time.sleep(1)
        print(N)
sys.exit(0)