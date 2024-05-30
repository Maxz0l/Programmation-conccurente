import multiprocessing as mp
import sys,os,time

sem = mp.Semaphore(0)

def processus1():
    print("Tache 1 terminée")
    time.sleep(2)
    sem.release()

def processus2():
    sem.acquire()
    print("Tache 2 terminée")

p1 = mp.Process(target=processus1)
p2 = mp.Process(target=processus2)
p1.start()
p2.start()
p1.join()
p2.join()



