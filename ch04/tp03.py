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


print(50*'-')


a = 1234
def the_function():
    global a
    print("start the_function()")
    a = 2
    print(a)
    print("end the_function()")


print(a)
print("before the_function()")
the_function()
print("after the_function()")
print(a)
print(50*'-')


def hello(name,firstname,age=22):
    print("Hello "+name+" "+firstname+" "+str(age))

hello("GAURAT","Frédéric",age=48)
hello(firstname="Frédéric",name="GAURAT")

print(50*'-')

def add(*l):
    print(l)
    r = 0
    for i in l:
        # r = r +i
        r += i

    return r

# l = [1,2,3,4,5]
# r = add(l)
# print(r) # 15


r = add(1,2,3,4,5)
print(r) # 15


print("toto","titi",34,False,sep=";")