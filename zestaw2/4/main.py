# Mamy trzy liczby całkowite, x, y, z reprezentujące wymiary prostopadłościanu, 
# oraz pewną liczbę naturalną n. Wypisz listę wszystkich możliwych współrzędnych (i, j, k) 
# na trójwymiarowej siatce, gdzie i + j + k nie jest równe n. 
# Warunki: 0 ≤ i ≤ x, 0 ≤ j ≤ y, 0 ≤ k ≤ z.

# Rozwiązanie zapisz w postaci list składanych (list comprehesion), ale można 
# zacząć od zagnieżdżonych pętli.
# Przykład

# Niech x = 1, y = 1, z = 2, n = 3.

# Lista wszystkich permutacji trójek [i, j, k] w tym przykładzie:

# [[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [0,1,2], [1,0,0], [1,0,1], [1,0,2], [1,1,0], [1,1,1], [1,1,2]]

# Elementy, które nie sumują się do 3 to:

# [[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,2]]

# Parametry x, y, z, n wczytać na początku za pomocą funkcji input().


x, y, z, n = int(input("Enter x: ")), int(input("Enter y: ")), int(input("Enter z: ")), int(input("Enter n: "))

combinations = []

def makeZ(z):
    result = [a for a in range(z+1)]
    return result

def makeY(y, z):
    result = []
    for j in range(y+1):
        result += [[j, a] for a in makeZ(z)]
    return result

def makeX(x, y, z):
    result = []
    for i in range(x+1):
        result += [[i, a[0], a[1]] for a in makeY(y, z)]
    return result

combinations = makeX(x, y, z)

for i in combinations:
    if (i[0]+i[1]+i[2]) != n:
        print(i)