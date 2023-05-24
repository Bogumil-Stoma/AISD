from find_path import Graph, Vertice

def test_find_path_traversal():
    elo = Graph()
    elo.ReadFile('plansza.txt')
    assert elo.startIndex==7
    assert elo.destIndex==
    path = elo.FindPath(4)
    assert(len(path)==36)
    for i in range(36):
        assert(i in path)
    print(':)')
