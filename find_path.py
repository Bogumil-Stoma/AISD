from copy import deepcopy
from heapq import heappop, heappush
import sys

class Graph:
    def __init__(self):
        self.n: int = 0
        self.vertices: list[Vertice] = []
        self.justVertices = []
        self.startIndex: int = None
        self.destIndex: int = None

    def ReadFile1(self, file):
        verticesTMP = []
        with open(file, 'r') as fp:
            for line in fp:
                verticesTMP.extend(list(line.strip()))
            self.n = len(line.strip())
        n = self.n
        verticesTMP = list(map(int, verticesTMP))
        vertices2 = dict()
        for i, ver in enumerate(verticesTMP):
            vertices2[i] = dict()
            if i < n*n-n:
                down = (i+n, verticesTMP[i+n])
                vertices2[i][i+n] = verticesTMP[i+n]
            else:
                down = None

            if i >= n:
                up = (i-n, verticesTMP[i-n])
                vertices2[i][i-n] = verticesTMP[i-n]
            else: up = None
            if i%n==0: left = None
            else:
                left = (i-1, verticesTMP[i-1])
                vertices2[i][i-1] = verticesTMP[i-1]
            if i%n==(n-1): right =None
            else: right = (i+1, verticesTMP[i+1])
            self.vertices.append(Vertice(up, down, left, right, ver))
            if ver == 0:
                if self.startIndex is None: self.startIndex = i
                else: self.destIndex = i
        
    def ReadFile2(self, file):
        verticesTMP = []
        with open(file, 'r') as fp:
            for line in fp:
                verticesTMP.extend(list(line.strip()))
            self.n = len(line.strip())
        n = self.n
        verticesTMP = list(map(int, verticesTMP))
        vertices2 = dict()
        for i, ver in enumerate(verticesTMP):
            vertices2[i] = dict()
            if i < n*n-n:
                down = (i+n, verticesTMP[i+n])
                vertices2[i][i+n] = verticesTMP[i+n]
            else:
                down = None

            if i >= n:
                up = (i-n, verticesTMP[i-n])
                vertices2[i][i-n] = verticesTMP[i-n]
            else: up = None
            if i%n==0: left = None
            else:
                left = (i-1, verticesTMP[i-1])
                vertices2[i][i-1] = verticesTMP[i-1]
            if i%n==(n-1): right =None
            else:
                right = (i+1, verticesTMP[i+1])
                vertices2[i][i+1] = verticesTMP[i+1]
            self.vertices.append(Vertice(up, down, left, right, ver))
            if ver == 0:
                if self.startIndex is None: self.startIndex = i
                else: self.destIndex = i
        self.justVertices = verticesTMP
        self.vertices = vertices2

            
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

        board[self.startIndex] = '0'
        board[self.destIndex] = '0'

        current_vertex_index = vertex_table[self.destIndex][1]
        while current_vertex_index != self.startIndex:
            board[current_vertex_index] = str(self.vertices[current_vertex_index].cost)
            current_vertex_index = vertex_table[current_vertex_index][1]
        
        y = 0
        for i in range(len(board)):
            if (i+1)%self.n==0:
                board.insert(i+y+1, "\n")
                y += 1

        return visited, "".join(board)



    def FindShortestPath2(self, start, dest):
        distances = {vertex: [sys.maxsize, 0] for vertex in self.vertices}
        distances[start] = [0,0]

        queue = [(0, start)]
        while queue: 
            curDistance, curVertex = heappop(queue)
            if curDistance > distances[curVertex][0]:
                continue
            if curVertex == dest: #jeśli szukamy z dokładnego end to start to wydajniej jest odkomentować tą część
                break
            for neighbor, cost in self.vertices[curVertex].items():
                distance = curDistance + cost
                if distance < distances[neighbor][0]:
                    distances[neighbor] = [distance, curVertex]
                    heappush(queue, (distance, neighbor))
        path = []
        while dest != start:
            path.append(dest)
            dest = distances[dest][1]
        path.append(start)
        return path

    def PrintGraph(self):
        dis = self.FindShortestPath2(self.startIndex, self.destIndex)
        for i in range(self.n*self.n):
            if i%self.n == 0:
                print()
            if i in dis:
                print(self.justVertices[i], end ='')
            else:
                print('.', end='')
        print()

    # def printNormal(self):
    #     for i in range(self.n*self.n):
    #         if i%self.n == 0:
    #             print()
    #         print(self.justVertices[i], end='')
    #     print()

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
        self.cost : int = cost

