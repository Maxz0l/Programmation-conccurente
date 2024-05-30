import os,sys

# Ecrire un programme permettant d’exécuter deux processus, chacun réalisant son propre traitement. Tester la
# fonction os.execlp() en écrivant un programme qui lance un autre programme.

def processus_1(): # Définition du process 1
    print("Processus 1, ID:", os.getpid())
    os.execlp("python3","python3","exo1bis.py")

def processus_2(): # Définition du process 2
    print("Processus 2, ID:", os.getpid())
    os.execlp("python3","python3","exo1bisbis.py")

if __name__ == "__main__": # Programme principale
    pid1 = os.fork()
    if pid1 == 0:
        processus_1()
    else:
        processus_2()

