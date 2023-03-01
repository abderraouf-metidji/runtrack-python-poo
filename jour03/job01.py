class Ville:
    def __init__(self, nom_ville, nb_habitants):
        self.__nom_ville = nom_ville
        self.__nb_habitants = nb_habitants

    def get_nom_ville(self):
        return self.__nom_ville

    def get_nb_habitants(self):
        return self.__nb_habitants

    def set_nb_habitants(self, nb_habitants):
        self.__nb_habitants = nb_habitants

class Personne:
    def __init__(self, nom_personne, age, ville):
        self.__nom_personne = nom_personne
        self.__age = age
        self.__ville = ville

    def get_nom(self):
        return self.__nom_personne

    def get_age(self):
        return self.__age

    def get_ville(self):
        return self.__ville.get_nom_ville()

    def ajouterPopulation(self):
        current_population = self.__ville.get_nb_habitants()
        self.__ville.set_nb_habitants(current_population + 1)

Paris = Ville('Paris', 1000000)

print(f'Population de la ville de {Paris.get_nom_ville()} est de {Paris.get_nb_habitants()}')

Marseille = Ville('Marseille', 861635)

print(f'Population de la ville de {Marseille.get_nom_ville()} est de {Marseille.get_nb_habitants()}')

John = Personne('John', '45 ans', Paris)
John.ajouterPopulation()

Myrtille = Personne('Myrtille', '4 ans', Paris)
Myrtille.ajouterPopulation()

Chloé = Personne('Chloé', '18 ans', Marseille)
Chloé.ajouterPopulation()

print(f'Mise à jour de la population de la ville de {Paris.get_nom_ville()} {Paris.get_nb_habitants()} habitants')

print(f'Mise à jour de la population de la ville de {Marseille.get_nom_ville()} {Marseille.get_nb_habitants()} habitants')