import os,sys,time
N = sys.argv[1]

def creation_process(N):
    for i in range (2,N+1):
        pid = os.fork()
        if pid == 0:
            print(f"Je suis le processus fils {os.getpid()}, mon père et le processus {os.getppid()}")
            time.sleep(2*i)
        sys.exit(i)

if __name__ == "__main__":
    N=8
    creation_process(N)
    os.wait