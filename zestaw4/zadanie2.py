from math import hypot, atan, sin, cos, sqrt

class Zespolona:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def conjugate(self):
        return self.__class__(self.r, -self.i)

    def argz(self):
        return atan(self.i / self.r)

        
    def __abs__(self):
        return (sqrt(self.r**2+self.i**2))

    def __repr__(self):
        return "Zespolona(" + str(self.r) + ", " + str(self.i) + ")"

    def __str__(self):
        if(self.i > 0):
            znak = "+"
        else:
            znak = ""
        return "(" + str(self.r) + znak + str(self.i) + "j)"

    def __add__(self, other):
        if isinstance(other, int):
            return self.__class__(self.r + other, self.i)
        if isinstance(other, float):
            return self.__class__(self.r + other, self.i)
        else:
            return self.__class__(self.r + other.r, self.i + other.i)
        
    def __sub__(self, other):
        if isinstance(other, int):
            return self.__class__(self.r - other, self.i)
        if isinstance(other, float):
            return self.__class__(self.r - other, self.i)
        else:
            return self.__class__(self.r - other.r, self.i - other.i)

    def __mul__(self, other):
        if isinstance(other, int):
            return self.__class__(self.r * other, self.i * other)
        if isinstance(other, float):
            return self.__class__(self.r * other, self.i * other)
        else:
            return self.__class__(self.r * other.r - self.i * other.i, self.r*other.i + self.i * other.r)

    def __radd__(self, other):
        if isinstance(other, int):
            return self.__class__(other + self.r, self.i)
        if isinstance(other, float):
            return self.__class__(other + self.r, self.i)
        else:
            return self.__class__(other.r + self.r, other.i + self.i)

    def __rmul__(self, other):
        if isinstance(other, int):
            return self.__class__(other * self.r, other * self.i)
        if isinstance(other, float):
            return self.__class__(other *self.r , other*self.i) 
        else:
            return self.__class__(other.r * self.r - other.i * self.i, other.r*self.i + other.i * self.r)

    def __rsub__(self, other):
        if isinstance(other, int):
            return self.__class__(other - self.r, -self.i)
        if isinstance(other, float):
            return self.__class__(other - self.r, -self.i)
        else:
            return self.__class__(other.r - self.r, other.i - self.i)


    def __eq__(self, other):
        return (self.r == other.r and other.i == self.i)

    def __ne__(self, other):
        return (self.r != other.r or self.i != other.i)

    def __pow__(self, other):
        r = sqrt(self.i**2 + self.r**2)
        return self.__class__(round(r**other*cos(other*self.argz())),round(r**other*sin(other*self.argz())))


def main():
    print("Liczby zespolone")
    a = Zespolona(2, 5)
    b = Zespolona(1, -3)
    print(a)
    print(b)
    b_copy = eval(repr(b))
    print(type(b_copy), b_copy.r, b_copy.i)
    print(a + b)
    print(a - b)
    print(a + 4)
    print(7 - a)
    print(a * 4)
    print(a * (-4))
    print(a == Zespolona(2, 5))
    print(a ==  b)
    print(a != b)
    print(a != Zespolona(2, 5))
    print(a ** 2)
    print(b ** 4)


if __name__ == "__main__":
    main()


# Liczby zespolone
# (2+5j)
# (1-3j)
# <class '__main__.Zespolona'> 1 -3
# (3+2j)
# (1+8j)
# (6+5j)
# (5-5j)
# (8+20j)
# (-8-20j)
# True
# False
# True
# False
# (-21+20j)
# (28+96j)