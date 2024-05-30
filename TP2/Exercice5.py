import sys,os
import time

N = int(sys.argv[1])

for i in range (N):
    pid_fils = os.fork()
    if pid_fils == 0:
        pid = os.getpid()
        ppid = os.getppid()
        print("pid du fils:", pid, "pid du père:", ppid)
        time.sleep(2*i)
        sys.exit(i)
    
for i in range(N):
    pid, status = os.wait()
    print("Pid du fils qui réveille:", pid,"Il renvoie le status", os.WEXITSTATUS(status))
        