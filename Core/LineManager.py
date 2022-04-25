from AttractionDataTypes import Attraction, AttractionSeats, Line
import LineManagerUtils

class LineManager:
  selectedAttraction: Attraction
  currentSeats: AttractionSeats
  waitingLine: Line

  def __init__(self, selectedAttraction: Attraction) -> None:
    self.selectedAttraction = selectedAttraction
    self.waitingLine = Line()
    self.currentSeats = AttractionSeats(selectedAttraction)

  def CanAddExpressGroup(self) -> bool:
    return self.currentSeats.GetLineTypesPercentage()[0] < 65 and len(self.waitingLine.expressLine) != 0

  def CanAddRegularGroup(self) -> bool:
    return len(self.waitingLine.regularLine) != 0

  def CanAddSingleLiner(self) -> bool:
    return self.waitingLine.singleRiderLine != 0

  def FillAttraction(self) -> None:
    for _ in range(self.selectedAttraction.attractionRows):
      row = []
      waitingOtherGroups: bool = False
      shouldAddSingleLiner: bool = False

      while not self.currentSeats.IsRowFull(row) and not self.waitingLine.IsEmpty():
        if self.CanAddExpressGroup() and not waitingOtherGroups:
          if self.currentSeats.CanAddThisGroupToRow(self.waitingLine.expressLine[0], row):
            LineManagerUtils.AddExpressGroupToRow(self.waitingLine.expressLine[0], row)
            self.waitingLine.MoveExpressGroup()
          else:
            try:
              nextGroup = self.waitingLine.expressLine[1]
            except:
              nextGroup = 0
            if self.currentSeats.CanAddThisGroupToRow(nextGroup, row):
              LineManagerUtils.AddExpressGroupToRow(self.waitingLine.expressLine[1], row)
              self.waitingLine.MoveExpressGroup(1)
            else:
              waitingOtherGroups = True
        elif self.CanAddRegularGroup() and not shouldAddSingleLiner:
          if self.currentSeats.CanAddThisGroupToRow(self.waitingLine.regularLine[0], row):
            LineManagerUtils.AddRegularGroupToRow(self.waitingLine.regularLine[0], row)
            self.waitingLine.MoveRegularGroup()
          else:
            try:
              nextGroup = self.waitingLine.regularLine[1]
            except:
              nextGroup = 0
            if self.currentSeats.CanAddThisGroupToRow(nextGroup, row):
              LineManagerUtils.AddRegularGroupToRow(nextGroup, row)
              self.waitingLine.MoveRegularGroup(1)
            else:
              shouldAddSingleLiner = True
        else:
          if self.CanAddSingleLiner():
            LineManagerUtils.AddSingleRiderToRow(row)
            self.waitingLine.MoveSingleRiderGroup()
          else:
              break
      if len(row) != 0:
        self.currentSeats.AddRow(row)
  
  def PrintAttraction(self, cartNumber: int):
    print('Cart: ' + str(cartNumber))
    for row in self.currentSeats.seatsMatrix:
      print(row)

  def RunAttraction(self):
    self.currentSeats.seatsMatrix = []

  def IsEmpty(self) -> bool:
    return self.waitingLine.IsEmpty()
