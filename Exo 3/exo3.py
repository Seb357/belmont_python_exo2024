def trouver_max(liste):
    if not liste:
        return None
    
    maximum = liste[0]
    for nombre in liste:
        if nombre > maximum:
            maximum = nombre
    return maximum

print("le maximum est", trouver_max([1, 2, 3, 4, 5, 6, 7, 8, 9]))