l = ["Valeur 01","Valeur 02","Valeur 03","Valeur 04"]

for item in l:
    print(item)


for i in range(3,15,2):
    print(i)


# 0 Valeur 01 
# 1 Valeur 02
# 2 Valeur 03
# 3 Valeur 04

for i in range(len(l)):
    print(str(i)+" "+l[i])


r = range(5) # [0,1,2,...]
l = list(r)
print(l)


print(50*'-')


l = [2,56,3,7,90,54]
to_found = 777

# for i in l:
#     if i == to_found:
#         print("ok "+str(i))
#         continue
#     print(i)


for i in l:
    print(i)
    if i == to_found:
        print("ok "+str(i))
        break
else: # s'éxécute si la boucle n'a pas été interrompue
    print("pas de break")


