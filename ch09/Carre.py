from Rectangle import Rectangle

class Carre(Rectangle):


    def __init__(self, cote) -> None:
        super().__init__(cote, cote)
        self.__cote = cote

    def get_cote(self):
        return self.__cote

    def set_cote(self,cote):
        self.__cote = cote