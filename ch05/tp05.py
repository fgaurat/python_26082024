l = ["Valeur 01", "Valeur 02", "Valeur 03", "Valeur 04"]

for pos,item in enumerate(l):
    print(pos,item)


d = {
    "firstname": "Frédéric",
    "name": "GAURAT",
    "age": 48,
    12: "Truc",
    "projects": ["Projet 1", "Projet 2"]
}

for key in d:
    print(key,d[key])

keys = d.keys()
print(keys)

values = d.values()
print(values)

for key,value in d.items():
    print(key,value)