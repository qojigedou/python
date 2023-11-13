# Narysować odwrócony pusty trójkąt z gwiazdek o zadanej długości nieparzystej,

rows = int(input("Enter number of rows: "))

for i in range(rows):
	for j in range(i):
		print(" ", end="")
	for k in range(2*(rows-i)-1):
		if k==0 or k==2*(rows-i-1) or i==0:
			print("*", end="")
		else:
			print(" ", end="")
	print()
