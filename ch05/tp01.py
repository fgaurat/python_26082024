import copy
from collections import deque

l = [1, 2, 3]

print(l)

l.append(4)
print(l)

a = l.pop()
print(l)
print(a)

l2 = [4, 5, 6]
l.extend(l2)
print(l)


l.insert(2, "toto")
print(l)
# l.remove("toto")
# v = l.pop(2)
del l[2]
print(l)


# cl = l[:]
cl = l.copy()
print(cl)
l[0] = 1000
print("l", l)
print("cl", cl)


l = [
    [1, 2, 3],
    [4, 5, 6]
]

print(l)
print(l[1][1])

cl = copy.deepcopy(l)
l[1][1] = 1000
print(l)
print(cl)


print(50*'-')
l = [1, 2, 3]
print(l)
l.insert(0, -10)
print(l)
last_value = l.pop()
print(last_value)

print(l)
first_value = l.pop(0)
print(l)
print(first_value)

print(50*'-')
l = [1, 2, 3]
d = deque(l)
print(l)
print(d)
d.appendleft(-1 )
print(d)
