from AttractionDataTypes import Attraction

def FindAttractionInDB(name: str) -> str:
  with open('Attractions/Attractions.txt') as attractionStr:
    for line in attractionStr.readlines():
      attractionRows, attractionSeats, attractionName = line.split(',')
      if attractionName.strip().lower() == name.strip().lower():
        return Attraction(attractionName.strip(),int(attractionRows),int(attractionSeats))
    raise Exception('Attraction Not Found')

def GetAttraction(name: str) -> Attraction:
  return FindAttractionInDB(name)