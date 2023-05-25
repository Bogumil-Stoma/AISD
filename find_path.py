# from sys import maxsize

class Graph:
    def __init__(self):
        self.n: int = 0
        self.vertices: list[Vertice] = []
        self.startIndex: int = None
        self.destIndex: int = None

    def ReadFile(self, file):
        verticesTMP = []
        with open(file, 'r') as fp:
            for line in fp:
                verticesTMP.extend(list(line.strip()))
            self.n = len(line.strip())
        n = self.n
        verticesTMP = list(map(int, verticesTMP))
        for i, ver in enumerate(verticesTMP):
            if i < n*n-n: down = (i+n, verticesTMP[i+n])
            else: down = None
            if i >= n: up = (i-n, verticesTMP[i-n])
            else: up = None
            if i%n==0: left = None
            else: left = (i-1, verticesTMP[i-1])
            if i%n==(n-1): right =None
            else: right = (i+1, verticesTMP[i+1])
            self.vertices.append(Vertice(up, down, left, right, ver))
            if ver == 0:
                if self.startIndex is None: self.startIndex = i
                else: self.destIndex = i
            
            
    def FindPath(self):
        visited : list[int] = []
        unvisited : list[int] = [i for i in range(len(self.vertices))]
        vertex_table = [[float('inf'), None] for _ in self.vertices]


        vertex_table[self.startIndex][0] = 0
        vertex_table[self.startIndex][1] = self.startIndex

        while unvisited:
            # finding vertex with smallest cost
            current_vertex_index = unvisited[0]
            for vertex_index in unvisited:
                if vertex_table[vertex_index][0] < vertex_table[current_vertex_index][0]:
                    current_vertex_index = vertex_index
            
            current_vertex = self.vertices[current_vertex_index]
            
            if current_vertex.up is not None:
                neighbor_index = current_vertex.up[0]
                a = vertex_table[current_vertex_index][0] + current_vertex.up[1]
                if a < vertex_table[neighbor_index][0]:
                    vertex_table[neighbor_index][0] = a
                    vertex_table[neighbor_index][1] = current_vertex_index
            
            if current_vertex.down is not None:
                neighbor_index = current_vertex.down[0]
                a = vertex_table[current_vertex_index][0] + current_vertex.down[1]
                if a < vertex_table[neighbor_index][0]:
                    vertex_table[neighbor_index][0] = a
                    vertex_table[neighbor_index][1] = current_vertex_index

            if current_vertex.left is not None:
                neighbor_index = current_vertex.left[0]
                a = vertex_table[current_vertex_index][0] + current_vertex.left[1]
                if a < vertex_table[neighbor_index][0]:
                    vertex_table[neighbor_index][0] = a
                    vertex_table[neighbor_index][1] = current_vertex_index

            if current_vertex.right is not None:
                neighbor_index = current_vertex.right[0]
                a = vertex_table[current_vertex_index][0] + current_vertex.right[1]
                if a < vertex_table[neighbor_index][0]:
                    vertex_table[neighbor_index][0] = a
                    vertex_table[neighbor_index][1] = current_vertex_index
            
            visited.append(current_vertex_index)
            unvisited.remove(current_vertex_index)

        board = ["_" for _ in self.vertices]


        board[self.startIndex] = 0
        board[self.destIndex] = 0

        current_vertex_index = vertex_table[self.destIndex][1]
        while current_vertex_index != self.startIndex:
            board[current_vertex_index] = self.vertices[current_vertex_index].cost
            current_vertex_index = vertex_table[current_vertex_index][1]
        
        for i in range(len(board)):
            print(board[i], end='')
            if (i+1)%self.n==0:
                print()

        return(visited)



class Vertice:
    '''
    Stores vertice with possible connections, where connection(eg. up) is in form (INDEX, COST)
    '''
    def __init__(self, up: tuple[int,int], down: tuple[int,int],
                  left: tuple[int,int], right: tuple[int,int], cost):
        self.up: tuple[int,int] = up
        self.down: tuple[int,int] = down
        self.left: tuple[int,int] = left
        self.right: tuple[int,int] = right
        self.cost: int = cost

elo = Graph()
elo.ReadFile('plansza.txt')
elo.FindPath()
print()
elo = Graph()
elo.ReadFile('plansza1.txt')
elo.FindPath()
print()
elo = Graph()
elo.ReadFile('plansza2.txt')
elo.FindPath()
print()
elo = Graph()
elo.ReadFile('plansza3.txt')
elo.FindPath()
print()
elo = Graph()
elo.ReadFile('plansza5.txt')
elo.FindPath()
print(':)')
