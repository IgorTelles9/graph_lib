from queue import Queue
from math import ceil 
class Graph: 

    def __init__(self, file, list = True) -> None:
        self._list = list
        self._vertices = 0
        self._degree = []
        self._graph = []
        self._edges = 0
        self._level = []

        with open(file) as reader:
            line  = reader.readline()
            line = line.replace('\n', '')
            # get the number of vertices
            self._vertices = int(line) 

            # creates a vector with size = number of vertices and 0 in every position
            self._degree = [0 for x in range(self._vertices)] 

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
                self._graph = [0 for x in range(self._vertices)]
                
                # creates a vector with size = number of vertices and an array with size = vertex degree in each position
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
                        vertex = int(temp[w])
                        edge = int(temp[1 if w == 0 else 0])
                        index = self._graph[vertex-1].index(None)
                        self._graph[vertex-1][index] = edge
                        line = reader.readline()
                
                # sorts each edge vector
                for vertex in self._graph:
                    vertex.sort()
        else:
            with open(file) as reader:
                # creates a matrix nxn
                self._graph = [[0 for x in range(self._vertices)] for x in range(self._vertices)]
                line = reader.readline()
                line = reader.readline()
                while line != '':
                    line = line.replace('\n', '')
                    temp = line.split(' ')
                    self._graph[int(temp[0])-1][int(temp[1])-1] = 1
                    self._graph[int(temp[1])-1][int(temp[0])-1] = 1
                    line = reader.readline()


    def getAverageDegree(self):
        return sum(self._degree)/self._vertices

    def getMedianDegree(self):
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
            writer.write('Grau médio: ' + "{:.2f}".format(self.getAverageDegree()) + '\n' )
            writer.write('Mediana do grau: ' + "{:.1f}".format(self.getMedianDegree()) + '\n' )
    
    def bfs(self, s, w=True):
        """ Executes a bfs, starting in the given vertex s. Return a txt file"""
        marker = [0 for x in range(len(self._graph))]
        self._level = [-1 for x in range(len(self._graph))]
        queue = Queue() 
        queue_removed = []
        queue.push(s)
        marker[s-1] = 1
        self._level[s-1] = 0
        arvore =[]

        arvore.append([f"Vértice {s} - Pai: Não tem, Nível: 0"])
        while (len(queue) != 0):
            u = queue.pop()
            queue_removed.append(u)

            if self._list:
                for item in self._graph[u-1]:
                    if marker[item-1] == 0:
                        marker[item-1] = 1
                        self._level[item-1] = self._level[u-1] + 1
                        arvore.append([f"Vértice {item} - Pai: {u}, Nível: {self._level[item-1]}"])
                        queue.push(item)
            else:
                for index, item in enumerate(self._graph[u-1]):
                    if item == 1:
                        if marker[index] == 0:
                            marker[index] = 1
                            self._level[index] = self._level[u-1] + 1
                            arvore.append([f"Vértice {index + 1} - Pai: {u}, Nível: {self._level[index]}"])
                            queue.push(index + 1)

        if (w):
            with open('bfs.txt', 'w')  as writer:
                for item in arvore:
                    for text in item:
                        writer.write(text + '\n')
        
    def getDistance(self,a,b, w=True):
        self.bfs(a, False)
        if (w):
            with open('distance_' + str(a) + '_' + str(b) + '.txt', 'w') as writer:
                writer.write(str(self._level[b-1]))
        else:
            return self._level[b-1]

    def getDiameter(self, w=True):
        diameter = 0
        for vertex_a in range(self._vertices):
            self.bfs(vertex_a-1, False)
            diameter = max(self._level) if (max(self._level) > diameter) else diameter
            
        if (w):
            with open('diameter.txt', 'w') as writer:
                writer.write(str(diameter))
        else:
            return diameter   
      
g = Graph('grafo_1.txt')
g.getInfo('exit.txt')
g.bfs(1)
g.getDistance(1,3)
g.getDiameter()

                
                

            
            

                

        