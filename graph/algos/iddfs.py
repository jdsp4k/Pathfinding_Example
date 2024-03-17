from graph.graph import Graph
from graph.pathdoesnotexisterror import PathDoesNotExistError

def __backtrace(previous : dict[str, str], current : str):
    path = [current]
    while current in previous:
        current = previous[current]
        path.append(current)
    path.reverse()
    return path

def iddfs(
        g : Graph,
        start : str,
        target : str,
        maxDepth : int = 0):
    
    stack : list[tuple[str, int]]= [(start, 0)]
    previous = {}
    visited = set()

    while len(stack) > 0:
        current, depth = stack.pop(0)
        if current == target:
            return __backtrace(previous, current)
        else:
            visited.add(current)
            for i in g.citiesList[current][0]:
                if i not in stack and i not in visited and depth + 1 <= maxDepth:
                    stack.append((i, depth + 1))
                    previous[i] = current

    if maxDepth >= len(g.citiesList):
        #Obvously no connected node can be farther away then the length of the graph so...
        #If the depth is larger than the length of the graph then something has gone wrong
        raise PathDoesNotExistError(start, target)
    else:
        return iddfs(g, start, target, maxDepth + 1)


    if root == "":
        root = start
    if start == target:
        return path + [start]
    else:
        nextStep = ""
        visited.add(start)
        for i in g.citiesList[start][0]:
            if i not in visited:
                nextStep = i
                break
        
        if nextStep == "":
            if depth != 0:
                return iddfs(g, path[-1], target, path[:-1], visited, depth - 1, maxD, root)
            else:
                if len(visited) == len(g.citiesList):
                    raise PathDoesNotExistError(root, target)
                else:
                    return iddfs(g, root, target, maxD = maxD + 1, root = root)
        else:
            if depth <= maxD:
                return iddfs(g, nextStep, target, path + [start], visited, depth + 1, maxD, root)
            else:
                return iddfs(g, path[-1], target, path[:-1], visited, depth - 1, maxD, root)