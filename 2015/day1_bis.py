import sys

data = open(sys.argv[1]).read()

floor = 0
position = 0
for char in data:
	position += 1
	if (char == '('):
		floor += 1
	elif (char == ')' and floor != 0):
		floor -= 1
	else:
		print(position)
		break
	