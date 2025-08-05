import sys

lines = open(sys.argv[1]).readlines()

number = 0

for line in lines:
	pattern = False
	letterBetween = False

	for i in range(0, len(line) - 1):
		substring = line[i:i+2]
		for j in range(i+2, len(line) - 1):
			if (substring == line[j:j+2]):
				pattern = True

	for i in range(0, len(line) - 2):
		if (line[i] == line[i+2]):
			letterBetween = True
		
	if (pattern and letterBetween):
		number += 1
print(number)