class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Les coordonnées sont: {self.x}, {self.y}")

    def afficherX(self):
        print(f"La valeur de x est : {self.x}")

    def afficherY(self): 
        print(f"La valeur de y : {self.y}")

    def changerX(self, nouveauX):
        self.x = nouveauX

    def changerY(self, nouveauY):
        self.y = nouveauY

p = Point(2, 8)


p.afficherLesPoints()
p.afficherX()
p.afficherY()
p.changerX(5)
p.changerY(10)
p.afficherLesPoints()