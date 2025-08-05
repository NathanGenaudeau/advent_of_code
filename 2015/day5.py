import sys

lines = open(sys.argv[1]).readlines()

number = 0

for line in lines:
	vowels = 0
	letterFollow = False
	containsPattern = False

	for i in range(0, len(line)):
		if (line[i] in 'aeiou'):
			vowels += 1
	for i in range(0, len(line) - 1):
		if (line[i] == line[i+1]):
			letterFollow = True
	
	if ('ab' in line or 'cd' in line or 'pq' in line or 'xy' in line):
		containsPattern = True
		
	if (vowels >= 3 and letterFollow and not containsPattern) :
		number += 1
print(number)