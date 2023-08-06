import hashlib

start = 'ckczppom'
number = 1

while True:
	char = start + str(number)
	md5 = hashlib.md5(char.encode('utf-8')).hexdigest()
	if (md5[:5] == '00000'):
		print(number)
		break
	number += 1