from cmath import sqrt

class Graph():
    def __init__(self, lineList):
        self.citiesList : dict[str, tuple[list, tuple[float, float] | None]] = {}
        for line in lineList:
            line = line.split()
            self.addConnection(*line)

    def addConnection(self, *args):
        try:
            try:
                self.citiesList[args[0]][0].index(args[1])
            except ValueError as e:
                self.citiesList[args[0]][0].append(args[1])
                self.citiesList[args[0]][0].sort()
        except KeyError as e:
            self.citiesList[args[0]] = ([args[1]], (None, None))
        
        try:
            try:
                self.citiesList[args[1].upper()][0].index(args[0])
            except ValueError as e:
                self.citiesList[args[1].upper()][0].append(args[0])
                self.citiesList[args[1].upper()][0].sort()
        except KeyError as e:
            self.citiesList[args[1]] = ([args[0]], (None, None))

    def setLocation(self, city : str, loc : tuple[float, float]):
        f = self.citiesList.get(city, None)
        if f is None:
            raise KeyError
        else:
            self.citiesList[city] = (self.citiesList[city][0], loc)

    def getPythagDistance(self, start : str, target : str):
        try:
            lat = (self.citiesList[start][1][0] - self.citiesList[target][1][0]) ** 2
            lng = (self.citiesList[start][1][1] - self.citiesList[target][1][1]) ** 2
            return sqrt(lat + lng).real
        except TypeError as e:
            #If we try to do a distance calculation with a node which has no coords, return infinity
            return float('inf')
            
    
    def __str__(self):
        out = ""
        for key in self.citiesList:
            out += f"{key:14s} \t({self.citiesList[key][1][0]:03.7f}, {self.citiesList[key][1][1]: 3.7f}) \t"
            for con in self.citiesList[key][0]:
                out += con + " "
            out += "\n"
        return out