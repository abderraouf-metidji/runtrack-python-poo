class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def viellir(self):
        self.age += 1

    def nommer(self, nom):
        self.nom = nom

animal = Animal()

print("Mon animal est âgé de : ", animal.age, "ans")

animal.viellir()

print("Mon animal est maintenant âgé de : ", animal.age, "ans")

animal.nommer("Luna")

print("L'animal se nomme : ", animal.nom)