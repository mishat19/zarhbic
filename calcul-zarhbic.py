"""
Module principal pour le calculateur Zarhbic.
Ce programme permet de calculer des expressions selon les règles du druide Zarhbic.
"""

def calcul_zarhbic(expression):
    """
    Calcule le résultat d'une expression selon les règles de Zarhbic.

    Args:
        expression (str): Chaîne représentant l'expression à calculer (ex: "35+", "47+3*").

    Returns:
        int or str: Résultat du calcul ou message d'erreur.
    """
    chiffres = []
    operateurs = []

    # 1. Parsing de l'expression
    for c in expression:
        if c.isdigit():
            chiffres.append(int(c))
        else:
            operateurs.append(c)

    # 2. Vérification de la validité
    if len(chiffres) < 2 and operateurs:
        return "Erreur : Il faut au moins deux chiffres pour un opérateur dyadique."

    # 3. Application des règles
    resultat = chiffres[0]
    for i, operateur in enumerate(operateurs):
        if i + 1 >= len(chiffres):
            break  # Évite les erreurs d'index
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
    Fonction principale : boucle interactive pour saisir et calculer des expressions Zarhbic.
    """
    print("Calculateur Zarhbic - Entrez une expression (ex: 35+, 47+3*, 104+2-)")
    print("Opérateurs autorisés : +, *, -, $")
    print("Tapez 'quit' pour quitter.")

    while True:
        try:
            expression = input("\nVotre expression : ").strip()
            if expression.lower() == 'quit':
                break

            resultat = calcul_zarhbic(expression)
            print(f"Résultat : {resultat}")

        except ValueError as ve:
            print(f"Erreur de valeur : {ve}")
        except IndexError as ie:
            print(f"Erreur d'index : {ie}")
        except Exception:
            print("Une erreur inattendue est survenue. Veuillez réessayer.")

if __name__ == "__main__":
    main()
