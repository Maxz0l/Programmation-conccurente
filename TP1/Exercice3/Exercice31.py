import os,sys
N = 10
v=1
while os.fork()==0 and v<=N :
    v+= 1
print(v)
sys.exit(0)

# Ce programme stop lorsque l'on dépasse la valeur N limite et on exit le programme à ce moment