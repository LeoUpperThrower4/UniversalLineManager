class Attraction:
    attractionName = "Default"
    attractionRows = -1
    attractionSeats = -1
    attractionSeatsPerRow = -1

    def __init__(self, attractionName: int, attractionRows: int, attractionSeats: int) -> None:
        self.attractionName = attractionName
        self.attractionRows = attractionRows
        self.attractionSeats = attractionSeats
        self.attractionSeatsPerRow = attractionSeats / attractionRows

class AttractionSeats:
    attraction: Attraction
    seatsMatrix = list[list]
    expressLineCount, regularLineCount, singleLineCount = 0, 0, 0

    def __init__(self, attraction) -> None:
        self.attraction = attraction
        self.seatsMatrix = []

    def AddRow(self, row: list):
        self.seatsMatrix.append(row)

    def IsRowFull(self, row: list):
        return len(row) == self.attraction.attractionSeatsPerRow

    def GetExpressPercentage(self) -> int:
        expressCount = 0
        for row in self.seatsMatrix:
            for seat in row:
                if seat == 'X':
                    expressCount += 1
        return int(expressCount * 100 / self.attraction.attractionSeats)

    def GetRegularPercentage(self):
        regularCount = 0
        for row in self.seatsMatrix:
            for seat in row:
                if seat == 'R':
                    regularCount += 1

        return int(regularCount * 100 / self.attraction.attractionSeats)

    def GetSinglePercentage(self):
        singleCount = 0
        for row in self.seatsMatrix:
            for seat in row:
                if seat == 'S':
                    singleCount += 1

        return int(singleCount * 100 / self.attraction.attractionSeats)

    def CanAddThisGroupToRow(self, group: int, row: list) -> bool:
        availableSeatsInRow = self.attraction.attractionSeatsPerRow - len(row)
        if group <= availableSeatsInRow and group != 0:
            return True
        return False

    def GetLineTypesPercentage(self) -> list:
        expressPercentage = self.GetExpressPercentage()
        regularPercentage = self.GetRegularPercentage()
        singlePercentage = self.GetSinglePercentage()
        return [expressPercentage, regularPercentage, singlePercentage]

class Line:
    # Waiting Line Setup
    ## each value of the list represents a group of people
    regularLine = []  # represented as R
    expressLine = []  # represented as X
    singleRiderLine = 0  # total number of single riders, represented as S

    def __init__(self) -> None:
        self.regularLine = [2, 3, 4, 3, 2, 2, 2, 3, 4, 4, 2, 3, 4, 3]
        self.expressLine = [2, 4, 3, 2, 3, 4]
        self.singleRiderLine = 15

    def MoveExpressGroup(self, depth: int = 0) -> None:
        newExpressLine: list = self.expressLine[0:depth]
        newExpressLine += self.expressLine[depth + 1:]
        self.expressLine = newExpressLine

    def MoveRegularGroup(self, depth: int = 0) -> None:
        newRegularLine: list = self.regularLine[0:depth]
        newRegularLine += self.regularLine[depth + 1:]
        self.regularLine = newRegularLine
        
    def MoveSingleRiderGroup(self) -> None:
        self.singleRiderLine -= 1

    def IsEmpty(self) -> bool:
        return (
            (len(self.regularLine) == 0)
            and (len(self.expressLine) == 0)
            and (self.singleRiderLine == 0)
        )
