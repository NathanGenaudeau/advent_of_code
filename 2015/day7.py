import sys

def AND(a, b):
  return a & b

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
wires = {}

lines = open(sys.argv[1]).readlines()
for line in lines:
    [left_side, right_side] = line.replace('\n', '').split(' -> ')
    
    if (right_side not in wires):
        if (isInt(left_side)):
            wires[right_side] = int(left_side)
        else:
            wires[right_side] = 'xxx'

x = 0

while wires['a'] == 'xxx':
  line = lines[x]
  [left_side, right_side] = line.replace('\n', '').split(' -> ')
  left = ''
  operator = ''
  right = ''
  if (len(left_side.split(' ')) == 3):
    [left, operator, right] = left_side.split(' ')

    if ((isInt(left) or wires[left] != 'xxx') and (isInt(right) or wires[right] != 'xxx')):
      if (operator == 'AND'):
        wires[right_side] = int(left) & wires[right] if isInt(left) else wires[left] & wires[right]
      elif (operator == 'OR'):
        wires[right_side] = wires[left] | wires[right]
      elif (operator == 'RSHIFT'):
        wires[right_side] = wires[left] >> int(right)
      elif (operator == 'LSHIFT'):
        wires[right_side] = wires[left] << int(right)
      else:
        wires[right_side] = wires[left]

  elif (len(left_side.split(' ')) == 2):
    [operator, right] = left_side.split(' ')
    if (isInt(right) or wires[right] != 'xxx'):
      wires[right_side] = ~wires[right]
  else:
    if (not isInt(left_side) and wires[left_side] != 'xxx'):
      wires[right_side] = wires[left_side]

  x = (x + 1) % len(lines)

print(wires['a'])
