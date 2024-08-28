from dataclasses import dataclass

@dataclass
class Rectangle:
    longueur:int=0
    largeur:int=0

def main():
    r = Rectangle(4,3)
    print(r.longueur)
    r.longueur = 12
    print(r.longueur)


if __name__ == '__main__':
    main()