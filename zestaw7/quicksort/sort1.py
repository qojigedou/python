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
############ Przykład: Quick Sort #########
def partition(arr,start_ind,end_ind):
    i = ( start_ind - 1 )   
    x = arr[end_ind]

    for j in range(start_ind , end_ind):
        if arr[j] <= x:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[end_ind] = arr[end_ind],arr[i+1]
    return (i+1)

algorytm = "Quick"

def quicksort(arr):
    start_ind = 0
    end_ind = len(arr)-1
    t0 = time.perf_counter()
    size = end_ind - start_ind + 1
    stack = [0] * (size)
    top = -1

    top = top + 1
    stack[top] = start_ind
    top = top + 1
    stack[top] = end_ind

    while top >= 0: 
        end_ind = stack[top]
        top = top - 1
        start_ind = stack[top]
        top = top - 1

        
        i = ( start_ind - 1 )   
        x = arr[end_ind]

        for j in range(start_ind , end_ind):
            if arr[j] <= x:
                i = i+1
                arr[i],arr[j] = arr[j],arr[i]

        arr[i+1],arr[end_ind] = arr[end_ind],arr[i+1]
        p = i+1

        if p-1 > start_ind:
            top = top + 1
            stack[top] = start_ind
            top = top + 1
            stack[top] = p - 1
        if p+1 < end_ind:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = end_ind
    delta_t = time.perf_counter() - t0
    return delta_t
###############################################
###############################################
print(f"Sortowanie: {algorytm}")
delta_t = quicksort(tablica)
print(f"R: Tablica posortowana w czasie {delta_t*1000:.1f} ms. Liczba operacji: {len(tablica.pelne_kopie):.0f}.")


delta_t = quicksort(tablica1)
print(f"S: Tablica posortowana w czasie {delta_t*1000:.1f} ms. Liczba operacji: {len(tablica1.pelne_kopie):.0f}.")

delta_t = quicksort(tablica2)
print(f"A: Tablica posortowana w czasie {delta_t*1000:.1f} ms. Liczba operacji: {len(tablica2.pelne_kopie):.0f}.")

delta_t = quicksort(tablica3)
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