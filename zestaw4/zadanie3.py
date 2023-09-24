# podpunkt A) 
# zdefiniować w ramach klasy A funkcję foo(self, x), metodę klasy class_foo, metodę statyczną static_foo, 
# tak, żeby kod poniżej drukował treści jak w komentarzach

class A(object):
    def __init__(self):
        self.foo = self.__inst_foo
        self.class_foo = self.__inst_class_foo
        self.static_foo = self.__inst_static_foo

    def __inst_foo(self, x):
        print("wykonanie foo(", self, ", ", x, ")", sep="")
    def foo(self, x):
        print("ditto")

    @classmethod
    def __inst_class_foo(self,x):
        print("class foo(", self, ", ", x, ")", sep="")
    @classmethod
    def class_foo(self, x):
        print("ditto")
    @staticmethod
    def __inst_static_foo(x):
        print("wykonanie foo(", x, ")", sep="")
    @staticmethod
    def static_foo(x):
        print("ditto")



# podpunkt B)
# zdefiniować dowolną klasę bazową dziedzicząca z ABC i posiadającą metodę abstrakcyjną
# po czym zdefiniować ze dwie klasy potomne z odpowiednimi definicjami, zademonstrować w działaniu
from abc import ABC, abstractmethod

class MyABC(ABC):
    @abstractmethod
    def __iter__(self):
        pass

    def  get_iter(self):
        return self.__iter__()

class inher_MyABC1(MyABC):
    def __iter__(self):
        print("inherit class 1 __iter__")

    def get_iter(self):
        return self.__iter__()

class inher_MyABC2(MyABC):
    def __iter__(self):
        print("inherit class 2 __iter__")

    def get_iter(self):
        return self.__iter__()

# podpunkt C
# zdefiniować dowolną klasę oraz atrybut klasy tak, że stanie się on atrybutem czytanym poprzez 
# dekorator @property, a ustawianym za pomocą @nazwa.setter, pokazać w działaniu

class Kwadrat:
    def __init__(self, value):
        self._x = value

    @property
    def x(self):
        print("Wczytaj bok kwadrata")
        return self._x
    
    @x.setter
    def x(self, value):
        print("Ustaw bok kwadrata")
        self._x = value

    @x.deleter
    def x(self):
        print("Usun bok kwadrata")
        del self._x

def main():
    print("podpunkt A: \n")
    a = A()
    a.foo(123) # wykonanie foo(<__main__.A object at 0x0000023A680D1F10>, 123)
    A.foo(a,123) # ditto
    a.class_foo(123) # class_foo(<class '__main__.A'>, 123)
    A.class_foo(123) # ditto
    a.static_foo(123) # wykonanie static_foo(123)
    A.static_foo(123) # ditto

    print("podpunkt B: \n")
    inh = inher_MyABC1()
    inh.get_iter()

    inh2 = inher_MyABC2()
    inh2.get_iter()

    print("podpunkt C: \n")
    kwadr = Kwadrat(2)
    print(kwadr.x)

    kwadr.x = 12

    del kwadr.x

if __name__ == "__main__":
    main()