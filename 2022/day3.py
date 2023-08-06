import sys

items = open(sys.argv[1]).readlines()

total = 0
for item in items:
	if item != '' :
		a = item[0:len(item)//2]
		b = item[len(item)//2:]
		commonItem = list(set(a).intersection(set(b)))[0]
		number = ord(commonItem) - 38 if commonItem.isupper() else ord(commonItem) - 96
		total += number
print(total)