import json


def main():
    # with open('hello.txt','w') as f: # mode écriture
    with open('hello.txt','a') as f: # mode ajout (append)
        # f.write('Hello\n')
        print("Hello",file=f)

    
    with open('hello.txt','r') as f: # mode read (lecture)

        # content = f.read() # chargement dans un scalaire, chargement complet en mémoire
        # print(content)
        # lines = content.splitlines()
        # print(lines)

        # dirty_lines = f.readlines() # chargement dans une liste, chargement complet en mémoire
        # lines = [line.strip() for line in dirty_lines]
        # print(lines)
        
        for line in f: # chargement de la ligne courante
            print(line.strip())

    
    l = [
        {"name":"GAURAT","firstname":"Fred"},
        {"name":"MARTIN","firstname":"Jean"},
        {"name":"DURAND","firstname":"Louis"}
    ]

    print(l)
    with open('data.json','w') as f:
        json.dump(l,f)
        # json.dump(l,f,indent=4)
    
    with open('data.json','r') as f:
        l2 = json.load(f)
        print(l2)
        print(l2[0])
        print(l2[0]["name"])

if __name__ == '__main__':
    main()