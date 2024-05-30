import os,sys

message = "Je suis Enzo"
message = message.encode() 
(dfr,dfw) = os.pipe()
pid = os.fork()
if pid!=0:
    os.close(dfr)
    n = os.write(dfw,message)
    print("Le processus",os.getpid(),"transmet le message :",message)
    os.close(dfw)
else:
    os.close(dfw)
    message_recu = os.read(dfr,len(message))
    print("Le processus",os.getpid(),"recoit le message :",message_recu)
    os.close(dfr)
sys.exit(0)