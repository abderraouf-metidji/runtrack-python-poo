class Vehicule:
    def __init__(self, marque, modèle, année, prix):
        self.marque = marque
        self.modèle = modèle
        self.année = année
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque : {self.marque} ")
        print(f"Modèle : {self.modèle}")
        print(f"Année : {self.année}")
        print(f"Prix : {self.prix}")

    def demarrer(self):
        print("Attention, je roule.")

class Voiture(Vehicule):
    def __init__(self, marque, modèle, année, prix):
        Vehicule.__init__(self, marque, modèle, année, prix)
        self.portes = 4

    def informationsVehicule(self):
        Vehicule.informationsVehicule(self)
        print(f"Nombre de portes : {self.portes}")

    def demarrer(self):
        print("Attention, je roule en voiture.")


class Moto(Vehicule):
    def __init__(self, marque, modèle, année, prix):
        Vehicule.__init__(self, marque, modèle, année, prix)
        self.roue = 2

    def informationsVehicule(self):
        Vehicule.informationsVehicule(self)
        print(f"Nombre de roue : {self.roue}")

    def demarrer(self):
        print("Attention, je roule en moto.")


voiture1 = Voiture("Mercedes", "Classe A", 2020, 18500)
voiture1.informationsVehicule()
voiture1.demarrer()

moto1 = Moto("Yamaha", "1200 Vmax", 1987, 4500)
moto1.informationsVehicule()
moto1.demarrer()