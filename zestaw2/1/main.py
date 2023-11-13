# Mamy zagnieżdżoną listę, na przykład:

# list1 = [1, 2, [3, 4, [5, 6], 5], 3, [4, 5]]

# Dodaj element o kolejnej wartości w najbardziej zagnieżdżonej liście. 
#W tym przypadku 7 w miejscu:

# [1, 2, [3, 4, [5, 6, 7], 5], 3, [4, 5]]

# Napisz program, który zrobi to uniwersalnie, dla dowolnego zagnieżdżenia.
# Przykłady

# [1, [2, 3] 4] => [1, [2, 3, 4] 4]
 
# [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7] => [3, 4, [2, [1, 2, [7, 8, 9], 3, 4], 3, 4], 5, 6, 7]

# Jeżeli największe zagnieżdżenie na danym poziomie się powtórzy, 
#należy dodać w obu zagnieżdżeniach, czyli:

# [1, [3], [2]] => [1, [3, 4], [2, 3]]




list1 = [3, 4,[2, [1, 2, [7, 8], 3, 4],3, 4], 5, 6, 7]
print("list1:", list1)
dictionary = {}

def depth(lista, level):
    if level not in dictionary:
        dictionary[level] = []
    dictionary[level].append(lista)

    if not isinstance(lista, list):
        return
    for i in lista:
        depth(i, level + 1)


depth(list1, 0)

is_list = False

for i in range(max(dictionary.keys()), -1, -1):
    if is_list:
        break
    for j in dictionary[i]:
        if isinstance(j, list):
            is_list = True
            j.append(j[len(j)-1]+1)

print("modified list1:", list1)
