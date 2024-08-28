
def main():
    # with open('hello.txt','w') as f: # mode écriture
    with open('hello.txt','a') as f: # mode ajout (append)
        # f.write('Hello\n')
        print("Hello",file=f)



if __name__ == '__main__':
    main()