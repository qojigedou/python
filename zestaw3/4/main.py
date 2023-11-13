# Rekurencyjne liczenie ciągu Fibonacciego jest naturalnym algorytmem, niemniej, 
# wyliczanie każdego kolejnego wyrazu ciągu „od początku” jest niepotrzebne. 
# O wiele wydajniejszą metodą byłoby zastosowanie czegoś w rodzaju buforu 
# – pamięci podręcznej, w której zapamiętywalibyśmy poprzednio (wcześniej) 
# wyliczone wyrazy i z nich korzystali. Znacząco przyspieszy to obliczenia.

# Proszę napisać (uzupełnić poniższy szkielet) kod tak, żeby powstawał 
# słownik – pamięć podręczna z poprzednimi wyliczonymi wartościami i z 
# nich korzystać, a wyliczać nowe tylko gdy jeszcze nie były policzone 
# wcześniej. Słownik proszę zrobić w dekoratorze.

import functools

def pamiec(func):
    dictionary = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not args[0] in dictionary:
            dictionary[args[0]] = func(args[0])

        return dictionary[args[0]]


    return wrapper

@pamiec
def fibonacci(n):
    return n if 0 <= n < 2 else fibonacci(n - 1) + fibonacci(n - 2)

for i in range(100):
    print(fibonacci(i))