class Graph: 

    def __init__(self, file, list = True) -> None:
        self._list = list
        self._vertex_size = 0
        self._degree = []
        self._graph = []
        with open(file) as reader:
            line  = reader.readline()
            line = line.replace('\n', '')
            # get the number of vertices
            self._vertex_size = int(line) 

        if (self._list):
            with open(file) as reader:
                self._graph = [0 for x in range(self._vertex_size)]
                # creates a vector with size = number of vertices and 0 in every position
                self._degree = [0 for x in range(self._vertex_size)] 
        
                # updates the degree vector with the actual value for each vertex
                reader.seek(0, 0)
                line = reader.readline()
                line = reader.readline()
                while line != '':
                    line = line.replace('\n', '')
                    temp = line.split(' ')
                    vertex = int(temp[0])
                    self._degree[vertex-1] += 1 
                    vertex = int(temp[1])
                    self._degree[vertex-1] += 1
                    line = reader.readline()
                
                # creates a vector with size = number of vertices and an array with size = vertex degree in each position
                for i in range(self._vertex_size):
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
                self._graph = [[0 for x in range(self._vertex_size)] for x in range(self._vertex_size)]
                line = reader.readline()
                line = reader.readline()
                while line != '':
                    line = line.replace('\n', '')
                    temp = line.split(' ')
                    self._graph[int(temp[0])-1][int(temp[1])-1] = 1
                    line = reader.readline()


    def getInfo(self):
       # n´umero de v´ertices, n´umero de arestas, grau m´ınimo, grau m´aximo, grau m´edio,
       # e mediana de grau. Al´em disso, imprimir informa¸c˜oes sobre as componentes conexas (ver
       # abaixo).
       pass

g = Graph('g.txt', False)

                
                

            
            

                

        