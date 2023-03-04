def longueur(chaine):
    if chaine == "":
        return 0
    else:
        return 1 + longueur(chaine[1:])
    
chaine = str(input("Entrez un mot : "))
result = longueur(chaine)
print("La chaine de caractère contient {} lettres" .format(longueur(chaine)))