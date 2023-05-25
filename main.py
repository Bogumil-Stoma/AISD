from find_path import Graph
import gc
import time

def measure_time1(graph):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    a = graph.FindPath()
    stop = time.process_time()
    if gc_old: gc.enable()
    return stop-start, *a

def measure_time2(graph):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    a = graph.FindShortestPath2(graph.startIndex, graph.destIndex)
    stop = time.process_time()
    if gc_old: gc.enable()
    return stop-start



print("Measuring without queue")
elo = Graph()
elo.ReadFile1('plansza.txt')
my_time, visited, board = measure_time1(elo)
print("Time: ", my_time)
print(board)

print("Measuring with queue")
elo = Graph()
elo.ReadFile2('plansza.txt')
my_time = measure_time2(elo)
print("Time: ", my_time)
elo.PrintGraph()

print("Measuring without queue")
elo = Graph()
elo.ReadFile1('plansza1.txt')
my_time, visited, board = measure_time1(elo)
print("Time: ", my_time)
print(board)

print("Measuring with queue")
elo = Graph()
elo.ReadFile2('plansza1.txt')
my_time = measure_time2(elo)
print("Time: " , my_time)
elo.PrintGraph()

print("Measuring without queue")
elo = Graph()
elo.ReadFile1('plansza2.txt')
my_time, visited, board = measure_time1(elo)
print("Time: " , my_time)
print(board)

print("Measuring with queue")
elo = Graph()
elo.ReadFile2('plansza2.txt')
my_time = measure_time2(elo)
print("Time: " , my_time)
elo.PrintGraph()

print("Measuring without queue")
elo = Graph()
elo.ReadFile1('plansza3.txt')
my_time, visited, board = measure_time1(elo)
print("Time: " , my_time)
print(board)

print("Measuring with queue")
elo = Graph()
elo.ReadFile2('plansza3.txt')
my_time = measure_time2(elo)
print("Time: " , my_time)
elo.PrintGraph()

print("Measuring without queue")
elo = Graph()
elo.ReadFile1('plansza5.txt')
my_time, visited, board = measure_time1(elo)
print("Time: " , my_time)
print(board)

print("Measuring with queue")
elo = Graph()
elo.ReadFile2('plansza5.txt')
my_time = measure_time2(elo)
print("Time: " , my_time)
elo.PrintGraph()