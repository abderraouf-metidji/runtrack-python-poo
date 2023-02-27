class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA)
    
    def CalculerTVA(self):
        return self.prixHT * (1 + self.TVA) - self.prixHT
    
    def afficher(self):
        print("Nom :", self.nom)
        print("Prix HT :", self.prixHT)
        print("TVA :", self.CalculerTVA())
        print("Prix TTC :", self.CalculerPrixTTC())
    
    def modifier_nom(self, nom):
        self.nom = nom
        
    def modifier_prixHT(self, prixHT):
        self.prixHT = prixHT
        
    def get_nom(self):
        return self.nom
    
    def get_prixHT(self):
        return self.prixHT
    
    def get_TVA(self):
        return self.TVA


produit1 = Produit("Xbox", 400, 0.2)
produit2 = Produit("Ordinateur", 1700, 0.2)

produit1.afficher()
produit2.afficher()

produit1.modifier_nom("Playstation")
produit1.modifier_prixHT(500)
produit1.afficher()

produit2.modifier_nom("Télévision 4k")
produit2.modifier_prixHT(800)
produit2.afficher()