from itertools import product

k, m = map(int, input().split())
values = []

for _ in range(k):
    row = list(map(int, input().split()[1:]))
    values.append(list(map(lambda x:x**2, row)))
print(max(map(lambda x: sum(x)%m, product(*values))))