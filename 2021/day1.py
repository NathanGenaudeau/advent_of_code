import sys

depths = open(sys.argv[1]).readlines()

count = 0
for i in range(len(depths)):
	if (i > 0 and depths[i] != '' and int(depths[i]) > int(depths[i-1])):
		count += 1
print(count)