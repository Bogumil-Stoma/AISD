from copy import deepcopy
import heapq

class Graph:
    def __init__(self):
        self.n: int = 0
        self.vertices: list[Vertice] = []
        self.justVertices = []
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
            self.vertices.append(Vertice(up, down, left, right))
            if ver == 0:
                if self.startIndex is None: self.startIndex = i
                else: self.destIndex = i
        self.justVertices = verticesTMP
        self.vertices = vertices2

    def FindPath(self, src):
        # visited : list[int] = []
        # unvisited : list[int] = [i for i in range(len(self.vertices))]
        # #  to_visit_queue : list[int] = []
        # vertex_table = [[None, None] for _ in self.vertices]
        # # print(vertex_table)
        # # current_vertex : Vertice = self.vertices[self.startIndex]
        # # vertex_table[self.startIndex][0] = 0
        # # if current_vertex.up is not None:
        # #     vertex_table[current_vertex.up[0]][0] = current_vertex.up[1]
        # #     vertex_table[current_vertex.up[0]][1] = self.startIndex
        # #     # to_visit_queue.insert(0, current_vertex.up[0])

        # # if current_vertex.down is not None:
        # #     vertex_table[current_vertex.down[0]][0] = current_vertex.down[1]
        # #     vertex_table[current_vertex.down[0]][1] = self.startIndex
        # #     # to_visit_queue.insert(0, current_vertex.down[0])

        # # if current_vertex.left is not None:
        # #     vertex_table[current_vertex.left[0]][0] = current_vertex.left[1]
        # #     vertex_table[current_vertex.left[0]][1] = self.startIndex
        # #     # to_visit_queue.insert(0, current_vertex.left[0])

        # # if current_vertex.right is not None:
        # #     vertex_table[current_vertex.right[0]][0] = current_vertex.right[1]
        # #     vertex_table[current_vertex.right[0]][1] = self.startIndex
        #     # to_visit_queue.insert(0, current_vertex.right[0])

        # # visited.append(self.startIndex)
        # # unvisited.remove(self.startIndex)

        # vertex_table[self.startIndex][0] = 0

        # # prev_vertex_index = self.startIndex
        # current_vertex = self.startIndex
        # while unvisited:
        #     # current_vertex = None

        #     for vertex in unvisited:
        #         if vertex_table[vertex][0] is not None:
        #             if vertex_table[current_vertex][0] is not None:
        #                 if vertex_table[vertex][0] < vertex_table[current_vertex][0]:
        #                     current_vertex = vertex

        #     if self.vertices[current_vertex].up is not None:
        #         if vertex_table[self.vertices[current_vertex].up[0]][0] is not None:
        #             a = vertex_table[self.vertices[current_vertex].up[0]][0] + self.vertices[current_vertex].up[1]
        #             if a < vertex_table[self.vertices[current_vertex].up[0]][0]:
        #                 vertex_table[self.vertices[current_vertex].up[0]][0] = a
        #                 vertex_table[self.vertices[current_vertex].up[0]][1] = current_vertex
        #             else:
        #                 vertex_table[self.vertices[current_vertex].up[0]][0] = self.vertices[current_vertex].up[1]
        #                 vertex_table[self.vertices[current_vertex].up[0]][1] = current_vertex

        #     if self.vertices[current_vertex].down is not None:
        #         if vertex_table[self.vertices[current_vertex].down[0]][0] is not None:
        #             a = vertex_table[self.vertices[current_vertex].down[0]][0] + self.vertices[current_vertex].down[1]
        #             if a < vertex_table[self.vertices[current_vertex].down[0]][0]:
        #                 vertex_table[self.vertices[current_vertex].down[0]][0] = a
        #                 vertex_table[self.vertices[current_vertex].down[0]][1] = current_vertex
        #         else:
        #             vertex_table[self.vertices[current_vertex].down[0]][0] = self.vertices[current_vertex].down[1]
        #             vertex_table[self.vertices[current_vertex].down[0]][1] = current_vertex


        #     if self.vertices[current_vertex].left is not None:
        #         if vertex_table[self.vertices[current_vertex].left[0]][0] is not None:
        #             a = vertex_table[self.vertices[current_vertex].left[0]][0] + self.vertices[current_vertex].left[1]
        #             if a < vertex_table[self.vertices[current_vertex].left[0]][0]:
        #                 vertex_table[self.vertices[current_vertex].left[0]][0] = a
        #                 vertex_table[self.vertices[current_vertex].left[0]][1] = current_vertex
        #             else:
        #                 vertex_table[self.vertices[current_vertex].left[0]][0] = self.vertices[current_vertex].left[1]
        #                 vertex_table[self.vertices[current_vertex].left[0]][1] = current_vertex

        #     if self.vertices[current_vertex].right is not None:
        #         if vertex_table[self.vertices[current_vertex].right[0]][0] is not None:
        #             a = vertex_table[self.vertices[current_vertex].right[0]][0] + self.vertices[current_vertex].right[1]
        #             if a < vertex_table[self.vertices[current_vertex].right[0]][0]:
        #                 vertex_table[self.vertices[current_vertex].right[0]][0] = a
        #                 vertex_table[self.vertices[current_vertex].right[0]][1] = current_vertex
        #             else:
        #                 vertex_table[self.vertices[current_vertex].right[0]][0] = self.vertices[current_vertex].right[1]
        #                 vertex_table[self.vertices[current_vertex].right[0]][1] = current_vertex





        #     # current_vertex = self.vertices[current_vertex_index]
        #     # if current_vertex.up is not None:
        #     #     if vertex_table[current_vertex.up[0]][0] is not None:
        #     #         a = vertex_table[current_vertex.up[0]][0] + current_vertex.up[1]
        #     #         if a < vertex_table[current_vertex.up[0]][0]:
        #     #             vertex_table[current_vertex.up[0]][0] = a
        #     #             vertex_table[current_vertex.up[0]][1] = current_vertex_index
        #     #     else:
        #     #         vertex_table[current_vertex.up[0]][0] = current_vertex.up[1]
        #     #         vertex_table[current_vertex.up[0]][1] = current_vertex_index

        #     #     if current_vertex.up[0] not in to_visit_queue+visited: to_visit_queue.insert(0, current_vertex.up[0])

        #     # if current_vertex.down is not None:
        #     #     if vertex_table[current_vertex.down[0]][0] is not None:
        #     #         a = vertex_table[current_vertex.down[0]][0] + current_vertex.down[1]
        #     #         if a < vertex_table[current_vertex.down[0]][0]:
        #     #             vertex_table[current_vertex.down[0]][0] = a
        #     #             vertex_table[current_vertex.down[0]][1] = current_vertex_index
        #     #     else:
        #     #         vertex_table[current_vertex.down[0]][0] = current_vertex.down[1]
        #     #         vertex_table[current_vertex.down[0]][1] = current_vertex_index

        #     #     if current_vertex.down[0] not in to_visit_queue+visited: to_visit_queue.insert(0, current_vertex.down[0])

        #     # if current_vertex.left is not None:
        #     #     if vertex_table[current_vertex.left[0]][0] is not None:
        #     #         a = vertex_table[current_vertex.left[0]][0] + current_vertex.left[1]
        #     #         if a < vertex_table[current_vertex.left[0]][0]:
        #     #             vertex_table[current_vertex.left[0]][0] = a
        #     #             vertex_table[current_vertex.left[0]][1] = current_vertex_index
        #     #     else:
        #     #         vertex_table[current_vertex.left[0]][0] = current_vertex.left[1]
        #     #         vertex_table[current_vertex.left[0]][1] = current_vertex_index

        #     #     if current_vertex.left[0] not in to_visit_queue+visited: to_visit_queue.insert(0, current_vertex.left[0])

        #     # if current_vertex.right is not None:
        #     #     if vertex_table[current_vertex.right[0]][0] is not None:
        #     #         a = vertex_table[current_vertex.right[0]][0] + current_vertex.right[1]
        #     #         if a < vertex_table[current_vertex.right[0]][0]:
        #     #             vertex_table[current_vertex.right[0]][0] = a
        #     #             vertex_table[current_vertex.right[0]][1] = current_vertex_index
        #     #     else:
        #     #         vertex_table[current_vertex.right[0]][0] = current_vertex.right[1]
        #     #         vertex_table[current_vertex.right[0]][1] = current_vertex_index

        #     #     if current_vertex.right[0] not in to_visit_queue+visited: to_visit_queue.insert(0, current_vertex.right[0])


        #     visited.append(current_vertex)
        #     unvisited.remove(current_vertex)

        # print(visited)
        # for i in range(len(vertex_table)):
        #     print(vertex_table[i], end='')
        #     if (i+1)%6==0:
        #         print()
        # return(visited)
        pass


    def FindShortesPath2(self, start, end):
        distances = {vertex: [float('infinity'),0] for vertex in self.vertices}
        distances[start] = [0,0]

        queue = [(0, start)]
        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            if current_distance > distances[current_vertex][0]:
                continue
            if current_vertex == end:
                break
            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor][0]:
                    distances[neighbor] = [distance, current_vertex]
                    #bruv[current_vertex].append(neighbor)
                    heapq.heappush(queue, (distance, neighbor))
        path = []
        while end != start:
            path.append(end)
            end = distances[end][1]
        path.append(start)
        return path[::-1]

    def PrintGraph(self):
        dis = self.FindShortesPath2(self.startIndex, self.destIndex)
        for i in range(self.n*self.n):
            if i%self.n == 0:
                print()
            if i in dis:
                print(self.justVertices[i], end ='')
            else:
                print('X', end='')
class Vertice:
    '''
    Stores vertice with possible connections, where connection(eg. up) is in form (INDEX, COST)
    '''
    def __init__(self, up, down,
                  left, right):
        self.up: tuple[int,int] = up
        self.down: tuple[int,int] = down
        self.left: tuple[int,int] = left
        self.right: tuple[int,int] = right

elo = Graph()
elo.ReadFile('plansza.txt')
elo.PrintGraph()
elo = Graph()
elo.ReadFile('plansza2.txt')
elo.PrintGraph()
elo = Graph()
elo.ReadFile('plansza3.txt')
elo.PrintGraph()
print()
print(':)')
