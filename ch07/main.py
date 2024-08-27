import sys
def main():
    a = 2
    b = 3
    c = a/b
    print(a, b, c)
    
    # f-string
    # s = f"{a=}, {b=}, {a}/{b} = {c:.3}"
    # s = f"{a=}, {b=}, {a}/{b} = {c*100:.2f}%"
    s = f"{a=}, {b=}, {a}/{b} = {c:.2%}" # interpolation

    a = "toto"
    print(f"{a:<10}",'-')
    print(f"{a:>10}")
    print(s)

    print(50*"-")

    l = ["Valeur 01", "Valeur 02", "Valeur 03"]

    # s = f"v1={l[0]}, v2={l[1]}, v3={l[2]}"
    
    # s = ", v3={2}, v1={0}, v2={1}".format(l[0],l[1],l[2])
    # s = "v1={},  v2={}, v3={}".format(l[0],l[1],l[2])
    s = "v1={},  v2={}, v3={}".format(*l)
    
    # s = "v1={0}, v2={1}, v3={2}".format()
    print(s)

    
    # s = "v1={0}, v2={1}, v3={2}".format(*l)
    s = "v1={}, v2={}, v3={}".format(*l)
    print(s)


    d = {
        "firstname": "Frédéric",
        "name": "GAURAT",
        "age": 48,
    }
    s = "infos : {theFirstname} {theName}".format(theName=d['name'],theFirstname=d['firstname'])
    print(s)
    # l = ["Valeur 01", "Valeur 02", "Valeur 03"]
    # print(l) => ["Valeur 01", "Valeur 02", "Valeur 03"]
    # print(*l) => "Valeur 01", "Valeur 02", "Valeur 03"


    # d = {"k1":"valeur 1", "k2": "valeur 2"}
    # print(d) => {"k1":"valeur 1", "k2": "valeur 2"}
    # print(**d)# error print(k1="valeur 1",k2="valeur 2")
    
    # s = "infos : {firstname} {name}".format(name=d['name'],firstname=d['firstname'])
    s = "infos : {firstname} {name}".format(**d)



if __name__ == '__main__':
    main()
