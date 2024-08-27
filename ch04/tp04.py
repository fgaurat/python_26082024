

def old_mult2(l):
    r = []
    for i in l:
        r.append(i*2)
    return r


def mult2(item: int) -> int:
    """ mult 2 item"""
    return item*2


l = [1, 2, 3, 4]
# l2 = list(map(mult2,l))
l2 = list(map(lambda i: i*2, l))
print(l)
print(l2)  # [2,4,6,8]


def l(i, j): return i*j


print(l(2, 3))
