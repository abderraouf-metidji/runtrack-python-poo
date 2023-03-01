class Tache:
    def __init__(self, titre, description, statut='à faire'):
        self.titre = titre
        self.description = description
        self.statut = statut
        
    def marquer_comme_finie(self):
        self.statut = 'finie'
        
class ListeDeTaches:
    def __init__(self, taches=None):
        if taches is None:
            self.taches = []
        else:
            self.taches = taches
            
    def ajouter_tache(self, tache):
        self.taches.append(tache)
        
    def supprimer_tache(self, tache):
        self.taches.remove(tache)
        
    def afficher_liste(self):
        for tache in self.taches:
            print(tache.titre, tache.description, tache.statut)
            
    def filter_liste(self, statut):
        taches_filtrees = []
        for tache in self.taches:
            if tache.statut == statut:
                taches_filtrees.append(tache)
        return taches_filtrees


liste_de_taches = ListeDeTaches()

tache1 = Tache("Faire les courses.", "Acheter du lait, des oeufs et du pain.")
liste_de_taches.ajouter_tache(tache1)

tache2 = Tache("Appeler le médecin.", "Prendre rendez-vous pour une consultation.")
liste_de_taches.ajouter_tache(tache2)

tache3 = Tache("Faire du sport.", "Aller courir pendant 30 minutes.", "en cours")
liste_de_taches.ajouter_tache(tache3)

liste_de_taches.afficher_liste()

taches_a_faire = liste_de_taches.filter_liste('à faire')
for tache in taches_a_faire:
    print(tache.titre, tache.description, tache.statut)

tache1.marquer_comme_finie()

liste_de_taches.supprimer_tache(tache2)

liste_de_taches.afficher_liste()