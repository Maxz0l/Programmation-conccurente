import sys,os
for i in range(4) :
    pid = os.fork()
    if pid != 0 :
        print("Ok")
    print("Bonjour !")
sys.exit(0)

# Ce programme nous montre comment fonctionnne la fonction fork()