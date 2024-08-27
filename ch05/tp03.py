

s1 = {2, 3, 4, 5, 1, 2, 2, 1}
s2 = {5, 6, 7, 1, 2, 4}
print(type(s1))
print(s2)
s3 = s1 & s2
print(s3)

l = ["Valeur 01","Valeur 01","Valeur 02","Valeur 03","Valeur 03","Valeur 01"]
# s = set(l)
# dedup_l = list(s)
print(set(l))
dedup_l = list(set(l))
print(dedup_l)
