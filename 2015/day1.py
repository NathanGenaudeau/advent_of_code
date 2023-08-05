import sys

data = open(sys.argv[1]).read()

floor = 0
for char in data:
	if (char == '('):
		floor += 1
	elif (char == ')'):
		floor -= 1
print(floor)