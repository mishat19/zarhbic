"""
Module pour le calculateur Zarhbic utilisant une pile.
Lit les calculs depuis un fichier texte et affiche les résultats.
"""
import os

def lire_fichier(nom_fichier):
    """
    Lit un fichier texte contenant les calculs de Zarhbic.

    Args:
        nom_fichier (str): Nom du fichier à lire.

    Returns:
        list: Liste des lignes du fichier, ou None en cas d'erreur.
    """
    # Vérifie si le fichier existe
    if not os.path.exists(nom_fichier):
        print(f"Erreur : Le fichier '{nom_fichier}' n'existe pas.")
        return None

    # Vérifie si le fichier est lisible
    if not os.access(nom_fichier, os.R_OK):
        print(f"Erreur : Le fichier '{nom_fichier}' n'est pas lisible.")
        return None

    # Lit le fichier avec un encodage explicite
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            return [ligne.strip() for ligne in fichier if ligne.strip()]
    except UnicodeDecodeError:
        print(f"Erreur : Le fichier '{nom_fichier}' n'est pas encodé en UTF-8.")
        return None
    except PermissionError:
        print(f"Erreur : Permission refusée pour lire '{nom_fichier}'.")
        return None
    except OSError as e:
        print(f"Erreur système lors de la lecture de '{nom_fichier}' : {e}")
        return None

def parser_ligne(ligne):
    """
    Parse une ligne du fichier en liste de chiffres et d'opérateurs.

    Args:
        ligne (str): Ligne à parser (ex: "3 5 +").

    Returns:
        tuple: (list[int], list[str]) ou (None, str) en cas d'erreur.
    """
    elements = ligne.split()
    chiffres = []
    operateurs = []
    for element in elements:
        if element.isdigit():
            chiffres.append(int(element))
        elif element in {'+', '*', '-', '/', '$'}:
            operateurs.append(element)
        else:
            return None, f"Erreur : Élément '{element}' non reconnu."

    if len(chiffres) < 2 and operateurs:
        return None, "Erreur : Il faut au moins deux chiffres pour un opérateur dyadique."

    return chiffres, operateurs

def calcul_avec_pile(chiffres, operateurs):
    """
    Calcule le résultat en utilisant une pile.

    Args:
        chiffres (list[int]): Liste des chiffres.
        operateurs (list[str]): Liste des opérateurs.

    Returns:
        int or str: Résultat ou message d'erreur.
    """
    pile = []
    # On empile d'abord tous les chiffres
    for chiffre in chiffres:
        pile.append(chiffre)

    # On applique les opérateurs
    for operateur in operateurs:
        if len(pile) < 2:
            return "Erreur : Pas assez de chiffres dans la pile pour appliquer l'opérateur."

        droit = pile.pop()
        gauche = pile.pop()

        if operateur == '+':
            pile.append(gauche + droit)
        elif operateur == '*':
            pile.append(gauche * droit)
        elif operateur == '-':
            pile.append(gauche - droit)
        elif operateur == '/':
            if droit == 0:
                return "Erreur : Division par zéro."
            pile.append(gauche // droit)  # Division entière pour rester sur des entiers
        elif operateur == '$':
            # Inversion des deux derniers chiffres (ex: 12$ → 21)
            pile.append(int(str(droit) + str(gauche)))
        else:
            return f"Erreur : Opérateur '{operateur}' non géré."

    return pile[0] if pile else "Erreur : Aucune valeur dans la pile."

def main():
    """
    Lit les calculs depuis un fichier, les parse, et affiche les résultats.
    """
    nom_fichier = "calculs.txt"
    lignes = lire_fichier(nom_fichier)
    if lignes is None:
        return

    print(f"Calculs lus depuis '{nom_fichier}' :")
    for i, ligne in enumerate(lignes, 1):
        print(f"\nCalcul n°{i} : {ligne}")
        chiffres, operateurs = parser_ligne(ligne)
        if chiffres is None:
            print(operateurs)  # Affiche le message d'erreur
            continue

        resultat = calcul_avec_pile(chiffres, operateurs)
        print(f"→ Résultat : {resultat}")

if __name__ == "__main__":
    main()
