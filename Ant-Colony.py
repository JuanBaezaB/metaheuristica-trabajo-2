import numpy as np
import time
import sys

start = time.time() 
# py.exe .\Ant-Colony.py 3 .\berlin52.tsp.txt 50 100 0.1 2.5 0.9

def inicializar_feromona(n,c):
    feromona = np.full((n,n),1/(c*n))
    return feromona, 1/(c*n)

def inicializar_colonia_hormigas(h,n):
    poblacion = np.full((h, n), -1)
    for i in range(h):
        poblacion[i][0] = float(np.random.randint(n))
    return poblacion

def calcular_distancias():
    distancias = np.full((nodos,nodos),-1, dtype=float)
    for i in range(nodos):
        for j in range(i+1, nodos):
            distancia = np.sqrt(np.sum(np.square(matriz_dist[i]-matriz_dist[j])))
            distancias[i][j] = distancia
            distancias[j][i] = distancia
    return 1/distancias

def seleccionar_nuevo_segmento():
    Thenodos = np.arange(nodos)
    for i in range(tamaño_pobl):
        row = poblacion[i][:]
        visitados = np.where(row != -1)
        visitados = [poblacion[i][item] for item in visitados]              # Usar visitados[0] para futuros calculos como se ve en noVisitados
        noVisitados = [item for item in Thenodos if item not in visitados[0]]
        if np.random.rand() < prob_limite:
            arg = []
            for j in noVisitados:
                arg.append(feromona[visitados[0][-1]][j]*((distancias[visitados[0][-1]][j])**val_heuristica))
            arg = np.array(arg)
            max = np.where(arg == np.amax(arg))
            poblacion[i][len(visitados[0])] = noVisitados[max[0][0]]
            feromona[poblacion[i][len(visitados[0])]][poblacion[i][len(visitados[0])-1]] = (1-evap_feromona)*feromona[poblacion[i][len(visitados[0])]][poblacion[i][len(visitados[0])-1]] + evap_feromona/(nodos*feromonaLocal)
            feromona[poblacion[i][len(visitados[0])-1]][poblacion[i][len(visitados[0])]] = feromona[poblacion[i][len(visitados[0])]][poblacion[i][len(visitados[0])-1]]
        else:
            arg = [0]
            for j in range(len(noVisitados)):
                arg.append(feromona[visitados[0][-1]][noVisitados[j]]*((distancias[visitados[0][-1]][noVisitados[j]])**val_heuristica))
            arg /= np.sum(arg)
            arg = np.array(arg)
            arg = np.cumsum(arg)
            rand = np.random.rand()
            pos = np.where(arg < rand)
            poblacion[i][len(visitados[0])] = noVisitados[pos[0][-1]]
            feromona[poblacion[i][len(visitados[0])]][poblacion[i][len(visitados[0])-1]] = (1-evap_feromona)*feromona[poblacion[i][len(visitados[0])]][poblacion[i][len(visitados[0])-1]] + evap_feromona/(nodos*feromonaLocal)
            feromona[poblacion[i][len(visitados[0])-1]][poblacion[i][len(visitados[0])]] = feromona[poblacion[i][len(visitados[0])]][poblacion[i][len(visitados[0])-1]]
    return poblacion

def solucionCalcularCosto(n,s,c):
    aux = 1/c[s[n-1]][s[0]]
    for i in range(n-1):
        aux+=(1/c[s[i]][s[i+1]])
    return np.round(aux, decimals = 4)

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
nodos = len(matriz_dist)
distancias = calcular_distancias()
solucionMejor = np.arange(0,nodos)
np.random.shuffle(solucionMejor)
solucionMejorCosto = solucionCalcularCosto(nodos,solucionMejor,distancias)
feromona, feromonaLocal = inicializar_feromona(nodos, solucionMejorCosto)

while 0 < num_ite and not np.round(solucionMejorCosto,decimals=4) == 7544.3659:
    poblacion = inicializar_colonia_hormigas(tamaño_pobl, nodos)
    for i in range(nodos-1):
        poblacion = seleccionar_nuevo_segmento()
    for i in range(tamaño_pobl):
        aux = solucionCalcularCosto(nodos,poblacion[i][:],distancias)
        if aux < solucionMejorCosto:
            solucionMejorCosto = aux
            solucionMejor = poblacion[i][:]
    for i in poblacion:
        feromona[poblacion[0]][poblacion[-1]] =  (1-evap_feromona)*feromona[poblacion[0]][poblacion[-1]] + evap_feromona/(nodos*feromonaLocal)
        feromona[poblacion[-1]][poblacion[0]] = feromona[poblacion[0]][poblacion[-1]]
    for i in range(nodos):
        for j in range(nodos):
            feromona[i][j] = (1-evap_feromona)*feromona[i][j]
            feromona[j][i] = (1-evap_feromona)*feromona[j][i]
    feromona[solucionMejor[0]][solucionMejor[-1]] = (1-evap_feromona)*feromona[solucionMejor[0]][solucionMejor[-1]] + evap_feromona/solucionMejorCosto
    feromona[solucionMejor[-1]][solucionMejor[0]] = feromona[solucionMejor[0]][solucionMejor[-1]]
    for i in range(len(solucionMejor)-1):
        feromona[solucionMejor[i]][solucionMejor[i + 1]] += evap_feromona/solucionMejorCosto
        feromona[solucionMejor[i + 1]][solucionMejor[i]] = feromona[solucionMejor[i]][solucionMejor[i + 1]]
    num_ite -= 1
print(solucionMejorCosto, " ", solucionMejor)


# sol = np.genfromtxt("berlin52.opt.tour.txt", skip_header = 4 , skip_footer=1, dtype = int)
# print(sol)
# print(solucionCalcularCosto(nodos,sol-1,distancias))


end = time.time()
print('Tiempo de ejecución:', end - start,'segundos')