from graph.graph import Graph
from graph.pathdoesnotexisterror import PathDoesNotExistError

def breadthFirst(g : Graph,
                 start : str,
                 target : str):
    q : list[tuple[str, list]] = []
    q = [(start, [start])]
    visited = set()
    while q:
        city, path = q.pop(0)
        visited.add(city)
        for node in g.citiesList[city][0]:
            if node == target:
                return path + [target]
            else:
                if node not in visited:
                    visited.add(city)
                    q.append((node, path + [node]))
    
    raise PathDoesNotExistError(start, target)