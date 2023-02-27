class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
        
    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon
        
    def afficherInfos(self):
        print(f"Le cercle a un rayon de {self.rayon}.")
        
    def circonference(self):
        return 2 * 3.14159 * self.rayon
    
    def aire(self):
        return 3.14159 * self.rayon ** 2
    
    def diametre(self):
        return 2 * self.rayon

cercle1 = Cercle(4)
cercle2 = Cercle(7)

cercle1.afficherInfos()
print(f"Circonférence : {cercle1.circonference()}")
print(f"Aire : {cercle1.aire()}")
print(f"Diamètre : {cercle1.diametre()}\n")

cercle2.afficherInfos()
print(f"Circonférence : {cercle2.circonference()}")
print(f"Aire : {cercle2.aire()}")
print(f"Diamètre : {cercle2.diametre()}")