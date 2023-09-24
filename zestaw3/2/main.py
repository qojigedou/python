
def intToRoman(num: int) -> str:
        integers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        romanLetters =["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        result = ""
        roman = []
        for i in range(len(integers)):
            while(num >= integers[i]):
                num = num - integers[i]
                roman.append(romanLetters[i])
                s = ''.join(roman)
        return s

n = int(input())
print("Roman representation:", intToRoman(n), end="\n")