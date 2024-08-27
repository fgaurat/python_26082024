

t = 1, 2, 3  # t = (1,2,3)

# s = []
# s = {"":""}


t1 = "toto", "tutu", "tata"  # ('toto', 'tutu', 'tata')
t2 = ("toto", "tutu", "tata")  # ('toto', 'tutu', 'tata')

print(t2)
print(type(t2))  # tuple


def f():

    return "valeur 1", "valeur 2"


a, b = f()

print(a)
print(b)

print(t1[0])
print(t1[1])

print(len(t1))
# t[0] = "truc"

l1 = ["a", 23, False]
print(l1)
# print(l1[0]+2)
del l1[0]
print(l1[0]+2)
t1 = ["a", 23, False]
