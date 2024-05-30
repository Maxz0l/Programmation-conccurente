# La commande sort <test.txt> fichier_trie trie e fichier text.txt et créer un nouveu fichier qui est trié.

# On veut faire des scripts réalisant les commandes cat fichier | wc et sort < fichier | grep chaine | tail –n 5 > sortie

import os,sys

commande = input("Quelle commande voulez vous ?")

if commande == 1:
    (dfr,dfw) = os.pipe()
    pid = os.fork()
    if pid !=0:
        os.close(dfr)
        os.dup2(dfw,1)
        os.close(dfw)
        os.execlp("cat","cat","test.txt")
    else:
        os.close(dfw)
        os.dup2(dfr,0)
        os.close(dfr)
        os.execlp("wc","wc")
    sys.exit(0)
