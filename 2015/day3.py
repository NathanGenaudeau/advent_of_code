import sys

lines = open(sys.argv[1]).readlines()

position = 0
houses = [0]

for char in lines[0]:
	if (char == '<'):
		position = position - 1
	elif (char == '>'):
		position = position + 1
	elif (char == '^'):
		position = position - 1000
	elif (char == 'v'):
		position = position + 1000
	if (not position in houses):
		houses.append(position)
print(len(houses))