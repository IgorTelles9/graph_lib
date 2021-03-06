import time
from graph import Graph
#import psutil

# Item 1
start = time.time()
g = Graph('grafo_W_4_0.txt', list=True, weighted=True, directed=True)
#g.dijkstra(1)
# for i in range(10,51,10):
#     print('dist entre 1 e ' + str(i) + ':' + str(g.getDistance(1,i, False)))
#     #print('caminho entre 1 e ' + str(i) + ':' + str(g.getPath(1,i, False)))
# # print('memory use in mb: ', psutil.Process().memory_info().rss / (1024 * 1024))
# finish = time.time() 
# print('time elapsed in : ', finish-start)

print(g.floyd_warshall())


###########################################################################################

# Item 2 - grafo 1 
# with open('bfs-time.txt', 'w') as writer:
#     for i in range(10):
#         for j in range(100):
#             start = time.time()
#             g.bfs(j+1, False)
#             finish = time.time()
#             r = finish-start
#             writer.write(str(r)+'\n')

# Item 2 - demais grafos
# with open('bfs-time.txt', 'w') as writer:
#     for i in range(1000):
#         start = time.time()
#         g.bfs(j+1, False)
#         finish = time.time()
#         r = finish-start
#         writer.write(str(r)+'\n')

###########################################################################################

# Item 3 - grafo 1 
# with open('dfs-time.txt', 'w') as writer:
#     for i in range(10):
#         for j in range(100):
#             start = time.time()
#             g.dfs(j+1, False)
#             finish = time.time()
#             r = finish-start
#             writer.write(str(r)+'\n')

#Item 2 - demais grafos
# with open('dfs-time.txt', 'w') as writer:
#     for i in range(1000):
#         start = time.time()
#         g.dfs(i+1, False)
#         finish = time.time()
#         r = finish-start
#         writer.write(str(r)+'\n')

###########################################################################################

# Item 6
# g.getConnectedComponents()

# Item 7
#g.getDiameter(opt=True)