

class Rectangle:

    def __init__(self,longueur,largeur) -> None:
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self,l):
        if l >0:
            self.__longueur = l

    def set_largeur(self,l):
        if l >0:
            self.__largeur = l

    def get_surface(self):
        return self.__largeur*self.__longueur
    
    def __eq__(self, value: object) -> bool:
        return self.__longueur ==  value.__longueur and self.__largeur ==  value.__largeur
    
    longueur = property(get_longueur,set_longueur)
    largeur = property(get_largeur,set_largeur)


def main():
    r = Rectangle(4,3)
    print(r.longueur)
    r.longueur = 12
    print(r.longueur)


    # print(r.get_longueur())
    # print(r.get_largeur())

    # r.set_longueur(7)
    # r.set_largeur(17)



if __name__ == '__main__':
    main()