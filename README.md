# Algoritmo genético para el Problema del Vendedor Viajero
El programa presenta una solución estocástica llamada algoritmo genético para la resolución del problema de las n reinas.
Para el correcto funcionamiento de este se deben considerar los siguientes puntos:
## Instalación
Para instalar la aplicación se deben seguir los siguientes pasos:
- Para bajar el programa haga click en el siguiente [link](https://github.com/JuanBaezaB/metaheuristica-trabajo-1/archive/refs/heads/main.zip)
- La aplicación funciona sobre python 3.10.5 o superior
- Instalar la biblioteca ``numpy`` con el siguiente comando:
```
pip install numpy
```
## Ejecución
- Para ejecutar se debe ejecutar el comando 
```
python .\Ant-Colony.py seed matriz_dist tamaño_pobl num_ite evap_feromona val_heuristica prob_limite 
```
- Donde:
  - **seed** es un valor entero positivo
  - **matriz_dist** son la posición x y de los nodos 
  - **tamaño_pobl** es un valor entero positivo igual o mayor a 2 que representa la cantidad de hormigas
  - **num_ite** es el número máximo de iteraciones que realiza el programa que toma valores mayores o iguales a 1
  - **evap_feromona** es el peso del valor de la heuristica
  - **val_heuristica** es un valor decimal en 2 y 3
  - **prob_limite** es un valor decimal entre 0.0 y 1.0 que representa la probabilidad el q0 para elegir le próximo nodo, este puede ser elegido por mejor resultado o por método de la ruleta
- Un ejemplo de entrada es la siguiente:
```
 py.exe .\Ant-Colony.py 3 .\berlin52.tsp.txt 50 100 0.1 2.5 0.9
```

Este programa fue desarrollado en [Github](https://github.com/JuanBaezaB/metaheuristica-trabajo-2)
## Autores
- Juan Baeza Baeza / jbaeza@ing.ucsc.cl / [JuanBaezaB](https://github.com/JuanBaezaB)
- Fernando Cabezas Herrera / fcabezas@ing.ucsc.cl / [FernandoProg](https://github.com/FernandoProg)
