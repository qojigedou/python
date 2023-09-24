import time
from mtablica import MonitorowanaTablica
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 50  # liczba elementów, można zmieniać
FPS = 60  # klatki na sekundę do parametru interval 

tablica = MonitorowanaTablica(0, 1000, N, "R") # zbadaj też opcje: "S", "A", "T"
tablica1 = MonitorowanaTablica(0, 1000, N, "S")
tablica2 = MonitorowanaTablica(0, 1000, N, "A")
tablica3 = MonitorowanaTablica(0, 1000, N, "T")
###############################################
############ Przykład: Tim Sort #########
algorytm = "Tim"

MINIMUM= 32
def find_minrun(n): 
    r = 0
    while n >= MINIMUM: 
        r |= n & 1
        n >>= 1
    return n + r 

def insertion_sort(array, left, right): 
    for i in range(left+1,right+1):
        element = array[i]
        j = i-1
        while element<array[j] and j>=left :
            array[j+1] = array[j]
            j -= 1
        array[j+1] = element
    return array

def merge(array, l, m, r): 
    array_length1= m - l + 1
    array_length2 = r - m 
    left = []
    right = []
    for i in range(0, array_length1): 
        left.append(array[l + i]) 
    for i in range(0, array_length2): 
        right.append(array[m + 1 + i]) 
    i=0
    j=0
    k=l
    while j < array_length2 and  i < array_length1: 
        if left[i] <= right[j]: 
            array[k] = left[i] 
            i += 1
        else: 
            array[k] = right[j] 
            j += 1
        k += 1

    while i < array_length1: 
        array[k] = left[i] 
        k += 1
        i += 1
    while j < array_length2: 
        array[k] = right[j] 
        k += 1
        j += 1

def timsort(array): 
    t0 = time.perf_counter()
    n = len(array) 
    minrun = find_minrun(n) 

    for start in range(0, n, minrun): 
        end = min(start + minrun - 1, n - 1) 
        insertion_sort(array, start, end) 
    size = minrun 
    while size < n: 
        for left in range(0, n, 2 * size): 
            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 
            merge(array, left, mid, right) 
        size = 2 * size 
    delta_t = time.perf_counter() - t0
    return delta_t
###############################################
###############################################
print(f"Sortowanie: {algorytm}")
delta_t = timsort(tablica)
print(f"R: Tablica posortowana w czasie {delta_t*1000:.1f} ms. Liczba operacji: {len(tablica.pelne_kopie):.0f}.")

delta_t = timsort(tablica1)
print(f"S: Tablica posortowana w czasie {delta_t*1000:.1f} ms. Liczba operacji: {len(tablica1.pelne_kopie):.0f}.")

delta_t = timsort(tablica2)
print(f"A: Tablica posortowana w czasie {delta_t*1000:.1f} ms. Liczba operacji: {len(tablica2.pelne_kopie):.0f}.")

delta_t = timsort(tablica3)
print(f"T: Tablica posortowana w czasie {delta_t*1000:.1f} ms. Liczba operacji: {len(tablica3.pelne_kopie):.0f}.")
###############################################

# konfiguracja wyświetlania histogramu
plt.rcParams["font.size"] = 16
fig, ax = plt.subplots(figsize=(16, 8))
container = ax.bar(np.arange(0, len(tablica), 1), tablica.pelne_kopie[0], align="edge", width=0.8)
fig.suptitle(f"Sortowanie: {algorytm}")
ax.set(xlabel="Indeks", ylabel="Wartość")
ax.set_xlim([0, N])
txt = ax.text(0.01, 0.99, "", ha="left", va="top", transform=ax.transAxes)

# funkcja aktualizująca stan poszczególnych klatek do wyświetlenia
def update(frame):
    txt.set_text(f"Liczba operacji = {frame}")
    for rectangle, height in zip(container.patches, tablica.pelne_kopie[frame]):
        rectangle.set_height(height)
        rectangle.set_color("darkblue")

    idx, op = tablica.aktywnosc(frame)
    if op == "get":
        container.patches[idx].set_color("green")
    elif op == "set":
        container.patches[idx].set_color("red")

    return (txt, *container)

# tu akumulowana jest animacja, wyświetlna komendą show
ani = FuncAnimation(fig, update, frames=range(len(tablica.pelne_kopie)), blit=True, interval=1000./FPS, repeat=False)
plt.show()