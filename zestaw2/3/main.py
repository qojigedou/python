# Dla dowolnego podanego łańcucha znakowego wypisać:

#     ile jest w nim słów (poprzez słowo rozumiemy ciąg co najmniej jednego 
#znaku innego niż znak przestankowy, dla uproszczenia przyjmijmy, 
#że liczymy a-z, A-Z i 0-9 jako coś, co składa się na słowa)
#     ile liter
#     ile cyfr
#     wypisać statystykę częstości występowania poszczególnych liter oraz cyfr


from collections import Counter
print("Entetr a string")
str = input()

num = 0
ch = 0
 
word_list = str.split()

word = len(word_list)
num = sum(c.isdigit() for c in str)
ch = sum(i.isalpha() for i in str)

print(f"Words in string: {word} , characters in string: {ch} , numbers in string: {num}\n")

print("\n")

collection = Counter(str)
print(f"The count of occurences of characters in a string: {collection} \n")