# @Date : 6/6/2024
# @Author : Enzo Lorandi
# @Description : Il faut resoudre le probleme qui empeche la boucle de se finir

import random,sys,os
import multiprocessing as mp
import time
import numpy as np
import matplotlib.pyplot as plt

def distance(x,y):
    return np.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

def moyenne(L):
    if len(L) == 0:
        return (0, 0)  # or some other default value
    else:
        return (sum(x[0] for x in L) / len(L), sum(x[1] for x in L) / len(L))

def K_means(k):
    # Création de 100 coordonnées aléatoires
    echantillons = [(100*random.random(),100*random.random()) for i in range(100)]
    epsilon = 0.05  # variable epsilon for stopping condition
    
    # Création de k centres aléatoires
    centres = [(100*random.random(),100*random.random()) for i in range (k)]
        
    # Initialisation variable de fin du programme
    fini = False
    count = 0  # Initialize compteur
    
    # Boucle pour affecter les points à un centre
    while not fini:
        groupes = []
        for i in range(k)  :
            groupes.append([])
        # groupes = [[] for i in range(k)]
        for echantillon in echantillons:
            distances = [distance(echantillon, centre) for centre in centres] 
            groupe_indice = np.argmin(np.array(distances)) 
            groupes[groupe_indice].append(echantillon) 
            # Mise à jour des centres
            new_centres = [moyenne(groupe) for groupe in groupes]
            # On regarde si les centres changent
            if all(distance(new_centre, centre) < epsilon for new_centre, centre in zip(new_centres, centres)):
                fini = True
            else:
                centres = new_centres
                print(centres)
        count += 1
        if count >= 500:  # Stop après 100 iterations
            print('******')
            break
        
    
    # plot des figures
    for i in range(k):
        plt.scatter([x[0] for x in groupes[i]], [x[1] for x in groupes[i]], label=f"Groupe {i+1}")
        plt.scatter([centres[i][0]], [centres[i][1]], label=f"Centre {i+1}", marker='x')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    k = 4
    K_means(k)