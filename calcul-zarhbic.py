"""
Module principal pour le calculateur Zarhbic.
Ce programme permet de calculer des expressions selon les règles du druide Zarhbic.
"""

def parse_expression(expression):
    """
    Parse une expression en listes de chiffres et d'opérateurs.

    Args:
        expression (str): Chaîne à parser (ex: "35+", "47+3*").

    Returns:
        tuple: (list[int], list[str]) ou (None, str) en cas d'erreur.
    """
    chiffres = []
    operateurs = []
    for c in expression:
        if c.isdigit():
            chiffres.append(int(c))
        elif c in {'+', '*', '-', '$'}:
            operateurs.append(c)
        else:
            return None, f"Erreur : Opérateur '{c}' non reconnu."

    if len(chiffres) < 2 and operateurs:
        return None, "Erreur : Il faut au moins deux chiffres pour un opérateur dyadique."

    return chiffres, operateurs

def calcul_zarhbic(chiffres, operateurs):
    """
    Calcule le résultat selon les règles de Zarhbic.

    Args:
        chiffres (list[int]): Liste des chiffres.
        operateurs (list[str]): Liste des opérateurs.

    Returns:
        int or str: Résultat ou message d'erreur.
    """
    if not chiffres:
        return "Erreur : Aucune expression valide."

    resultat = chiffres[0]
    for i, operateur in enumerate(operateurs):
        if i + 1 >= len(chiffres):
            return "Erreur : Nombre de chiffres insuffisant pour les opérateurs."

        next_chiffre = chiffres[i + 1]
        if operateur == '+':
            resultat += next_chiffre
        elif operateur == '*':
            resultat *= next_chiffre
        elif operateur == '-':
            resultat -= next_chiffre
        elif operateur == '$':
            resultat = int(str(resultat)[::-1])  # Inversion des chiffres

    return resultat

def main():
    """
    Boucle interactive pour saisir et calculer des expressions Zarhbic.
    """
    print("Calculateur Zarhbic - Entrez une expression (ex: 35+, 47+3*, 104+2-)")
    print("Opérateurs autorisés : +, *, -, $")
    print("Tapez 'quit' pour quitter.")

    while True:
        expression = input("\nVotre expression : ").strip()
        if expression.lower() == 'quit':
            break

        chiffres, operateurs = parse_expression(expression)
        if isinstance(chiffres, tuple) and chiffres is None:
            print(operateurs)  # Affiche le message d'erreur
            continue

        resultat = calcul_zarhbic(chiffres, operateurs)
        print(f"Résultat : {resultat}")

if __name__ == "__main__":
    main()
