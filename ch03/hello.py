

print("Hello")

# theworldisflat
# TheWorldIsFlat => PascalCase, UpperCamelCase > Class
# theWorldIsFlat => camelCase > propriété,variables
# the_world_is_flat => snake_case > variables
# the-world-is-flat => kebab-case, train-case, spin-case


# Inférence de type
the_world_is_flat = True # False
s = "toto"# 'toto'
i = 22

d = 1.2

print(the_world_is_flat)

print(type(the_world_is_flat))
print(type(s))
print(type(i))
print(type(d))


if the_world_is_flat:
    print("Be careful not to fall off!")

print("La fin")



a = 17/3
b = 17//3
c = 2**2
print(a)
print(b)
print(c)



s = 'L\'orage gronde'
s1 = "L'orage\tgronde\nVoilà"
s11 = 'L\'orage\tgronde\nVoilà'
print(s)
print(s1)
p = "c:\\tp_python\\new_tp"
p1 = r"c:\tp_python\new_tp" # mode raw/brut
print(p)
print(p1)

s2 = """Ligne 01
Ligne 02
Ligne 03
Ligne 04
La fin
"""

print(s2)

t = "2"+3

print("-"*50)
a=2
b="toto"
c = a*b
print(c)
print("-"*50)

b="Bonjour"
print(b[3])
print(len(b)) #length
print(b[-1])
# print(b[-75])

print(b[0:3]) # b[0:3] O inc, 3 excl
print(b[:3]) # b[:3] O inc, 3 excl
print(b[2:5]) # b[2:5] 2 inc, 5 excl
print(b[2:]) 
print(b[:]) 
print(b[2:4]) # b[2:4] 2 inc, 4 excl

print(b[2:456])

# b[0]="N"
# b="Nonjour"
print(b)
b = "toto"


a =2
b =2
print(hex(id(a)))
print(hex(id(b)))
b=3
print(hex(id(a)))
print(hex(id(b)))
print(50*'-')

squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[-1])
print(squares[3])
print(squares[3:])
squares2 = [1, 4, 9, 16, 25]
squares3 = squares + squares2
print(squares3)
squares[0] = 1000
print(squares)
squares.append(36)
print(squares)
print(len(squares))
print(max(squares))
print(min(squares))