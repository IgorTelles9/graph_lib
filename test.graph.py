import time
from graph import Graph
#import psutil

# Item 1
# start = time.time()
g = Graph('grafo_3.txt', False)
# print('memory use in mb: ', psutil.Process().memory_info().rss / (1024 * 1024))
# finish = time.time()
# print('time elapsed in : ', finish-start)

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
with open('dfs-time.txt', 'w') as writer:
    for i in range(1000):
        start = time.time()
        g.dfs(i+1, False)
        finish = time.time()
        r = finish-start
        writer.write(str(r)+'\n')

###########################################################################################