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