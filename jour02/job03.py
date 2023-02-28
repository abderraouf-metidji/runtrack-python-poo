class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True

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
            
    def verification(self):
        return self.__disponible
        
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre n'est plus disponible.")
        else:
            print("Le livre a été emprunté")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas été emprunté.")

livre = Livre("La nuit rouge", "Abdou", 355)

livre.verification()

livre.emprunter()

livre.verification()

livre.emprunter()

livre.rendre()

livre.rendre()