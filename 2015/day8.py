import sys

lines = open(sys.argv[1]).readlines()

nbCharacStringLiteralTotal = 0
nbCharacValueStringTotal = 0

for line in lines:
  line = line.replace('\n', '')
  nbCharacStringLiteral = 0
  nbCharacValueString = 0

  i = 0
  while i < len(line):
    if (line[i] == '"'):
      nbCharacStringLiteral += 1
    elif (line[i] == "\\"):
      if (line[i+1] == '"'):
        nbCharacStringLiteral += 2
        nbCharacValueString += 1
        i += 1
      elif (line[i+1] == '\\'):
        nbCharacStringLiteral += 2
        nbCharacValueString += 1
        i += 1
      elif (line[i+1] == 'x'):
        nbCharacStringLiteral += 4
        nbCharacValueString += 1
        i += 3
    else:
      nbCharacStringLiteral += 1
      nbCharacValueString += 1
    i += 1
  nbCharacStringLiteralTotal += nbCharacStringLiteral
  nbCharacValueStringTotal += nbCharacValueString
print(nbCharacStringLiteralTotal - nbCharacValueStringTotal)
    
