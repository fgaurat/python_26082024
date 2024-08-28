from Rectangle import Rectangle

def main():
    r = Rectangle(4,3)
    print(r.get_longueur())
    print(r.get_largeur())

    r.set_longueur(7)
    r.set_largeur(17)

    print(r.get_longueur())
    print(r.get_largeur())
    
    r.set_longueur(-7)
    print(r.get_longueur())

    print(r.get_surface())
    
    r = Rectangle(4,3)
    r1 = Rectangle(4,3)
    
    print(id(r),id(r1))
    if r==r1:
        print("ok")
    else:
        print("ko")



if __name__ == '__main__':
    main()

