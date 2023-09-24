from collections import Counter
print("Entetr a string")
str = input()

num = 0
ch = 0
 
word_list = str.split()

word = len(word_list)
num = sum(c.isdigit() for c in str)
ch = sum(i.isalpha() for i in str)

print("Words in string:", word, ",", "characters in string:", ch, ",", "numbers in string:", num, end="\n")

print("\n")

collection = Counter(str)
print("The count of occurences of characters in a string:", collection, end="\n")