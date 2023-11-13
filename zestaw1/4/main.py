#Napisać program rysujący prostokąt zbudowany z małych kratek. 
#Należy zbudować pełny string, a potem go wypisać.


print("Enter the wigth of the rectange: ")
rect_width = int(input())

print("Entetr the length of hte rectangle: ")
rect_length = int(input())

string = "+"+"---+"*(rect_width)
string += "\n"
for i in range(rect_length):
	string += "|"+ "   |"*(rect_width)+"\n"
	string += "+"+"---+"*(rect_width)+"\n"

print(string)
