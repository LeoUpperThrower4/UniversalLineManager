import sys

sys.path.insert(0, './Utils')
sys.path.insert(0, './Core')

import AttractionUtils
from LineManager import LineManager

# Business Rules
## carts have to be as full as possible
## express has priority
## every run must have at least 35% of people from regular line 
## only 1 group deep will be looked
## single riders fill empty spaces
## it was considered only groups that could fill rows. Example: if an attraction has 3 rows, there will be only groups of, at most, 3 people

if __name__ == '__main__':
  # Attraction Setup
  try:
    selectedAttraction = AttractionUtils.GetAttraction('Hulk')
  except Exception as Ex: # TODO: Criar exception exclusiva
    print('Attraction Not Found')
    exit

  lineManager = LineManager(selectedAttraction)

  cartNumber = 0

  while not lineManager.IsEmpty():
    cartNumber += 1
    lineManager.FillAttraction()
    print('------' + selectedAttraction.attractionName + '------')
    lineManager.PrintAttraction(cartNumber)
    lineManager.RunAttraction()