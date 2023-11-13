# W pliku tramwaje.json znajdują się dane z numerami linii tramwajowych w Krakowie oraz przystanków, przez które przejeżdża dany tramwaj. W języku Python, czytanie danych w formatach .json czy .csv jest wykonywane z pomocą modułów. W naszym przypadku:

# import json
# with open('tramwaje.json', "r", encoding='utf-8') as read_file:
#     data = json.load(read_file)

# Wczytane dane (zróbmy print) są złożone z nadmiernie zagnieżdżonych 
# typów: słownika, listy, słownika, listy:

# {
#     'linia': [{
#         'name': '1', 'przystanek': [
#             {'name': 'Wzgórza Krzesławickie 01'},
#             {'name': 'Jarzębiny 02'}
#             …

# Zatem, przykładowo, żeby odczytać pierwszy przystanek dla linii 1, 
# trzeba wywołać w konsoli:

# data["linia"][0]["przystanek"][0]["name"]

# żeby zobaczyć nazwę 'Wzgórza Krzesławickie 01'.

# Należy przepisać dane do uproszczonego formatu typu słownik, 
# którego kluczem będzie numer linii tramwajowej (zapisany jako int), 
# a wartością krotka zawierająca wszystkie nazwy przystanków danej linii.

#     Uwaga: technicznie przystanki oprócz nazw mają też numery, proszę 
#     uprościć dane, zapisując wyłącznie nazwy przystanków bez końcowych 
#     numerów (01, 02…).

# Przykładowo, dla linii nr 1 spodziewany format danych wygląda następująco:

# {
#     1: ('Wzgórza Krzesławickie', 'Jarzębiny', 'Darwina', 'Wiadukty', 'Elektromontaż', 'Zajezdnia Nowa Huta', 'Kombinat', 'Struga', 'Plac Centralny im. R.Reagana', 'Os. Kolorowe', 'Rondo Czyżyńskie', 'Centralna', 'Rondo 308. Dywizjonu', 'M1 al. Pokoju', 'TAURON Arena Kraków al. Pokoju', 'Plaza', 'Dąbie', 'Ofiar Dąbia', 'Fabryczna', 'Francesco Nullo', 'Teatr Variété', 'Rondo Grzegórzeckie', 'Hala Targowa', 'Starowiślna', 'Poczta Główna', 'Plac Wszystkich Świętych', 'Filharmonia', 'Jubilat', 'Komorowskiego', 'Salwator')
# }

# Proszę wynik konwersji zapisać do pliku wyjściowego (również w formacie .json), 
# np. w ten sposób:

# with open('tramwaje_out.json', 'w', encoding='utf-8') as file:
#     json.dump(trams, file, ensure_ascii=False)

# W przykładzie założono, że słownik jest pod nazwą trams.

# Ponadto, proszę wypisać na ekranie następujące informacje: numer linii 
# – liczba przystanków, posortowane po liczbie przystanków w kolejności 
# malejącej. Na koniec wypisać również liczbę wszystkich przystanków 
# obsługiwanych przez tramwaje (w tym celu należy oczywiście znaleźć 
# część wspólną krotek z nazwami przystanków, bo tramwaje często współdzielą 
# ten sam przystanek).

#     Uwaga: jako rozwiązanie proszę wysłać zarówno kod programu jak i 
#     otrzymany plik wynikowy wynikowy.


import json
import pprint
with open('tramwaje.json', "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

trams = {}

for i in data["linia"]:
    stations = []
    if 'przystanek' in i:
        for station in i["przystanek"]:
            name = station["name"]
            stations.append(name.rsplit(' ', 1)[0])
    trams[int(i['name'])] = tuple(stations)

with open('tramwaje_out.json', 'w', encoding='utf-8') as file:
    json.dump(trams, file, ensure_ascii=False)

pprint.pprint(sorted(trams.items(), key = lambda item: len(item[1]), reverse=True))

set_stations = set()
for i in trams.values():
    set_stations = set_stations.union(set(i))

print(tuple(set_stations))