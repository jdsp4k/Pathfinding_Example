from graph.graph import Graph
from graph.pathdoesnotexisterror import PathDoesNotExistError

def bestFirst(
        g : Graph,
        start : str,
        target : str,
        path : list[str] = [],
        visited : set[str] = set()):
    if start == target:
        return path + [start]
    else:
        visited.add(start)
        nextStep = ""
        cities = g.citiesList[start][0]
        cities.sort(key = lambda x : g.getPythagDistance(x, target))
        for i in cities:
            if i not in visited:
                nextStep = i
                break
        
        if nextStep == "":
            if len(path) == 1:
                raise PathDoesNotExistError(path[0], target)
            else:
                return bestFirst(g, path[-1], target, path[:-1], visited)
        else:
            path.append(start)
            return bestFirst(g, nextStep, target, path, visited)