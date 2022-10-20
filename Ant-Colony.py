from unicodedata import decimal
import numpy as np
import time
import sys
import math

start = time.time() # py.exe .\Ant-Colony.py 4 .\berlin52.tsp.txt 40 200 0.1 2.5 0.9

def inicializar_feromona(n,c):
    feromona = np.full((n,n),1/(c*n))
    return feromona

def inicializar_colonia_hormigas(h,n):
    poblacion = np.full((h, n), -1)
    for i in range(h):
        poblacion[i][0] = np.random.randint(n)
    return poblacion

def calcular_distancias():
    distancias = np.full((len(matriz_dist),len(matriz_dist)),-1)
    for i in range(len(matriz_dist)):
        for j in range(i+1, len(matriz_dist)):
            distancia = np.sqrt(np.sum(np.square(matriz_dist[i]-matriz_dist[j])))
            distancias[i][j] = distancia
            distancias[j][i] = distancia
    return 1/distancias

def seleccionar_nuevo_segmento():
    nodos = np.arange(len(matriz_dist))
    for i in range(len(poblacion)):
        row = poblacion[i][:]
        visitados = np.where(row != -1)
        visitados = [poblacion[i][item] for item in visitados]              # Usar visitados[0] para futuros calculos como se ve en noVisitados
        noVisitados = [item for item in nodos if item not in visitados[0]]
        if np.random.rand() < prob_limite:
            arg = []
            for j in noVisitados:
                arg.append(feromona[visitados[0][-1]][j]*((distancias[visitados[0][-1]][j])**val_heuristica))
            arg = np.array(arg)
            max = np.where(arg == np.amax(arg))
            poblacion[i][len(visitados[0])] = noVisitados[max[0][0]]
        else:
            arg = []
            for j in noVisitados:
                arg.append(feromona[visitados[0][-1]][j]*((distancias[visitados[0][-1]][j])**val_heuristica))
            arg = np.array(arg)
            max = np.where(arg == np.amax(arg))
            poblacion[i][len(visitados[0])] = noVisitados[max[0][0]]
    return poblacion

def solucionCalcularCosto(n,s,c):
    #n: numero de variables
    #s:vector solucion
    #c:matriz de distancias
    print(c)
    aux = c[s[n-1]][s[0]]
    for i in range(n-1):
        aux+=c[s[i]][s[i+1]]
    return aux

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

matriz_dist = np.genfromtxt(matriz_dist, delimiter=' ', skip_header = 6 , usecols=(1,2) , skip_footer=1, dtype = float)
distancias = calcular_distancias()

solucionMejor = np.arange(0,len(matriz_dist))
np.random.shuffle(solucionMejor)
solucionMejorCosto= solucionCalcularCosto(len(matriz_dist),solucionMejor,distancias)
feromona = inicializar_feromona(len(matriz_dist), solucionMejorCosto)

poblacion = inicializar_colonia_hormigas(tamaño_pobl, len(matriz_dist))
for i in range(len(matriz_dist)-1):
    poblacion = seleccionar_nuevo_segmento()
print(poblacion)


generacion = 0
while generacion < num_ite and not (np.round(solucionCalcularCosto,decimals=4)) == 7544.3659:

    generacion+=1
end = time.time()
print('Tiempo de ejecución:', end - start,'segundos')