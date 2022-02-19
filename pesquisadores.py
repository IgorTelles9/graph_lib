# 343930 - Ratton
# 11365 - turing
# 2722 - dijkstra
# 471365 - kruskal
# 5709 - jon kreinberg
# 11386 - Eva tardos

import time
from graph import Graph



g = Graph('rede_colaboracao.txt', list = True, weighted=True,directed = False)

#g.getPath(a=2722, b=343930, w=True)

#g.getPath(a=2722, b=11365, w=True)

g.getPath(a=2722, b=471365, w=True)
g.getPath(a=2722, b=5709, w=True)
g.getPath(a=2722, b=11386, w=True)



# 