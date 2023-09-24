uppercase = []
lowercase = []
oddDigits = []
evenDigits = []
s = str(input())
for i in sorted(s):
    if i.isalpha():
        if i.isupper():
            symbol = uppercase
        else:
            symbol = lowercase
    elif i.isdigit():
        if int(i)%2==0 :
            symbol = evenDigits
        else:
            symbol = oddDigits
    symbol.append(i)

print("".join(lowercase+uppercase+oddDigits+evenDigits))