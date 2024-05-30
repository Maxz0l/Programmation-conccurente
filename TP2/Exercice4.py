import os,sys
n=0
for i in range(1,5) :
    fils_pid = os.fork() #1
    if (fils_pid > 0) : #2
        #os.wait() #3
        n = i*2
        break;
print("n = ", n) #4
sys.exit(0)

# Après la ligne 2 on se retrouve dans le bloc d'exécution du père
# La valeur qui est nulle pour le PID correspond au fils
# Lorsque l'on est dans ce cas le systeme est en effet deterministe car le processus suivant doit attendre que le précédent s'exécute pour pouvoir se lancer
# Au contraire lorsque l'on enlève la ligne os.wait() le programme n'est plus deterministe (même si on voit que la même chose est affiché à chaque fois) car le processus se font en m^me temps et donc potentiellent si l'un est retardé alors il pourra passer derriere un autre fork et donc mettre le déssordre dans la séquence
# On a donc les affichages suivants possibles : [0,4,2,8,6],[8,6,4,2,0] ainsi de suite ...
# La ligne os.fork() à peu de chance d'échouer car il faudrait qu'il n'y est plus aucune place pour kabcer le programme et cela veut donc dire que l'on doit attendre la fin d'un programme avant le lancement d'un nouveau. Dans ce cas la machine est probablement morte (un virus qui lance des programmes sans qu'on le demande ...)
