import os, sys
os.fork()
if (os.fork()) :
    os.fork()
print("3ETI 2024")
sys.exit(0)

# C'est clair quand o le fait avec l'arbre 
# fork() un pere et f1
# fork() un pere f3 un pere qui est f1 et f2
# Si on est un pere (donc pere et f1) alors on cré le f4 et le f5