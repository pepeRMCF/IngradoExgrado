class Graph():
    graph = {}
    v = 0
    route = ''
    filas = ''
    adjMatriz = []

    # Constructor que recibe la ruta del archivo
    def __init__(self, route):
        self.route = route

    # Creamos el grafo con los elementos del txt usando un dicionario (Graph) y una lista (adjacencyList)
    # Usamos el vprimer numero de cada linea como key del diccionario y el segundo numero es el valor
    def create_graph(self):
        with open(self.route, 'r') as f:
            self.v = int(f.readline().rstrip())
            lines = f.readlines()
        for i in lines:
            aristas = i.split(" ")
            vertice1 = int(aristas[0])
            vertice2 = int(aristas[1])
            if self.v < vertice1 and vertice1 > vertice2:
                self.v = vertice1

            if self.v < vertice2 and vertice2 > vertice1:
                self.v = vertice2

            if vertice1 not in list(self.graph):
                self.graph[vertice1] = []

            adjacencyList = self.graph[vertice1]

            adjacencyList.append(vertice2)
            self.graph[vertice1] = adjacencyList
        f.close()

    def matriz(self):
        self.create_graph()

        for i in range(self.v):
            filas = []
            for j in range(self.v):
                if i in list(self.graph) and j in self.graph[i]:
                    filas.append(1)
                else:
                    filas.append(0)
            self.adjMatriz.append(filas)
        for i in range(self.v):
            filas = ""
            for j in range(self.v):
                filas += str(self.adjMatriz[i][j])+" "
            # print(filas)

    def matriz_traspuesta(self, matrix):
        self.matriz()
        if matrix == None or len(matrix) == 0:
            return []

        result = [[None for i in range(len(matrix))]
                  for j in range(len(matrix[0]))]

        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                result[i][j] = matrix[j][i]

        return result

    def print_matrix(self, matrix):
        for row in matrix:
            print(*row)
    
    def IngradoExgrado(self, graph, n):
        _in = [0] * n
        out = [0] * n
        d = {k:v[0] for k,v in graph.items()}
        adjList = list(map(list, d.items()))
        for i in range(0, len(adjList)):
                List = adjList[i]
                out[i] = len(List)
                for j in range(0, len(List)):
                    _in[List[j]] += 1
        
        print("Vertice\tIngrado\tExgrado")
        for k in range(0, n):
                print(str(k) + "\t" + str(_in[k]) +
                            "\t" + str(out[k]))
    

ruta = Graph('doc.txt')
print('\n')
print('Matriz de traspuesta:')

mtraspuesta = ruta.matriz_traspuesta(ruta.adjMatriz)
ruta.print_matrix(mtraspuesta)
ruta.IngradoExgrado(ruta.graph, 5)

