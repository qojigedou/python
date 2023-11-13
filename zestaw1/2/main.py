#Napisać program, który czyta podane jako zewnętrzne argumenty liczby naturalne, 
#a następnie każdą rozkłada na czynniki pierwsze (co polega na zapisaniu dowolnej 
#liczby naturalnej za pomocą iloczynu liczb pierwszych). 
#Wymagany jest format wyjściowy w postaci a1^k1*a2^k2*...*a3, jeśli ki==1 to opuszczamy 
#wykładnik potęgi.

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




