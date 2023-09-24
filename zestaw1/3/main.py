ruler_length = int(input("Enter the lenght of the ruler: "))

string = "|"
for i in range(ruler_length):
	string += "....|"
string += "\n"
string += "0"
for i in range(1, ruler_length+1):
	string += " "*(5-len(str(i)))+str(i)
print(string)
