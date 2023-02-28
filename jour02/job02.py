class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages

    def get_titre(self):
        return self.__titre
    
    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_pages(self):
        return self.__pages
    
    def set_pages(self, new_pages):
        if isinstance(new_pages, int) and new_pages > 0:
            self.__pages = new_pages
        else:
            print("Erreur il faut que le nombre soit un entier positif.")
            

livre = Livre("La nuit rouge", "Abdou", 355)

print("Auteur :", livre.get_auteur())
print("Titre :", livre.get_titre())
print("Nombre de pages:", livre.get_pages())

livre.set_auteur("Abderraouf")
livre.set_titre("L'avenir")
livre.set_pages(200)

print("Auteur :", livre.get_auteur())
print("Titre :", livre.get_titre())
print("Nombre de pages:", livre.get_pages())

livre.set_pages(-100)

print("Nombre de pages:", livre.get_pages())