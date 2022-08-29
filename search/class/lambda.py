peaple = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Revanclaw"},
    {"name": "Draco", "house": "Slytherin"},
]


# def f(person):
#    return person["name"]

# peaple.sort(key=f)

peaple.sort(key=lambda person: person["name"])

print(peaple)
