#Napisać program, który czyta podane jako zewnętrzne argumenty liczby naturalne, 
#a następnie każdą rozkłada na czynniki pierwsze (co polega na zapisaniu dowolnej 
#liczby naturalnej za pomocą iloczynu liczb pierwszych). 
#Wymagany jest format wyjściowy w postaci a1^k1*a2^k2*...*a3, jeśli ki==1 to opuszczamy 
#wykładnik potęgi.


import sys
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def factorize(num):
    if is_prime(num):
        return str(num)
    
    factors = []
    k = 2
    pierw = int(math.sqrt(num))
    
    while num > 1 and k <= pierw:
        count = 0
        while num % k == 0:
            count += 1
            num //= k
        if count != 0:
            factors.append((k, count))
        k += 1
    
    if num > 1:
        factors.append((num, 1))
    
    return factors

def format_output(factors):
    result = ""
    for factor, count in factors:
        result += str(factor)
        if count > 1:
            result += "^" + str(count)
        result += '*'
    return result[:-1]

def main():
    argv = sys.argv[1:]
    
    for arg in argv:
        num = int(arg)
        factors = factorize(num)
        result = format_output(factors)
        print(f"{num} = {result}")

if __name__ == "__main__":
    main()
