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
