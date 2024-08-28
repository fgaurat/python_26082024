def fib(n):    # write Fibonacci series up to n
    """
    Doc : Print a Fibonacci series up to n.
    Ligne 01
    """ 
    # Docstring
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
r = fib(2000)
print(r)

# Procédure -> pas de retour
# Fonction ->  retourne une valeur

def fib2(n=10):    # write Fibonacci series up to n
    """
    Doc : Return a Fibonacci series up to n.
    Ligne 01
    """ 
    # Docstring
    l = []
    a, b = 0, 1
    while a < n:
        l.append(a)
        a, b = b, a+b

    return l


r = fib2(2000)
print(r) # [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597 ]

r = fib2(20)
print(r)
r = fib2()
print(r)


print(50*'-')

# hoisting : remontée d'une variable dans une function
a = 1234
def the_function():
    global a
    print("start the_function()")
    # a = 2
    print(a)
    print("end the_function()")


# print(a)
print("before the_function()")
the_function()
print("after the_function()")
# print(a)
print(50*'-')

def hello(name,firstname,age=22):
    print("Hello "+name+" "+firstname+" "+str(age))

# par position
hello("GAURAT","Frédéric")

# par position & keyword
hello("GAURAT","Frédéric",age=48)

# par keyword
hello(firstname="Frédéric",name="GAURAT")

print(50*'-')

# par position en nombre variable
def add(*l):
    print(l)
    r = 0
    for i in l:
        # r = r +i
        r += i

    return r

l = [1,2,3,4,5]
r = add(*l) # add(1,2,3,4,5)
print(r) # 15

a = 1 # écriture, affectation de a 
b = a # lecture de a


r = add(1,2,3,4,5)
r = add(1,2,3,4,5,56,76)
print(r) # 15


print("toto","titi",34,False,sep=";")

a,b = 0,1 # a=0 et b =1
a,b = [0,1] # a=0 et b =1
print(a)
print(b)

# a,b = 0,1,3 # ValueError: too many values to unpack (expected 2)

# a,b,c = 0,1 # ValueError: not enough values to unpack (expected 3, got 2)

a,b,*c = 0,1,2,3,4,5

print(a,b,c)
# l1 = [0,1]
# l2 = (0,1)
# print(type(l1))
# print(type(l2))


l = [1,2,3,4]

a,b,*c = l # pack

print(c) # [3, 4]
print(*c) # unpack
print(3,4) # unpack


# par keywords en nombre variable
def hello(**kwargs): # keyword arguments
    print(kwargs) # dict
    print(kwargs['firstname'])
    print(kwargs['name'])


hello(firstname="Frédéric",name="GAURAT")

i =2
s = 'toto'

l = [1,2,3,4]

d = {
    'firstname': 'Frédéric', 
    'name': 'GAURAT'
    }

print(l[1])
print(d['firstname'])



l = ["admin","12345"]

login = l[0]
passw = l[1]

d = {
    "login":"admin",
    "passw":"12345",
}

login = d["login"]
passw = d["passw"]
