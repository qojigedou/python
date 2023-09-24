print("Enter the decimal number :")
n = int(input())

def fun(n):
    binary = bin(n)[2:].strip('0').split('1')
    return max([len(x) for x in binary])
print("The biggest binary gap is", fun(n), end="\n")    
