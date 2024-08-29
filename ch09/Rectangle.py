

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
    
    # redéfinition de l'opérateur ==
    def __eq__(self, value: object) -> bool:
        return self.__longueur ==  value.__longueur and self.__largeur ==  value.__largeur
    
    # redéfinition de la convertion de type
    def __str__(self) -> str:
        largeur = self.__largeur
        longueur = self.__longueur 
        return f"{__class__.__name__} {longueur=}, {largeur=}"