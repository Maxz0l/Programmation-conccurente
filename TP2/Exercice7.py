import os,sys

N = 3
for i in range(N) :
    os.fork()
print("Bonjour")
sys.exit(0)

# Programme a finir 