import random, os, sys, time
import multiprocessing as mp

N = random.randint(2,5)
print(N)

def producteur1():
    for i in range(N):
        message = i
        Q1.put(message)
        print(f"Producteur 1 : {message}")

def producteur2():
    for i in range(N):
        message = i
        Q2.put(message)
        print(f"Producteur 2 : {message}")

def consommateur1():
    for i in range(N):
        message = Q1.get() 
        print(f"Consommateur 1 : {message}")
        time.sleep(1)
        sem2.release()
        sem1.acquire()


def consommateur2():
    for i in range(N):
        message = Q2.get()
        print(f"Consommateur 2 : {message}")
        time.sleep(2)
        sem1.release()
        sem2.acquire()

sem1 = mp.Semaphore(0)
sem2 = mp.Semaphore(0)
Q1 = mp.Queue()
Q2 = mp.Queue()

p1 = mp.Process(target=producteur1)
p2 = mp.Process(target=producteur2)
c1 = mp.Process(target=consommateur1)
c2 = mp.Process(target=consommateur2)

p1.start()
p2.start()
c1.start()
c2.start()

p1.join()
p2.join()
c1.join()
c2.join()