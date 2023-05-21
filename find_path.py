class Graph:
    def __init__(self):
        self.n: int = 0
        self.vertices: list[Vertice] = []
        self.startIndex: int = 0

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
            self.vertices.append(Vertice(up, down, left, right))
            if ver == 0:
                self.startIndex = i



class Vertice:
    '''
    Stores vertice with possible connections, where connection(eg. up) is in form (INDEX, COST)
    '''
    def __init__(self, up: tuple[int,int], down: tuple[int,int],
                  left: tuple[int,int], right: tuple[int,int]):
        self.up: tuple[int,int] = up
        self.down: tuple[int,int] = down
        self.left: tuple[int,int] = left
        self.right: tuple[int,int] = right

elo = Graph()
elo.ReadFile('plansza.txt')
print(elo.startIndex)
print(':)')
