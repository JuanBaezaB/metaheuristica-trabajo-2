from operator import le
import numpy as np
import time
import sys

start = time.time()

def inicializar_feromona(n):
    feromona = np.full((n,n),0.01)
    return feromona

def inicializar_colonia_hormigas(h,n):
    poblacion = np.full((h, n), -1)
    for i in range(h):
        poblacion[i][0] = np.random.randint(n)
    return poblacion

if len(sys.argv) == 8:
    seed = int(sys.argv[1])
    matriz_dist = str(sys.argv[2])
    tamaño_pobl = int(sys.argv[3])
    num_ite = int(sys.argv[4])
    evap_feromona = float(sys.argv[5])
    val_heuristica = float(sys.argv[6])
    prob_limite = float(sys.argv[7])
    print("semilla: ", seed)
    print("matriz de distancias: ", matriz_dist)
    print("tamaño de poblacion: ", tamaño_pobl)
    print("numero de iteraciones: ", num_ite)
    print("factor de evaporacion de la feromona: ", evap_feromona)
    print("peso del valor de la heuristica: ", val_heuristica)
    print("valor de probabilidad limite: ", prob_limite)
else:
    print('Error en la entrada de los parametros')
    print('Los paramentros a ingresar son: semilla, matriz de distancias, tamaño de poblacion, numero de iteraciones, factor de evaporacion de la feromona, peso del valor de la heuristica, valor de probabilidad limite')
    sys.exit(0)

np.random.seed(seed)

matriz_dist = np.genfromtxt(matriz_dist, delimiter=' ', skip_header = 6 , usecols=(0,1,2) , skip_footer=1, dtype = float)
feromona = inicializar_feromona(len(matriz_dist))
poblacion = inicializar_colonia_hormigas(tamaño_pobl, len(matriz_dist))
print(feromona)

end = time.time()
print('Tiempo de ejecución:', end - start,'segundos')