class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def getlongueur(self):
        return self.__longueur
    
    def setlongueur(self, longueur):
        self.__longueur = longueur

    def getlargeur(self):
        return self.__largeur
    
    def setlargeur(self, largeur):
        self.__largeur = largeur

    def périmètre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__largeur * self.__longueur

class Parallélépipède(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.hauteur = hauteur
        

    def volume(self):
        return self.getlongueur() * self.getlargeur() * self.hauteur

rectangle1 = Rectangle(2, 4)

print(rectangle1.getlongueur())
print(rectangle1.getlargeur())
print(rectangle1.périmètre())
print(rectangle1.surface())

parallelepipede1 = Parallélépipède(2, 4, 3)

print(parallelepipede1.volume())