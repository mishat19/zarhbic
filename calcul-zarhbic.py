def calcul_zarhbic(expression):
    """
    Calcule le résultat d'une expression selon les règles de Zarhbic.
    Exemples :
    - "35+" → 3 + 5 = 8
    - "47+3*" → (4 + 7) + (7 * 3) = 11 + 21 = 32 (approximation)
    - "104+2-" → (1 + 0) + (0 + 4) - 2 = 1 + 4 - 2 = 3 (à adapter selon ta logique)
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

    # 3. Application des règles (hypothèse : opérateurs entre chaque paire de chiffres)
    resultat = chiffres[0]
    for i in range(len(operateurs)):
        if i + 1 >= len(chiffres):
            break  # Évite les erreurs d'index
        operateur = operateurs[i]
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
    print("Calculateur Zarhbic - Entrez une expression (ex: 35+, 47+3*, 104+2-)")
    print("Opérateurs autorisés : +, *, -, $")
    print("Tapez 'quit' pour quitter.")

    while True:
        expression = input("\nVotre expression : ").strip()
        if expression.lower() == 'quit':
            break

        try:
            resultat = calcul_zarhbic(expression)
            print(f"Résultat : {resultat}")
        except Exception as e:
            print(f"Erreur : {e}")

if __name__ == "__main__":
    main()
