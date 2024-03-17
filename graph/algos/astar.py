from graph.graph import Graph
from graph.pathdoesnotexisterror import PathDoesNotExistError

def __pathReconstruction(cameFrom : dict[str, float], current : str):
    totalPath = [current]
    while current in cameFrom:
        current = cameFrom[current]
        totalPath.append(current)
    totalPath.reverse()
    return totalPath
        
def aStar(
        g : Graph,
        start : str,
        target : str):
    openSet : list[str] = [start]
    cameFrom : dict[str, str] = {}
    gScore : dict[str, float] = {start: 0}
    fScore : list[tuple[float, str]] = [(g.getPythagDistance(start, target), start)]

    while len(openSet) > 0:
        openF = filter(lambda x : x[1] in openSet, fScore)
        current = next(openF)[1]

        if current == target:
            return __pathReconstruction(cameFrom, current)
        openSet.remove(current)
        for i in g.citiesList[current][0]:
            tentativeGScore = gScore[current] + g.getPythagDistance(current, i)
            if i not in gScore or tentativeGScore < gScore[i]:
                gScore[i] = tentativeGScore
                cameFrom[i] = current
                gScore[i] = tentativeGScore
                fScore.append((tentativeGScore + g.getPythagDistance(i, target), i))
                fScore.sort()
                if i not in openSet:
                    openSet.append(i)

    raise PathDoesNotExistError(start, target)