from pprint import pprint
import json


# convertir customers.csv -> customers.json

# id,first_name,last_name,email,gender,ip_address
# 1,Shena,Anthonies,santhonies0@unblog.fr,Female,140.172.40.54
# 2,Johann,Plaistowe,jplaistowe1@state.gov,Male,162.245.35.139

# [
#    {
#     "id":1,
#     "first_name":"Shena",
#     "last_name":"Anthonies",
#     "email":"santhonies0@unblog.fr",
#     "gender":"Female",
#     "ip_address":"140.172.40.54"
#   },
#   ...
# ]


# l = ["toto",'titi']

# for i in l:
#     print(i)

# [i for i in l] #comprehension list

# a = 2 
# l = [1,2,3]

def main():
    
    # Clefs du dictionnaires : 1ére ligne du fichier
    # Data : toutes les lignes après la première

    customers = []

    with open('customers.csv') as f: # lecture  par défaut  open('customers.csv',"r")
        lines = [line.strip() for line in f.readlines()]
        header = lines[0].split(",")
        
        
        all_data = lines[1:]
        for data in all_data:
            data = data.split(",")
            d={}
            
            # for i in range(len(header)):
            #     d[header[i]] = data[i]           
            
            for i,key in enumerate(header):
                d[key] = data[i]
            customers.append(d)


    with open('customers.json','w') as f:
        json.dump(customers,f,indent=4)


if __name__ == '__main__':
    main()