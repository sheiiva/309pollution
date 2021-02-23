############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#           Project : 309pollution         #
#                                          #
############################################

from math import factorial

from sources.utils import isInt


class Pollution():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._n = 0
        self._x = 0
        self._y = 0
        self._fileContent = None

    def parse(self, args: list) -> None:

        def getContent(filename: str) -> None:
            with open(filename, 'r') as f:
                return [elem.replace('\n', '') for elem in f.readlines()]

        self._n = int(args[1])
        self._fileContent = getContent(args[2])
        self._x = float(args[3])
        self._y = float(args[4])

    def checkFile(self) -> int:

        def checkElems(elems: list) -> int:
            for elem in elems:
                if not isInt(elem):
                    return 84

        fileContent = []

        for line in self._fileContent:
            elems = line.split(';')
            if len(elems) != 3 or checkElems(elems) == 84:
                print("ERROR - Wrong file format.")
                return 84
            fileContent.append([int(elem) for elem in elems])

        self._fileContent = fileContent

    def createMap(self, size: int) -> list:

        m = [[0 for _ in range(size)] for _ in range(size)]

        # Set with coordinates from file's content
        for coords in self._fileContent:
            m[coords[0]][coords[1]] = coords[2]

        return m

    def compute(self, map: list) -> float:

        def coefficientBinomial(n: float, k: float) -> float:
            return factorial(n) / (factorial(k) * factorial(n - k))

        def bezier(n: float, coords: float, k: float) -> float:
            return pow(coords/n, k) * pow(1 - (coords/n), n-k)

        pollution = 0

        for i in range(self._n):
            for j in range(self._n):
                pollution += coefficientBinomial(self._n-1, i) * coefficientBinomial(self._n-1, j)\
                                * bezier(self._n-1, self._x, i) * bezier(self._n-1, self._y, j) * map[i][j]

        return pollution

    def run(self, args: list) -> None:

        """
        Run computations and process output printing.
        """

        # Parse input arguments
        self.parse(args)
        # Check input file validity
        if self.checkFile() == 84:
            exit(84)
        # Set map for computation
        map = self.createMap(self._n)
        # Process output computing
        pollution = self.compute(map)
        # Print output result
        print('{:.2f}'.format(pollution))
