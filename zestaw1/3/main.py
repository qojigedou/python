#Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć liczby 
#składające się z kilku cyfr (ostatnia cyfra liczby ma znajdować 
#się pod znakiem kreski pionowej). Należy zbudować pełny string, a potem go wypisać.

ruler_length = int(input("Enter the lenght of the ruler: "))

string = "|"
for i in range(ruler_length):
	string += "....|"
string += "\n"
string += "0"
for i in range(1, ruler_length+1):
	string += " "*(5-len(str(i)))+str(i)
print(string)
