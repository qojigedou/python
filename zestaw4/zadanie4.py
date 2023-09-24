from functools import singledispatch, singledispatchmethod
@singledispatch
def fun(arg):
    print(arg)

@fun.register
def _(arg: str):
    print("String")

@fun.register
def _(arg: int):
    print("Integer")

class PowerOf:
    @singledispatchmethod
    def power(self, arg):
        raise NotImplementedError("Error")

    @power.register
    def _(self, arg:int):
        return arg*2

    @power.register
    def _(self, arg:str):
        return arg+arg


def main():
    print("4 is an", end=" ")
    fun(4)
    print("hello is a", end=" ")
    fun("hello")
    a = PowerOf()
    print("4*2:", a.power(4))
    
    b = PowerOf()
    print("la 2 times:", b.power("la"))
    


if __name__ == "__main__":
    main()
    
