
def main():
    a = 2
    b = 3
    c = a/b
    print(a, b, c)
    # f-string
    # s = f"{a=}, {b=}, {a}/{b} = {c:.3}"
    # s = f"{a=}, {b=}, {a}/{b} = {c*100:.2f}%"
    s = f"{a=}, {b=}, {a}/{b} = {c:.2%}"
    print(s)

    a = "toto"
    print(f"{a:<10}")
    print(f"{a:>10}")

    print(50*"-")

    l = ["Valeur 01", "Valeur 02", "Valeur 03"]

    s = "v1={0}, v2={1}, v3={2}".format("Valeur 01", "Valeur 02", "Valeur 03")
    print(s)

    # s = "v1={0}, v2={1}, v3={2}".format(*l)
    s = "v1={}, v2={}, v3={}".format(*l)
    print(s)


    d = {
        "firstname": "Frédéric",
        "name": "GAURAT",
        "age": 48,
    }
    # s = "infos : {firstname} {name}".format(name=d['name'],firstname=d['firstname'])
    # print(s)

    s = "infos : {firstname} {name}".format(**d)
    print(s)

    n = "fred"
    h = f"Bonjour {n}"
    print(h)


    l = [1,2]
    s = "v1 = {}, v2 = {}".format(l[0],l[1])
    print(s)


if __name__ == '__main__':
    main()
