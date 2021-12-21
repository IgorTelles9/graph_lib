from queue import Queue
class Graph: 

    def __init__(self, file, list = True) -> None:
        self._list = list
        self._vertices = 0
        self._degree = []
        self._graph = []
        self._edges = 0

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
    
    def bfs(self, s):
        """ Executes a bfs, starting in the given vertex s. Return a txt file"""
        marker = [0 for x in range(len(self._graph))]
        level = [-1 for x in range(len(self._graph))]
        queue = Queue() 
        queue_removed = []
        queue.push(s)
        marker[s-1] = 1
        level[s-1] = 0
        arvore =[]

        arvore.append([f"Vértice {s} - Pai: Não tem, Nível: 0"])
        while (len(queue) != 0):
            u = queue.pop()
            queue_removed.append(u)

            if self._list:
                for item in self._graph[u-1]:
                    if marker[item-1] == 0:
                        marker[item-1] = 1
                        level[item-1] = level[u-1] + 1
                        arvore.append([f"Vértice {item} - Pai: {u}, Nível: {level[item-1]}"])
                        queue.push(item)
            else:
                for index, item in enumerate(self._graph[u-1]):
                    if item == 1:
                        if marker[index] == 0:
                            marker[index] = 1
                            level[index] = level[u-1] + 1
                            arvore.append([f"Vértice {index + 1} - Pai: {u}, Nível: {level[index]}"])
                            queue.push(index + 1)

        with open('bfs.txt', 'w')  as writer:
            for item in arvore:
                for text in item:
                    writer.write(text + '\n')
        
g = Graph('grafo_1.txt')
g.getInfo('exit.txt')
g.bfs(1)

                
                

            
            

                

        