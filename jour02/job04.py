class Student:
    def __init__(self, nom, prenom, num_etudiant, credits = 0):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__credits = credits
        self.__level = self.__studentEval()

    def get_nom(self):
        return self.__nom
        
    def get_prenom(self):
        return self.__prenom
    
    def get_num_etudiant(self):
        return self.__num_etudiant
    
    def get_credits(self):
        return self.__credits

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__studentEval()
        else:
            print('Le nombre de crédits doit être supérieur à zéro')

    def get_credits(self):
        return self.__credits
    
    def studentInfo(self):
        print("Nom :", self.__nom)
        print("Prenom :", self.__prenom)
        print("Indentifiant :", self.__num_etudiant)
        print("Niveau :", self.__level)

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Tres bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    
john_doe = Student("Doe", "John", 145)

john_doe.add_credits(15)
john_doe.add_credits(25)
john_doe.add_credits(35)

john_doe.studentInfo()