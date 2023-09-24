from fractions import Fraction
from functools import reduce
from math import prod
from functools import reduce

def product(fracs):
    t = reduce(lambda a, b: a*b, fracs)
    return t.numerator, t.denominator

if __name__ == 'main':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)