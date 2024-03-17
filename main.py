import os
import random
import time

from graph.graph import Graph
from graph.pathdoesnotexisterror import PathDoesNotExistError
from graph.algos.depthfirst import depthFirst
from graph.algos.breadthfirst import breadthFirst
from graph.algos.iddfs import iddfs
from graph.algos.bestfirst import bestFirst
from graph.algos.astar import aStar

ADJ_FILENAME = os.path.join("res", "Adjacencies.txt")
COORD_FILENAME = os.path.join("res", "coordinates.csv")
ALGOS = {"DEPTH FIRST" : depthFirst, "BREADTH FIRST" : breadthFirst, "ID-DFS" : iddfs, "BEST FIRST" : bestFirst, "A*" : aStar}

def load(adj : str = ADJ_FILENAME, coord : str = COORD_FILENAME) -> Graph:
    with open(adj) as file:
        lines = []
        for line in file.readlines():
            lines.append(line.upper())

    with open(coord) as file:
        coords = []
        for line in file.readlines():
            coords.append(line.upper())

    g = Graph(lines)

    for coord in coords:
        c = coord.split(",")
        g.setLocation(c[0], (float(c[1]), float(c[2])))
    
    return g

print(f"Loading {ADJ_FILENAME}, {COORD_FILENAME}...")
g = load()

print("Graph loaded!")
print(g)

running = True

while running:
    hasAlgo = False
    while hasAlgo == False:
        print("Enter search algorithm or \"Q\" to quit")
        algoStr = ""
        for a in ALGOS:
            algoStr += a + ", "
        algoStr = algoStr[:-2]
        print(algoStr)
        algo = input(">").upper().split(",")
        hasAlgo = False
        if len(algo[0]) == 0:
            algo = list(ALGOS.keys())
            hasAlgo = True
        elif algo[0][0] == "Q":
            quit(0)
        else:
            try:
                algoCallable = []
                lastA = ""
                for a in algo:
                    lastA = a
            except KeyError as e:
                print(f"{lastA} is not a valid algorithm.")
            else:
                hasAlgo = True

    start = input("Enter starting node (enter for random node): ")
    target = input("Enter target notde (enter for random node): ") 

    if start == "":
        start = random.choice(list(g.citiesList.keys()))
    if target == "":
        target = random.choice(list(g.citiesList.keys()))

    start = start.upper()
    target = target.upper()
    
    if start in list(g.citiesList.keys()) and target in list(g.citiesList.keys()):
            
        print(f"\nTesting {start} to {target} using {", ".join(str(a) for a in algo)}:")
        for a in algo:
            try:
                start_time = time.time_ns()
                res = ALGOS[a](g, start, target)
                end_time = time.time_ns()
                elapsed = (end_time - start_time) / 1000
                print(f"{a} @ {elapsed:2.2f}Ms: {res}")
            except PathDoesNotExistError as e:
                print(a + ": " + str(e))
        print()
        
    else:
        if start not in list(g.citiesList.keys()):
            city = start
        else:
            city = target
        print(f"{city} is not a valid node name.\n")