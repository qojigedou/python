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
############ Przykład: Merge Sort #########
algorytm = "Merge"

def mergesort(tab):
    t0 = time.perf_counter()
    width = 1
    n = len(tab)
    while (width < n):
        left=0
        while (left < n):
            right = min(left+(width*2-1), n-1)
            m = min(left+width-1,n-1)

            n1 = m - left + 1
            n2 = right - m
            L = [0] * n1
            R = [0] * n2
            for i in range(0, n1):
                L[i] = tab[left + i]
            for i in range(0, n2):
                R[i] = tab[m + i + 1]
            i, j, k = 0, 0, left
            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    tab[k] = L[i]
                    i += 1
                else:
                    tab[k] = R[j]
                    j += 1
                k += 1
            while i < n1:
                tab[k] = L[i]
                i += 1
                k += 1
            while j < n2:
                tab[k] = R[j]
                j += 1
                k += 1
            left += width*2
        width *= 2
    delta_t = time.perf_counter() - t0
    return delta_t



    
###############################################
###############################################
print(f"Sortowanie: {algorytm}")
delta_t = mergesort(tablica)
print(f"R: Tablica posortowana w czasie {delta_t*1000:.1f} ms. Liczba operacji: {len(tablica.pelne_kopie):.0f}.")


delta_t = mergesort(tablica1)
print(f"S: Tablica posortowana w czasie {delta_t*1000:.1f} ms. Liczba operacji: {len(tablica1.pelne_kopie):.0f}.")

delta_t = mergesort(tablica2)
print(f"A: Tablica posortowana w czasie {delta_t*1000:.1f} ms. Liczba operacji: {len(tablica2.pelne_kopie):.0f}.")

delta_t = mergesort(tablica3)
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