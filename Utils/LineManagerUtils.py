def AddExpressGroupToRow(expressGroup: int, row: list) -> list:
  for _ in range(expressGroup):
    row.append('X')
  return row

def AddRegularGroupToRow(regularGroup: int, row: list) -> list:
  for _ in range(regularGroup):
    row.append('R')
  return row

def AddSingleRiderToRow(row: list) -> list:
  row.append('S')
  return row