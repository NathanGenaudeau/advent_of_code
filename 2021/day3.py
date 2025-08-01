import sys

binaries = open(sys.argv[1]).readlines()

gamma = ''
epsilon = ''
for i in range(len(binaries[0])):
	byte = ''
	for binary in binaries:
		if (binary != ''):
			byte += binary[i]
	if (byte.count('1') > byte.count('0')):
		gamma += '1'
		epsilon += '0'
	elif (byte.count('0') > byte.count('1')):
		gamma += '0'
		epsilon += '1'
print(int(gamma, 2) * int(epsilon, 2))
