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