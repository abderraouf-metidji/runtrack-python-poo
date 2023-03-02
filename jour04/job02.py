class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f'Âge : {self.age} ans')

    def bonjour(self):
        print('Hello')

    def modifierAge(self, maj_age):
        self.age = maj_age

class Eleve(Personne):
    def allerEnCours(self):
        print('Je vais en cours')

    def affichageAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignée):
        self.__matiereEnseignée = matiereEnseignée

    def enseigner(self):
        print("Le cours va commencer")

personne1 = Personne()
eleve1 = Eleve()

eleve1.affichageAge()
eleve1.bonjour()
eleve1.allerEnCours()
eleve1.modifierAge(15)
eleve1.affichageAge()

professeur1 = Professeur("Math")

professeur1.modifierAge(40)
professeur1.afficherAge()
professeur1.bonjour()
professeur1.enseigner()