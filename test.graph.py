import time
from graph import Graph

# Criação do grafo 
start = time.time()
g = Graph('grafo_2.txt', False)
finish = time.time()
print('time elapsed in : ', finish-start)

# BFS 
start = time.time()
g.getInfo('info.txt')
finish = time.time()
print('time elapsed in : ', finish-start)