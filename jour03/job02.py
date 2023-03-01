class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde_initial, autorisation_decouvert):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde_initial
        self.__decouvert_autorise = autorisation_decouvert
        
    def afficher(self):
        print("Détail du compte :")
        print(f"Titulaire : {self.__prenom} {self.__nom}")
        print(f"Numéro de compte : {self.__numero_compte}")
        print(f"Solde : {self.__solde} €")
        
    def afficherSolde(self):
        print(f"Le solde du compte est de {self.__solde} €")
        
    def versement(self, montant):
        self.__solde += montant
        print(f"{montant} € ont été ajoutés au compte.")
        self.afficherSolde()
        
    def retrait(self, montant):
        if self.__decouvert_autorise or (self.__solde - montant) >= 0:
            self.__solde -= montant
            print(f"{montant} € ont été retirés du compte.")
            self.afficherSolde()
        else:
            print("Opération impossible : solde insuffisant.")
            
    def agios(self):
        if self.__solde < 0:
            frais = abs(self.__solde) * 0.05
            self.__solde -= frais
            print(f"{frais} € d'agios ont été appliqués.")
            self.afficherSolde()
            
    def virement(self, compte_destinataire, montant):
        if compte_destinataire.__numero_compte == self.__numero_compte:
            print("Opération impossible : le compte émetteur et le compte destinataire sont identiques.")
        elif (not self.__decouvert_autorise and self.__solde - montant < 0):
            print("Opération impossible : solde insuffisant.")
        else:
            self.__solde -= montant
            compte_destinataire.__solde += montant
            print(f"{montant} € ont été transférés vers le compte {compte_destinataire.__numero_compte}.")
            self.afficherSolde()
            compte_destinataire.afficherSolde()


# Création compte
compte1 = CompteBancaire("22233114", "Doe", "John", 200, False)

compte1.afficher()
compte1.versement(200)
compte1.retrait(200)
compte1.retrait(1500)
compte1.agios()

# Création deuxième compte + virement
compte2 = CompteBancaire("59895559", "Doe", "Jack", -200, True)

compte2.afficher()
montant_virement = 200
compte1.virement(compte2, montant_virement)
compte2.afficher()