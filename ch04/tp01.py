to_find = 12
found = False

while not found: 
    value = int(input('Saisir une valeur :'))

    if value>to_find:
        print("c'est moins")
    elif value<to_find:
        print("c'est plus")
    else:
        print("ok")
        found = True