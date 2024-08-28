

class Rectangle:

    def __init__(self,longueur,largeur) -> None:
        self.__longueur = longueur
        self.__largeur = largeur

    @property # decorator
    def longueur(self):
        return self.__longueur
    
    @property # decorator
    def largeur(self):
        return self.__largeur

    @longueur.setter
    def longueur(self,l):
        if l >0:
            self.__longueur = l
    
    @largeur.setter
    def largeur(self,l):
        if l >0:
            self.__largeur = l

    def get_surface(self):
        return self.__largeur*self.__longueur
    
    def __eq__(self, value: object) -> bool:
        return self.__longueur ==  value.__longueur and self.__largeur ==  value.__largeur
    


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