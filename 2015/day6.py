import math
import sys

lines = open(sys.argv[1]).readlines()

matrix = [0] * 1000000

def splitLine(line, word):
	num1X = int(line.split(word)[1].split(' ')[0].split(',')[0])
	num1Y = int(line.split(word)[1].split(' ')[0].split(',')[1])
	num2X = int(line.split('through ')[1].split(',')[0])
	num2Y = int(line.split('through ')[1].split(',')[1])
	return [num1X, num1Y, num2X, num2Y]

for line in lines:
	if ('turn on ' in line):
		[num1X, num1Y, num2X, num2Y] = splitLine(line, 'turn on ')
		for i in range(num1X, num2X + 1):
			for j in range(num1Y, num2Y + 1):
				matrix[i * int(math.sqrt(len(matrix))) + j] = 1
	elif ('turn off' in line):
		[num1X, num1Y, num2X, num2Y] = splitLine(line, 'turn off ')
		for i in range(num1X, num2X + 1):
			for j in range(num1Y, num2Y + 1):
				matrix[i * int(math.sqrt(len(matrix))) + j] = 0
	elif ('toggle' in line):
		[num1X, num1Y, num2X, num2Y] = splitLine(line, 'toggle ')
		for i in range(num1X, num2X + 1):
			for j in range(num1Y, num2Y + 1):
				num = i * int(math.sqrt(len(matrix))) + j
				matrix[num] = 0 if matrix[num] == 1 else 1

print(sum(matrix))