def length(lst):
    """Renvoie la longueur de la liste."""
    return len(lst)


def mean(lst):
    """Calcule la moyenne des éléments de la liste."""
    if len(lst) == 0:
        return 0  # Si la liste est vide, renvoie 0
    return sum(lst) / len(lst)


def range_of_list(lst):
    """Renvoie la différence entre le max et le min de la liste."""
    if len(lst) == 0:
        return 0  # Si la liste est vide, renvoie 0
    return max(lst) - min(lst)


# Exemple d'utilisation
nombres = [1, 2, 3, 4, 5]

print("Longueur de la liste:", length(nombres))  # Sortie : 5
print("Moyenne de la liste:", mean(nombres))  # Sortie : 3.0
print("Plage de la liste:", range_of_list(nombres))  # Sortie : 4
