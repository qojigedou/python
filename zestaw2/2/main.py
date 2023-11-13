# Napisać program, który będzie wyświetlał bieżący czas aktualizowany dynamicznie.

# Tak ma to wyglądać:

# ►      14:48:31      ◄

# Czas można odczytać na wiele sposobów, użyjmy moduł datetime, wtedy, 
# bieżący punkt w czasie dostaniemy: now = datetime.now() i za pomocą 
# składowych now.hour, now.minute, now.second mamy potrzebne wartości. 
# Przy czym dla sekund należy sprytnie podmienić sekundy w zakresie 0..9 tak, 
# żeby przed nimi wyświetlało się zero (np. nie 5, tylko 05).

# Znaczki na początku i końcu mają kod chr(16) i chr(17).

# Zegar musi być wyświetlany w nieskończonej pętli funkcją print(), 
# argument end='\r' zapewni nadpisywanie.

# Potrzebne jest jeszcze (z modułu time) wołanie czegoś typu time.sleep(0.5) 
# w pętli, żeby niepotrzebnie nie odświeżać zbyt często bieżącego odczytu czasu.

from datetime import datetime
import time


while True:
    now = datetime.now()
    second = str(now.second)
    hour = str(now.hour)
    minute = str(now.minute)
    if(len(hour) == 1):
        hour = "0" + hour
    if len(minute) == 1:
        minute = "0" + minute
    if len(second) == 1:
        second = "0" + second
    print("► ", hour, ":", minute, ":", second," ◄" , sep = "", end='\r')

    time.sleep(0.5)