#Pathfinding Example
This is an example implementation of several pathfinding algorithms in Python. These implementaions produce a path from any given undirected graph with included coordinates. They are cycle and disconnect tolerant, and deterministic.

##Usage
Run `main.py`
The script will load the graph from `res/Adjacencies.txt` and the coordinates from `res/coordinates.csv`.
You may enter none to many algorithms from the presented list. If no algorithms are entered, it will run all algorithms.

##Algorithms

###Depth First
Searches the graph by following a path to it's end. In this case, because this is an undirected graph, there is no inherent order to child nodes; however in order to guaruntee determinism, they are prioritized in alphabetical order.

###Breadth First
Searches the graph by searching each node at an incrementally increasing distance from the start node. Guaurnteed to return a depth-optimal route. 

###ID-DFS
A depth first search executed to an incrementally increasing distance from the start node.

###Best First
A best first search is a heuristically driven search which will favor the best candidate out of all child nodes. In this implementation, the heuristic algorithm is the pythagorean distance from the target node.

###A*
A* is a heuristically driven search which will favor the best candidate out of all available nodes. It differs from a pure best-first because it also accounts for the cost from the start node. In this implementation, the heuristic algorithim is the pythagorean distance from the target node.

##Liscence
Copyright (C) 2024 by Jacob Smith <jdsp4k@umsystem.edu>

Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.