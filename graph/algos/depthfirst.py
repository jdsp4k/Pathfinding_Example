from graph.graph import Graph
from graph.pathdoesnotexisterror import PathDoesNotExistError

def depthFirst(g : Graph,
               start : str,
               target : str,
               currentPath : list[str] = [],
               visited : set[str] = set()):
    if start == target:
        currentPath.append(start)
        return currentPath
    else:
        nextStep = ""
        visited.add(start)
        for i in g.citiesList[start][0]:
            if not i in visited:
                nextStep = i
                break

        if nextStep != "":
            currentPath.append(start)
            return depthFirst(g, nextStep, target, currentPath, visited)
        else:
            if len(currentPath) < 2:
                errorText = "No path found between " + currentPath[0] + " and " + target
                raise PathDoesNotExistError(currentPath[0], target)
            else:
                return depthFirst(g, currentPath[-1], target, currentPath[:-1], visited)