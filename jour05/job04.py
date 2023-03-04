def trouver_max(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        max_precedent = trouver_max(liste[1:])
        if liste[0] > max_precedent:
            return liste[0]
        else:
            return max_precedent
        
result = trouver_max([74, 56, 5, 71, 60, 42, 44, 68, 47, 63, 9, 2])
print(result)