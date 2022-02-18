from stack import Stack
from queue import Queue
from p_queue import PQueue
from math import ceil, log2
from random import randrange

class Graph: 

    def __init__(self, file, list = True, weighted = True, directed=False) -> None:
        self._list = list
        self._vertices = 0
        self._degree = []
        self._graph = []
        self._edges = 0
        self._level = []
        self._connected_components = []
        self._connected_marker = []
        self._arvore = []

        # If the graph is directed we will work with matrix only
        if (directed):
            self._list = False

        # Flags 
        self._weighted = weighted
        self._negative_weighted = False
        
        # auxiliar function to set the flags
        def checkFlags(temp):
            if (self._weighted and self._negative_weighted == False):
                if (float(temp[2]) < 0):
                    self._negative_weighted = True   

        with open(file) as reader:
            line  = reader.readline()
            line = line.replace('\n', '')
            # get the number of vertices
            self._vertices = int(line) 

            # creates a vector with size = number of vertices and 0 in every position
            self._degree = [0 for x in range(self._vertices)] 
            self._connected_marker = [0 for x in range(self._vertices)] 
            self._parents = [0 for x in range(self._vertices)]

             # updates the degree vector with the actual value for each vertex and updates the number of edges
            reader.seek(0, 0)
            line = reader.readline()
            line = reader.readline()
            while line != '':
                self._edges += 1 
                line = line.replace('\n', '')
                temp = line.split(' ')
                vertex = int(temp[0])
                self._degree[vertex-1] += 1 
                vertex = int(temp[1])
                self._degree[vertex-1] += 1
                line = reader.readline()

        if (self._list):
            with open(file) as reader:
                # creates an array with size = number of vertices
                self._graph = [0 for x in range(self._vertices)]
                # populates each position with an array with this vertex's degree as size
                for i in range(self._vertices):
                    self._graph[i] = [None for x in range(self._degree[i])]
                
                # populates the self._list_graph with it's edges
                for w in range(2):
                    reader.seek(0, 0)
                    line = reader.readline()
                    line = reader.readline()
                    while line != '':
                        line = line.replace('\n', '')
                        temp = line.split(' ')
                        checkFlags(temp)
                        vertex = int(temp[w])
                        edge = int(temp[1 if w == 0 else 0])
                        index = self._graph[vertex-1].index(None)
                        self._graph[vertex-1][index] = [None for x in range(2)]
                        self._graph[vertex-1][index][0] = edge 
                        self._graph[vertex-1][index][1] = float(temp[2]) if self._weighted else 0
                        line = reader.readline()

                # sorts each edge vector
                for vertex in self._graph:
                    vertex.sort() 
        else:
            with open(file) as reader:
                # creates a matrix nxn
                self._graph = [[False for x in range(self._vertices)] for x in range(self._vertices)]
                line = reader.readline()
                line = reader.readline()
                while line != '':
                    line = line.replace('\n', '')
                    temp = line.split(' ')
                    checkFlags(temp)
                    self._graph[int(temp[0])-1][int(temp[1])-1] = float(temp[2]) if self._weighted else True
                    if (not(directed)):
                        self._graph[int(temp[1])-1][int(temp[0])-1] = float(temp[2]) if self._weighted else True
                    line = reader.readline()

    def toMatrix(self):
        m = [[False for x in range(self._vertices)] for x in range(self._vertices)]
        for index, edges in enumerate(self._graph):
            for edge in edges:
                m[index][edge[0] - 1] = edge[1]
        return m

    def getAverageDegree(self):
        """ Returns the average degree. """
        return sum(self._degree)/self._vertices

    def getMedianDegree(self):
        """ Returns the median degree. """
        degree_sorted = sorted(self._degree)
        if (self._vertices % 2 == 0):
            x = degree_sorted[ ceil(self._vertices/2) - 1]
            y = degree_sorted[ ceil(self._vertices/2)]
            return (x+y)/2
        return degree_sorted[ ceil(self._vertices/2) - 1]

    def getInfo(self, file):
        """ 
            Creates a .txt file with the following information: 
            Number of vertices and edges, max and min degree, average degree, median degree
        """
        if ('.txt' not in file):
            file = file + '.txt'
        with open(file, 'w') as writer:
            writer.write('Numero de vertices: ' + str(self._vertices) + '\n')
            writer.write('Numero de arestas: ' + str(self._edges) + '\n')
            writer.write('Grau maximo: ' + str(max(self._degree)) + '\n' )
            writer.write('Grau minimo: ' + str(min(self._degree)) + '\n' )
            writer.write('Grau medio: ' + "{:.2f}".format(self.getAverageDegree()) + '\n' )
            writer.write('Mediana do grau: ' + "{:.1f}".format(self.getMedianDegree()) + '\n' )
            writer.write('Componentes conexas: \n' + self.getConnectedComponents(False))
    
    def bfs(self, s, w=True, p=False, b=0):
        """ Executes a bfs, starting in the given vertex s. """
        marker = [0 for x in range(len(self._graph))]
        self._level = [-1 for x in range(len(self._graph))]
        queue = Queue() 
        queue_removed = []
        queue.push(s)
        marker[s-1] = 1
        self._level[s-1] = 0
        
        self._arvore.append(["V,P,N"])
        self._arvore.append([f"{s},-1,0"])
        while (len(queue) != 0):
            u = queue.pop()
            queue_removed.append(u)

            if (p and u == b):
                return queue_removed

            if self._list:
                for item in self._graph[u-1]:
                    item = item[0]
                    if marker[item-1] == 0:
                        marker[item-1] = 1
                        self._level[item-1] = self._level[u-1] + 1
                        self._arvore.append([f"{item},{u},{self._level[item-1]}"])
                        queue.push(item)
                        self._parents[item-1] = u
            else:
                for index, item in enumerate(self._graph[u-1]):
                    if (item):
                        if marker[index] == 0:
                            marker[index] = 1
                            self._level[index] = self._level[u-1] + 1
                            self._arvore.append([f"{index + 1},{u},{self._level[index]}"])
                            queue.push(index + 1)
                            self._parents[index] = u
        if (w):
            with open('bfs.txt', 'w')  as writer:
                for item in self._arvore:
                    for text in item:
                        writer.write(text + '\n')
        else:
            return queue_removed
        
    def dfs(self, s, w=True):
        """ Executes a bfs, starting in the given vertex s. """
        marker = [0 for x in range(len(self._graph))]
        stack = Stack()
        stack.push(s)
        arvore = [0 for x in range(len(self._graph))]
        level = [0 for x in range(len(self._graph))]
        level[s-1] = 0
        arvore[s-1] = f"{s},-1,{0}"
        while(len(stack) != 0):
            u = stack.pop()

            if self._list:
                if marker[u-1] == 0:
                    marker[u-1] = 1
                    for item in reversed(self._graph[u-1]):
                        item = item[0]
                        stack.push(item)
                        if (marker[item-1]==0):
                            self._parents[item-1] = u
                            level[item-1] = level[u-1] + 1
                            arvore[item-1] = f"{item},{u},{level[item-1]}"
            else:
                if marker[u-1] == 0:
                    marker[u-1] = 1
                    for index, item in reversed(list(enumerate(self._graph[u-1]))):
                        if (item):
                            stack.push(index+1)
                            if (marker[index]==0):
                                self._parents[index] = u
                                level[index] = level[u-1] + 1
                                arvore[index] = f"{index+1},{u},{level[index]}"
        if (w):                                    
            with open('dfs.txt', 'w')  as writer:
                writer.write("V,P,N" + '\n')
                for text in arvore:
                    writer.write(text + '\n')
    
    def dijkstra(self, s, write=True, p=False, b=0):
        """ executes dijkstra algorithm and returns a txt file with distances and path"""

        dist = PQueue(self._vertices)
        path = [] 
        dist_arr = [float('inf') for x in range(self._vertices)]
        explored = [False for x in range(self._vertices)]

        dist.update(s-1,0)
        dist_arr[s-1] = 0
        
        while (dist.getSize() > 0):
            u = dist.pop()
            path.append(u+1)
            explored[u] = True
            if (p and u+1 == b):
                return [path,dist_arr]

            # list
            if (self._list):
                for edge in self._graph[u]:
                    v = edge[0]-1
                    p = edge[1]
                    if (not(explored[v]) ):
                        if (dist_arr[v] > dist_arr[u] + p):
                            dist_arr[v] = dist_arr[u] + p
                            dist.update(v, dist_arr[v])
            else:
                for i, p in enumerate(self._graph[u]):
                    if (type(p) != bool):
                        if(dist_arr[i] > dist_arr[u] + p):
                            dist_arr[i] = dist_arr[u] + p
                            dist.update(i, dist_arr[i])

        if(write):
            with open('dijkstra.txt', 'w') as writer:
                writer.write('dijkstra partindo do vértice' + str(s) + ':\n')
                writer.write('distancias: ' + str(dist_arr)+ '\n')
                writer.write('caminho: ' + str(path)+ '\n')
        else:
            return [path,dist_arr]

    def getDistance(self,a,b, w=True):
        """ Returns the  shortest path between vertex a and b. """
        filename = 'distance_' + str(a) + '_' + str(b) + '.txt'
        if (self._weighted == True):
            if (self._negative_weighted == True):
                pass
                # Floyd-Warshal ou Bellman-Ford
            else:
                result = self.dijkstra(a, write=False)
                result = str(result[1][b-1])
        else: 
            self.bfs(a, False)
            result = str(self._level[b-1])
        if (w):
            with open(filename, 'w') as writer:
                writer.write('distancia entre ' + str(a) + '-' + str(b) + ':' + result)
        else:
            return result

    def getPath(self, a, b, w=True):
        filename = 'path' + str(a) + '_' + str(b) + '.txt'
        if (self._weighted == True):
            if (self._negative_weighted == True):
                pass
                # Floyd-Warshal ou Bellman-Ford
            else:
                result = self.dijkstra(a, False, True, b)
                result = str(result[0])
        else: 
            self.bfs(a, False, True, b)
            result = str(self._level[b-1])
        if (w):
            with open(filename, 'w') as writer:
                writer.write('caminho entre ' + str(a) + '-' + str(b) + ':' + result)
        else:
            return result



    def getDiameter(self, w=True, opt=False):
        """ 
        Returns the diameter of the graph. 
        The parameter 'opt' controls if the full algorithm will run or only an approximation
        """
        diameter = 0
        if (opt):
            """ Approximative run. Note it may not work for small graphs. """
            for i in range( int(log2(self._vertices)) ):
                index = randrange(1, self._vertices)
                self.bfs(index, False)
                diameter = eval(self._arvore[-1][-1][-1]) if (eval(self._arvore[-1][-1][-1]) > diameter) else diameter
        else: 
            for vertex_a in range(self._vertices):
                self.bfs(vertex_a-1, False)
                diameter = eval(self._arvore[-1][-1][-1]) if (eval(self._arvore[-1][-1][-1]) > diameter) else diameter  
        if (w):
            with open('diameter.txt', 'w') as writer:
                writer.write('diametro do grafo: ' + str(diameter))
        else:
            return diameter   
    
    def getConnectedComponents (self, w=True):
        """ Returns a list of lists of all connected components. """
        while sum(self._connected_marker) != self._vertices:
            if (self._weighted):
                connected = self.dijkstra(self._connected_marker.index(0)+1, False)
            else:
                connected = self.bfs(self._connected_marker.index(0)+1, False)
            connected = list(map(lambda x: x - 1,connected))
            for vertex in connected:
                self._connected_marker[vertex] = 1
            self._connected_components.append(list(map(lambda x: x + 1,connected)))
        self._connected_components = sorted(self._connected_components, key = lambda x: len(x), reverse=True)

        result = ''
        for component in self._connected_components:
            str_component = str(component).replace('[', '')
            str_component = str_component.replace(']', '')
            result +='tamanho: ' + str(len(component)) + '--> '
            result += str_component +'\n'

        if (w):
            with open('connected_components.txt', 'w') as writer:
                writer.write(result)         
        else:
            return result

    def getParent(self, v):
        return(self._parents[v-1])  

    def floyd_warshall(self):
        d = copy(self._graph)
        for v in range(self._vertices):
            for e in range(self._vertices):
                
                if d[v][e] == False and v != e:
                    d[v][e] = math.inf
        
        for k in range(self._vertices):
            for i in range(self._vertices):
               for j in range(self._vertices):
                   
                   if d[i][j] > d[i][k] + d[k][j]:
                       d[i][j] = d[i][k] + d[k][j]
        return(d)

    def minKey(self, key, mstSet):
 
        # Initialize min value
        min = math.inf
 
        for v in range(self._vertices):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
 
        return min_index
    
def primMST(self, graphN):
        min = PQueue(self._vertices)
        mstSet = [False] * self._vertices
        key = [math.inf] * self._vertices
        key[0] = 0
        min.update(0,0)
        parent = [None] * self._vertices
        parent[0] = -1
        weight = 0

        while min.getSize() > 0:
            
            u = min.pop() 

            mstSet[u] = True

            for v in self._graph[u]:
                if mstSet[v[0]-1] == False and key[v[0]-1] > v[1]:
                    key[v[0]-1] = v[1]
                    min.update(v[0]-1,v[1])
                    parent[v[0]-1] = u
            
        for w in key:
            weight += w                

        with open('mst' + f'_grafo_W_{graphN}' +'.txt', 'w')  as writer:
                writer.write("Peso:" + str(weight) + '\n')
                writer.write("u,v" + '\n')
                for u, v in enumerate(parent):
                    if v != -1:
                        writer.write(str(u+1) + "-" +str(v+1) + '\n')
