# @Date : 6/6/24
# @Author : LORANDI Enzo
# @Description : Ce code est une modification du code permettant d'obtenir une estimation de pi avec une execution en multi process et une comparaison du temps entre les 2 méthodes

import random, time
import multiprocessing as mp

# calculer le nbr de hits dans un cercle unitaire (utilisé par les différentes méthodes)

def frequence_de_hits_pour_n_essais(nb_iteration):
    count = 0
    for i in range(nb_iteration):
        x = random.random()
        y = random.random()
        # si le point est dans l’unit circle
        if x * x + y * y <= 1: 
            count += 1
    return count

def moyenne(L):
    return sum(L) / len(L)

if __name__ == "__main__" :
    nb_total_iteration = 10000000 # Nombre d’essai pour l’estimation
    
    # Début de l'execution en multi-process
    start_1 = time.time() # On démarre le chrono
    nb_process = 4
    pool = mp.Pool(processes=nb_process)
    nb_iteration_par_process = nb_total_iteration // nb_process
    results = pool.map(frequence_de_hits_pour_n_essais, [nb_iteration_par_process] * nb_process)
    resultat = moyenne(results)
    end_1 = time.time() # On stop le chrono
    time_execution_1 = end_1 - start_1
    # Fin de l'execution en multi-process
    
    # Début de l'execution en multi-process
    start_2 = time.time() # On démarre le chrono
    nb_hits=frequence_de_hits_pour_n_essais(nb_total_iteration)
    end_2 = time.time() # On stop le chrono
    time_execution_2 = end_2 - start_2
    # Fin de l'execution en multi-process
    
    print("Valeur estimée Pi par la méthode Mono−Processus : ", 4 * nb_hits / nb_total_iteration)
    print("Le temps d'éxecution par la méthode Mono−Processus est de: ",time_execution_2)
    print("Valeur estimée Pi par la méthode Multi−Processus : ", 4 * resultat / nb_iteration_par_process)
    print("Le temps d'éxecution par la méthode Multi−Processus est de: ",time_execution_1)

