def odwracanie(L, left, right):
    for i in range((right-left)//2 + 1):
        temp = L[right - i]
        L[right - i] = L[left + i]
        L[left + i] = temp

L = []
for i in range(10):
    L.append(i)

print(L)
odwracanie(L, 4, 8)
print("Odwrocony iteracyjnie L z 4 po 8 element: ", L)


def odwracanie_rek(L, left, right):
    if(left >= right):
        return 
    temp = L[right]
    L[right] = L[left]
    L[left] = temp
    odwracanie_rek(L, left + 1, right - 1)

L1 = []
for i in range(10):
    L1.append(i)

print(L1)
odwracanie_rek(L1, 4, 8)
print("Odwrocony rekurencyjnie L z 4 po 8 element: ", L)
