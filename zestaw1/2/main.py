import sys
import math

argv = sys.argv[1:]

for i in argv:
	#print(int(i))
	i = int(i)
	k = 2
	pierw = math.sqrt(i)
	string = ""
	while i > 1 and k <= pierw:
		count = 0
		while i % k == 0:
			count += 1
			i//=k
		if count != 0:
			string += str(k)
			if count > 1:
				string += "^" + str(count)
			string += '*'
		k = k + 1
	if i>1:
		string += str(i)+"*"
	print(i, "=", string[:-1])




