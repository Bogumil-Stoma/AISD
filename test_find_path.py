from find_path import Graph, Vertice

def test_find_path_traversal():
    elo = Graph()
    elo.ReadFile('plansza.txt')
    assert elo.startIndex==7
    assert elo.destIndex==26
    visited, path = elo.FindPath()
    assert(len(visited)==36)
    for i in range(36):
        assert(i in visited)
    expected_path = "_111__\n_0_1__\n___11_\n____1_\n__0_1_\n__111_\n"
    assert(path == expected_path)
    
