from stack import Stack
from queue import Queue
from p_queue import PQueue
from math import ceil, log2
from random import randrange

class Graph: 

    def __init__(self, file, list = True) -> None:
        self._list = list
        self._vertices = 0
        self._degree = []
        self._graph = []
        self._edges = 0
        self._level = []
        self._connected_components = []
        self._connected_marker = []
        self._arvore = []

        # Flags 
        self._weighted = False
        self._negative_weighted = False
        
        # auxiliar function to set the flags
        def checkFlags(temp):
            if (self._weighted == False):
                if (float(temp[2])!= 0):
                    self._weighted = True
            if (self._negative_weighted == False):
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
                        self._graph[vertex-1][index][1] = float(temp[2])
                        line = reader.readline()

                # sorts each edge vector
                for vertex in self._graph:
                    vertex.sort() # needs to be changed
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
                    self._graph[int(temp[0])-1][int(temp[1])-1] = float(temp[2])
                    self._graph[int(temp[1])-1][int(temp[0])-1] = float(temp[2])
                    line = reader.readline()

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
    
    def bfs(self, s, w=True):
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

            if self._list:
                for item in self._graph[u-1]:
                    if marker[item-1] == 0:
                        marker[item-1] = 1
                        self._level[item-1] = self._level[u-1] + 1
                        self._arvore.append([f"{item},{u},{self._level[item-1]}"])
                        queue.push(item)
                        self._parents[item-1] = u
            else:
                for index, item in enumerate(self._graph[u-1]):
                    if item == 1:
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
        ordem = []
        marker = [0 for x in range(len(self._graph))]
        stack = Stack()
        stack.push(s)
        arvore = [0 for x in range(len(self._graph))]
        level = []
        level = [0 for x in range(len(self._graph))]
        level[s-1] = 0
        arvore[s-1] = f"{s},-1,{0}"
        while(len(stack) != 0):
            u = stack.pop()

            if self._list:
                if marker[u-1] == 0:
                    marker[u-1] = 1
                    for item in reversed(self._graph[u-1]):
                        stack.push(item)
                        if (marker[item-1]==0):
                            self._parents[item-1] = u
                            level[item-1] = level[u-1] + 1
                            arvore[item-1] = f"{item},{u},{level[item-1]}"
            else:
                if marker[u-1] == 0:
                    marker[u-1] = 1
                    for index, item in reversed(list(enumerate(self._graph[u-1]))):
                        if item == 1:
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
    
    def dijkstra(self, s, write=True):
        """ executes dijkstra algorithm and returns a txt file with distances and path"""
        filename = 'dijkstra'+str(s)+'.txt'

        dist = PQueue(self._vertices)
        path = [] 
        dist_arr = [float('inf') for x in range(self._vertices)]

        dist.update(s-1,0)
        dist_arr[s-1] = 0
        
        while (dist.getSize() > 0):
            u = dist.pop()
            path.append(u+1)

            # list
            for edge in self._graph[u]:
                v = edge[0]
                p = edge[1]
                if (dist_arr[v-1] > dist_arr[u] + p):
                    dist_arr[v-1] = dist_arr[u] + p
                    dist.update(v-1, dist_arr[v-1])
        
        if(write):
            with open(filename, 'w') as writer:
                writer.write('dijkstra partindo do vértice' + str(s) + ':\n')
                writer.write('distancias: ' + str(dist_arr)+ '\n')
                writer.write('caminho: ' + str(path)+ '\n')



    def getDistance(self,a,b, w=True):
        """ Returns the  shortest path between vertex a and b. """
        filename = 'distance_' + str(a) + '_' + str(b) + '.txt',
        if (self._weighted == True):
            if (self._negative_weighted == True):
                pass
                # Floyd-Warshal ou Bellman-Ford
            else:
                pass
                # Dijkstra
        else: 
            self.bfs(a, False)
            result = str(self._level[b-1])
        if (w):
            with open(filename, 'w') as writer:
                writer.write('distancia entre ' + str(a) + '-' + str(b) + ':' + result)
        else:
            return self._level[b-1]

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

        