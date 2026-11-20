def graph_cycle_detector(graph: dict[int, list[int]]) -> bool:
    en_cours = set()
    termine = set()

    def dfs(noeud):
        if noeud in en_cours:
            return True
        if noeud in termine:
            return False

        en_cours.add(noeud)
        for voisin in graph.get(noeud, []):
            if dfs(voisin):
                return True
        en_cours.remove(noeud)
        termine.add(noeud)
        return False

    for noeud in graph:
        if dfs(noeud):
            return True
    return False


if __name__ == "__main__":
    assert graph_cycle_detector({0: [1], 1: [2], 2: [0]}) is True
    assert graph_cycle_detector({0: [1], 1: [2], 2: []}) is False
    assert graph_cycle_detector({0: [1, 2], 1: [3], 2: [3], 3: []}) is False
    assert graph_cycle_detector({0: [0]}) is True
    assert graph_cycle_detector({}) is False
    assert graph_cycle_detector({0: [1], 1: [2], 2: [3], 3: [1]}) is True
    assert graph_cycle_detector({0: [], 1: [], 2: []}) is False
    print("py_graph_cycle_detector : OK")
