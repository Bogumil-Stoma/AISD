from find_path import Graph

elo = Graph()
elo.ReadFile('plansza.txt')
visited, board = elo.FindPath()
print(board)

elo = Graph()
elo.ReadFile('plansza1.txt')
visited, board = elo.FindPath()
print(board)

elo = Graph()
elo.ReadFile('plansza2.txt')
visited, board = elo.FindPath()
print(board)

elo = Graph()
elo.ReadFile('plansza3.txt')
visited, board = elo.FindPath()
print(board)

elo = Graph()
elo.ReadFile('plansza5.txt')
visited, board = elo.FindPath()
print(board)